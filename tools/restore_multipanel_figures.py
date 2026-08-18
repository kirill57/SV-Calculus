#!/usr/bin/env python3
"""Restore dropped extra tikzpictures in PreTeXt figures from original LaTeX."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspaces/SV-Calculus")
TEX_ROOT = ROOT / "Single_Variable_Calculus_Change__Accumulation__and_Approximation"
XML_ROOT = ROOT / "source"


def xml_escape_tikz(tikz: str) -> str:
    return tikz.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def extract_figure_envs(tex: str) -> list[tuple[str, str]]:
    """Return (label, figure_body) for each figure with a \\label{fig:...}."""
    out = []
    i = 0
    begin = r"\begin{figure}"
    end = r"\end{figure}"
    while True:
        start = tex.find(begin, i)
        if start < 0:
            break
        stop = tex.find(end, start)
        if stop < 0:
            break
        body = tex[start : stop + len(end)]
        m = re.search(r"\\label\{(fig:[^}]+)\}", body)
        if m:
            out.append((m.group(1), body))
        i = stop + len(end)
    return out


def extract_tikzpictures(fig_tex: str) -> list[str]:
    pics = []
    i = 0
    b, e = r"\begin{tikzpicture}", r"\end{tikzpicture}"
    while True:
        start = fig_tex.find(b, i)
        if start < 0:
            break
        stop = fig_tex.find(e, start)
        if stop < 0:
            break
        stop += len(e)
        pics.append(fig_tex[start:stop])
        i = stop
    return pics


def panel_caption_after(fig_tex: str, pic: str) -> str | None:
    """Grab a short leftover label such as 'Trip A' after a tikzpicture."""
    idx = fig_tex.find(pic)
    if idx < 0:
        return None
    rest = fig_tex[idx + len(pic) :]
    nxt = re.search(r"\\(begin\{tikzpicture\}|end\{minipage\}|caption|label|end\{figure\})", rest)
    chunk = rest[: nxt.start()] if nxt else rest
    chunk = re.sub(r"%.*", "", chunk)
    chunk = chunk.replace(r"\hfill", " ").replace(r"\centering", " ")
    chunk = re.sub(r"\s+", " ", chunk).strip()
    if chunk and len(chunk) <= 40 and "\\" not in chunk:
        return chunk
    return None


def attach_below_label(pic: str, label: str) -> str:
    extra = (
        "\n\\node[font=\\small\\bfseries, anchor=north, yshift=-6pt] "
        f"at (current bounding box.south) {{{label}}};\n"
    )
    return pic[:- len(r"\end{tikzpicture}")] + extra + r"\end{tikzpicture}"


def image_block(xml_id: str, tikz: str) -> str:
    return (
        f'    <image xml:id="{xml_id}">\n'
        f"      <latex-image>\n{xml_escape_tikz(tikz)}\n"
        f"      </latex-image>\n"
        f"    </image>"
    )


def replacement_inner(fig_id: str, pics: list[str], captions: list[str | None], sidebyside: bool) -> str:
    blocks = []
    for i, pic in enumerate(pics):
        if captions[i]:
            pic = attach_below_label(pic, captions[i])
        blocks.append(image_block(f"{fig_id}-panel-{i+1}", pic))
    joined = "\n".join(blocks)
    if sidebyside and len(pics) == 2:
        return (
            '    <sidebyside widths="48% 48%" valign="bottom">\n'
            f"{joined}\n"
            "    </sidebyside>"
        )
    if sidebyside and len(pics) == 3:
        return (
            '    <sidebyside widths="32% 32% 32%" valign="bottom">\n'
            f"{joined}\n"
            "    </sidebyside>"
        )
    if sidebyside and len(pics) >= 4:
        pct = 23 if len(pics) == 4 else max(12, 90 // len(pics))
        widths = " ".join([f"{pct}%"] * len(pics))
        return (
            f'    <sidebyside widths="{widths}" valign="bottom">\n'
            f"{joined}\n"
            "    </sidebyside>"
        )
    return joined


def find_xml_figure(fig_id: str) -> tuple[Path, str] | None:
    """Return (path, full figure element text) matching xml:id."""
    pattern = re.compile(
        rf'<figure xml:id="{re.escape(fig_id)}">[\s\S]*?</figure>',
        re.M,
    )
    for path in XML_ROOT.rglob("*.xml"):
        text = path.read_text(encoding="utf-8")
        m = pattern.search(text)
        if m:
            return path, m.group(0)
    for path in XML_ROOT.rglob("*.ptx"):
        text = path.read_text(encoding="utf-8")
        m = pattern.search(text)
        if m:
            return path, m.group(0)
    return None


def replace_figure_images(old_fig: str, new_inner: str) -> str:
    """Keep caption; replace image/sidebyside children."""
    m = re.search(r"(<figure xml:id=\"[^\"]+\">\s*(?:<caption>[\s\S]*?</caption>\s*)?)", old_fig)
    if not m:
        raise ValueError("Could not split figure header")
    return m.group(1) + new_inner + "\n  </figure>"


def main() -> None:
    restored = []
    skipped = []
    missing = []
    for tex_path in sorted(TEX_ROOT.rglob("*.tex")):
        tex = tex_path.read_text(encoding="utf-8")
        for label, body in extract_figure_envs(tex):
            pics = extract_tikzpictures(body)
            if len(pics) < 2:
                continue
            fig_id = label.replace(":", "-")
            found = find_xml_figure(fig_id)
            if not found:
                missing.append(fig_id)
                continue
            path, old_fig = found
            captions = [panel_caption_after(body, pic) for pic in pics]
            sidebyside = body.count(r"\begin{minipage}") >= 2
            new_inner = replacement_inner(fig_id, pics, captions, sidebyside)
            new_fig = replace_figure_images(old_fig, new_inner)
            if new_fig == old_fig:
                skipped.append(fig_id)
                continue
            text = path.read_text(encoding="utf-8")
            if old_fig not in text:
                skipped.append(fig_id)
                continue
            path.write_text(text.replace(old_fig, new_fig, 1), encoding="utf-8")
            restored.append((fig_id, path.relative_to(ROOT), len(pics), sidebyside))

    print(f"Restored {len(restored)} multipanel figures:")
    for fig_id, rel, n, sbs in restored:
        layout = "sidebyside" if sbs else "stacked"
        print(f"  {fig_id}  ({n} panels, {layout})  {rel}")
    if missing:
        print("Missing XML for:")
        for x in missing:
            print(f"  {x}")
    if skipped:
        print("Unchanged:")
        for x in skipped:
            print(f"  {x}")


if __name__ == "__main__":
    main()
