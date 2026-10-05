"""Small exact-match edits with a durable explanation of each correction."""
from pathlib import Path
import json
import re
import os
import time

ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / 'qa/audit/editorial-changes.jsonl'

def save(path, data):
    """Use atomic replacement to avoid transient Windows reader locks."""
    path=path.resolve()
    if not path.is_relative_to(ROOT): raise ValueError(path)
    pending=path.with_name(path.name+'.audit-tmp')
    for attempt in range(5):
        try:
            pending.write_bytes(data if isinstance(data,bytes) else data.encode('utf-8'))
            os.replace(pending,path)
            return
        except OSError:
            if attempt==4: raise
            time.sleep(0.2)


def record(path, issue, before, after):
    with JOURNAL.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps({'file':str(path.relative_to(ROOT)), 'issue':issue,
                                 'before':before, 'after':after}, ensure_ascii=False)+'\n')


def replace(pattern, before, after, issue):
    paths = list((ROOT/'source').glob(pattern))
    if len(paths) != 1:
        raise ValueError((pattern, len(paths)))
    path = paths[0]
    text = path.read_text('utf-8')
    if text.count(before) == 0:
        # Readable excerpts collapse whitespace; preserve the exact source
        # match in the receipt when that is the only difference.
        matches=list(re.finditer(r'\s+'.join(re.escape(s) for s in before.split()),text))
        if len(matches)==1:
            before=matches[0].group()
        elif text.count(after)==1:
            return
    if text.count(before) != 1:
        raise ValueError((pattern, issue, text.count(before)))
    save(path,text.replace(before,after))
    record(path, issue, before, after)
