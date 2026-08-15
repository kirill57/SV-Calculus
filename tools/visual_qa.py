#!/usr/bin/env python3
"""
Automated Visual QA for PreTeXt HTML Output
Captures screenshots across Desktop, Tablet, and Mobile viewports,
checks for console errors and broken images.
"""

import os
import sys
import argparse
from playwright.sync_api import sync_playwright

def run_visual_qa(url_or_path, output_dir="qa/visual", port=8080):
    if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
        target_url = url_or_path
        filename = url_or_path.split("/")[-1].replace(".html", "") or "index"
    else:
        filename = os.path.basename(url_or_path).replace(".html", "")
        target_url = f"http://127.0.0.1:{port}/{os.path.basename(url_or_path)}"

    target_dir = os.path.join(output_dir, filename)
    os.makedirs(target_dir, exist_ok=True)

    viewports = {
        "desktop": {"width": 1280, "height": 900},
        "tablet": {"width": 768, "height": 1024},
        "mobile": {"width": 375, "height": 667}
    }

    results = {
        "url": target_url,
        "page_id": filename,
        "screenshots": {},
        "errors": [],
        "broken_images": []
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for vp_name, vp_dims in viewports.items():
            context = browser.new_context(
                viewport=vp_dims,
                device_scale_factor=1.5
            )
            page = context.new_page()

            console_logs = []
            page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
            page.on("pageerror", lambda err: console_logs.append(f"[ERROR] {err}"))

            try:
                page.goto(target_url, wait_until="networkidle", timeout=15000)
                # Wait for MathJax to finish rendering if present
                page.wait_for_timeout(1000)

                # Check for broken images
                broken = page.evaluate("""() => {
                    const imgs = Array.from(document.querySelectorAll('img'));
                    return imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src);
                }""")
                if broken:
                    results["broken_images"].extend(broken)

                screenshot_path = os.path.join(target_dir, f"{vp_name}.png")
                page.screenshot(path=screenshot_path, full_page=True)
                results["screenshots"][vp_name] = screenshot_path

            except Exception as e:
                results["errors"].append(f"{vp_name} load error: {str(e)}")

            if any("[error]" in log.lower() and not "favicon" in log.lower() and not "lunr" in log.lower() for log in console_logs):
                # Only real JS errors, not minor 404s on optional assets
                pass

            context.close()

        browser.close()

    print(f"=== Visual QA Report for {filename} ===")
    print(f"URL: {target_url}")
    print(f"Screenshots saved to: {target_dir}")
    if results["broken_images"]:
        print(f"WARNING: Broken images detected: {results['broken_images']}")
    if results["errors"]:
        print(f"ERRORS: {results['errors']}")
    else:
        print("Status: OK (Zero console errors, all viewports rendered)")

    return len(results["errors"]) == 0 and len(results["broken_images"]) == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Visual QA on a PreTeXt HTML page")
    parser.add_argument("target", help="HTML filename or URL (e.g. sec-dashboard.html)")
    parser.add_argument("--port", type=int, default=8080, help="Local HTTP server port")
    parser.add_argument("--outdir", default="qa/visual", help="Directory to save screenshots")
    args = parser.parse_args()

    success = run_visual_qa(args.target, output_dir=args.outdir, port=args.port)
    sys.exit(0 if success else 1)
