"""Collect current additions and language receipts without replacing audit history."""
from pathlib import Path
import datetime, hashlib, json
from lxml import etree as E

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'qa/audit'
ADD = ROOT / 'qa/additions'

def read(p):
    return json.loads(p.read_text('utf-8'))

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def passed(row):
    return row['status'] == 200 and row['mathLoaded'] and row['hintsLoaded'] and not any([
        row['mathErrors'], row['javascriptErrors'], row['brokenImages'],
        row['horizontalOverflow'], row['mobileOverflow']])

inv = read(QA/'inventory.json')
doc = E.parse(str(ROOT/'source/main.ptx'))
doc.xinclude()
ID = '{http://www.w3.org/XML/1998/namespace}id'
sections = {s.get(ID) for s in doc.iter('section')}
hints = len(list(doc.iter('hint')))
browser = read(QA/'browser-results.json')
supplement = read(QA/'browser-supplement.json')
assert not inv['errors']
assert not (ADD/'schema.log').read_text().strip()
assert not read(QA/'math-grouping.json')
assert {r['section'] for r in browser} == sections
assert len(browser) == len(sections) and all(passed(r) for r in browser)
assert sum(r['openedHints'] for r in browser) == hints
assert len(supplement) == 28 and all(passed(r) for r in supplement)
clean = read(ADD/'web-clean-validation.json')
assert not clean['changedCurrentPagesAfterCleanup']
assert not clean['remainingDuplicatedLabels']
nums = read(QA/'numerical-code-checks.json')
added = read(ADD/'mathematical-checks.json')
assert len(nums) == 40 and all(r['passed'] for r in nums)
assert len(added) == 63 and all(r['passed'] for r in added)
assert not read(QA/'inline-sphere-errors.json')
sphere = read(QA/'interactive-sphere.json')
assert sphere['webgl'] and sphere['libraryLoaded'] and not sphere['errors'] and not sphere['failedRequests']

pdf = ROOT/'output/print/main.pdf'
pdfsha = sha(pdf)
bounds = read(QA/'print-physical-boundaries.json')
visual = read(ADD/'print-visual-review.json')
assert bounds['sha256'] == pdfsha and not bounds['outsidePage']
assert visual['sha256'] == pdfsha and visual['visualReview'] == 'reviewed'
assert len(visual['renderedPages']) >= 57
assert not any(r['points'] >= 12 for r in read(QA/'print-overfull.json'))
for name in ['web-build.log', 'print-build.log']:
    assert 'Success!  Built requested target(s) without errors.' in (ADD/name).read_text(errors='replace'), name

baseline = read(QA/'baseline-inventory.json')['original_edition_sha256']
original = {str(p.relative_to(ROOT)): sha(p)
            for p in (ROOT/'Single_Variable_Calculus_Change__Accumulation__and_Approximation').rglob('*') if p.is_file()}
assert original == baseline, 'The separate original LaTeX edition changed'
files = sorted(p for p in (ROOT/'source').rglob('*') if p.suffix in {'.ptx','.xml'})
files += [ROOT/'project.ptx', ROOT/'publication/publication.ptx']
sources = {str(p.relative_to(ROOT)): sha(p) for p in files}
assert sources == read(ADD/'final-build-input.json'), 'Source changed after final builds began'
before = read(ADD/'source-before.json')
changed = [f for f,h in sources.items() if f in before and before[f] != h]
new = [f for f in sources if f not in before and f.startswith('source')]
records = [json.loads(line) for line in (ADD/'language-changes.jsonl').read_text('utf-8').splitlines()]
figures = [ROOT/'generated-assets/latex-image'/f'{name}-2.svg' for name in [
    'fig-inverse-hyperbolic-branches','fig-conditional-improper-lobes',
    'fig-contraction-cos-cobweb','fig-ode-nonunique-waiting']]
