"""Create chapter-organized review sheets from actual browser captures."""
from pathlib import Path
import argparse, json, math, re
from PIL import Image, ImageDraw, ImageFont
from lxml import etree as E

ROOT=Path(__file__).resolve().parents[1]
QA=ROOT/'qa/audit-2026-10-17'
ID='{http://www.w3.org/XML/1998/namespace}id'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('run')
    ap.add_argument('--kind',choices=['figure','table','array','opening'],default='figure')
    ap.add_argument('--group',choices=['early','middle','late','front','all'],default='all')
    args=ap.parse_args()
    run=QA/args.run
    if (run/'results.json').exists():
        rows=json.loads((run/'results.json').read_text('utf-8'))
    else:
        rows=[]
        for p in sorted(run.glob('worker-*.json')):
            try:rows.extend(json.loads(p.read_text('utf-8')))
            except json.JSONDecodeError:pass
    tree=E.parse(str(ROOT/'source/main.ptx')); tree.xinclude()
    groups={}
    order={}
    for i,division in enumerate(tree.xpath('//chapter|//appendix')):
        d=division.get(ID)
        if d.startswith('ch'):
            n=int(d[2:4]); group='early' if n<=6 else 'middle' if n<=12 else 'late'
        else:
            letter=d[3];group='early' if letter in 'ABC' else 'middle' if letter=='F' else 'late'
        for el in [division]+division.findall('section'):
            groups[el.get(ID)]=group
            order[el.get(ID)]=len(order)
        for row in rows:
            if row['page'].startswith(d+'-') and row['page'] not in groups:
                groups[row['page']]=group
                order[row['page']]=order[d]+0.1
    captures=[]
    for row in sorted(rows,key=lambda r:order.get(r['page'],10000)):
        if args.group=='front' and row['page'] in groups:continue
        if args.group not in {'all','front'} and groups.get(row['page'])!=args.group:continue
        if args.kind=='opening':
            path=run/'screenshots'/row['page']/'opening-desktop.png'
            if path.exists():captures.append({'id':row['page'],'file':str(path.relative_to(ROOT)),'page':row['page']})
        else:
            for capture in row.get('captures',[]):
                if capture['kind']==args.kind:
                    captures.append({**capture,'page':row['page']})
    out=run/'contacts'/args.group/args.kind
    out.mkdir(parents=True,exist_ok=True)
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
    manifest=[]
    # Twelve screenshots per sheet, with full-size originals kept for details.
    for start in range(0,len(captures),12):
        sheet=Image.new('RGB',(2400,2100),'#e5e5e5')
        draw=ImageDraw.Draw(sheet)
        batch=captures[start:start+12]
        for j,row in enumerate(batch):
            tile=Image.open(ROOT/row['file']).convert('RGB')
            if args.kind=='opening':
                # Exclude the desktop sidebar; preserve the main heading/text.
                tile=tile.crop((max(0,int(tile.width*.21)),0,tile.width,tile.height))
            tile.thumbnail((584,610))
            x=(j%4)*600+(600-tile.width)//2; y=(j//4)*700+18
            sheet.paste(tile,(x,y))
            label=row['id']
            for k,line in enumerate(re.findall('.{1,62}',label)[:3]):
                draw.text(((j%4)*600+8,(j//4)*700+632+20*k),line,fill='black',font=font)
            manifest.append({**row,'sheet':f'{start//12+1:02}.png','tile':j+1})
        sheet.save(out/f'{start//12+1:02}.png')
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(args.run,args.group,args.kind,'captures',len(captures),'sheets',math.ceil(len(captures)/12))

if __name__=='__main__':main()