assert all(p.is_file() for p in figures)
result = {
    'completed': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'PreTeXt edition only; selected additions and subsequent language audit',
    'chapters': inv['counts']['chapter'], 'appendices': inv['counts']['appendix'],
    'mainTopicsAdded': 4, 'additionalTopicsAdded': 6,
    'sourceSha256': sources, 'changedSourceFilesSinceInitialAudit': changed,
    'newSourceFiles': new, 'languageCorrections': len(records),
    'languageFiles': len({r['file'] for r in records}),
    'schemaErrors': 0, 'inventoryErrors': 0,
    'browserSections': len(browser), 'openedHints': hints,
    'browserSupplementPages': len(supplement), 'browserProblems': 0,
    'webOutputCleaned': True, 'rebuiltTopLevelWebPages': clean['rebuiltTopLevelPages'],
    'latestRecheckedSectionPages': read(ADD/'late-browser-pages.json'),
    'renderedMathNodes': sum(r['mathCount'] for r in browser),
    'existingNumericalChecks': len(nums), 'newMathematicalAndNumericalChecks': len(added),
    'numericalFailures': 0, 'figures': inv['counts']['figure'],
    'imagePanels': inv['counts']['image'],
    'newFigureSha256': {str(p.relative_to(ROOT)): sha(p) for p in figures},
    'newFiguresVisuallyReviewed': 4,
    'pdfPages': bounds['pages'], 'pdfSha256': pdfsha, 'pdfOutOfPageSpans': 0,
    'pdfOverfullBoxesAtLeast12Points': 0,
    'visuallyReviewedPdfPages': len(visual['renderedPages']),
    'originalEditionPreserved': True, 'originalFiles': len(original),
    'originalEditionSha256': original,
    'limitations': [
        'The native Asymptote print renderer uses the verified static sphere export.',
        'The installed publication schema is older than the functioning HTML configuration.',
        'The installed PreTeXt CLI version differs from the project requirements.'
    ]
}
(ADD/'final-validation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
status = f'''# PreTeXt audit, additions, and language pass completed

Completed 5 October 2026. Scope: the PreTeXt edition, its figures, HTML, and PDF print rendering. The separate original LaTeX edition is preserved: all {len(original)} files match their starting SHA-256 hashes.

The initial complete audit covers all 17 chapters and Appendices A–F. The four selected main topics and six additional topics are implemented with explanations, proofs or derivations, examples, counterexamples, exercises, and hints. Their locations are in [SELECTED-TOPICS-REPORT.md](SELECTED-TOPICS-REPORT.md).

The subsequent language pass reviewed all chapter and section openings, appendix introductions, frontmatter, and flagged prose throughout the book. It records {len(records)} corrections across {result['languageFiles']} source files. [LANGUAGE-AUDIT.md](LANGUAGE-AUDIT.md) explains the flags and links to every before-and-after replacement.

Final verification passed: manuscript schema, XML assembly, IDs and references, math grouping, all {len(browser)} section pages and {len(supplement)} supplemental pages in desktop/mobile browsers, and all {hints} opened hints. The {len(nums)} existing numerical/code checks and {len(added)} new mathematical/numerical checks pass. The interactive and embedded sphere render correctly. Four new vector figures were inspected visually.

The final {bounds['pages']:,}-page PDF has no text outside physical page boundaries and no overfull boxes of 12 points or more. Every page of the new material and all chapter and appendix openings were rendered; {len(visual['renderedPages'])} selected pages were inspected visually.

Current source and PDF hashes and verification results are in [additions/final-validation.json](additions/final-validation.json). The initial audit receipt in `audit/final-validation.json` is retained as history. [PRETEXT-AUDIT-REPORT.md](PRETEXT-AUDIT-REPORT.md) records the initial corrections and local toolchain limitations.

[MISSING-TOPICS.md](MISSING-TOPICS.md) records the ten implemented topics and four remaining proposals awaiting a later decision.
'''
(ROOT/'qa/AUDIT-STATUS.md').write_text(status, encoding='utf-8')
report = ROOT/'qa/SELECTED-TOPICS-REPORT.md'
content = report.read_text('utf-8')
marker = 'Final build and verification receipts are recorded in `qa/additions/final-validation.json`.'
verified = (f'The final builds pass: {len(browser)} section pages, {len(supplement)} supplemental pages, '
            f'{hints} opened hints, and {len(nums)+len(added)} mathematical/numerical checks, with no failures. '
            f'The {bounds["pages"]:,}-page PDF has no text outside the physical page and no overfull boxes '
            f'of 12 points or more. All new material and chapter/appendix openings were inspected in '
            f'{len(visual["renderedPages"])} rendered pages. '
            'Final build and verification receipts are recorded in `qa/additions/final-validation.json`.')
if marker in content:
    report.write_text(content.replace(marker, verified), encoding='utf-8')
summary = {k:v for k,v in result.items() if k not in {
    'sourceSha256','changedSourceFilesSinceInitialAudit','newSourceFiles',
    'latestRecheckedSectionPages','newFigureSha256','originalEditionSha256'}}
print(json.dumps(summary, indent=2))
