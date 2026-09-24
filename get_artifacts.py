"""Install only the versioned, checksum-verified numerical experiment records."""
from pathlib import Path
import argparse,hashlib,json,re,urllib.request,zipfile
ROOT=Path(__file__).resolve().parent
PREFIXES=('revision/results/predictions/','revision5/results/predictions/','revision6/results/predictions/','confirmation_hhar/results/predictions/','revision6/evaluation/','confirmation_hhar/evaluation/','revision6/schema_sensitivity/','revision6/summaries/','confirmation_hhar/summaries/')
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  while chunk:=f.read(1024*1024):h.update(chunk)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--archive',type=Path);args=ap.parse_args()
 spec=json.loads((ROOT/'artifacts.json').read_text());archive=args.archive
 if archive is None:
  assert re.fullmatch(r'[A-Za-z0-9._-]+',spec['version'])
  cache=ROOT/'downloads';cache.mkdir(exist_ok=True);archive=cache/(spec['version']+'.zip')
  if not archive.exists():
   partial=archive.with_suffix('.part')
   request=urllib.request.Request(spec['url'],headers={'User-Agent':'JRC-reproduction'})
   with urllib.request.urlopen(request,timeout=60) as response,partial.open('wb') as f:
    while chunk:=response.read(1024*1024):f.write(chunk)
   if partial.stat().st_size!=spec['bytes'] or digest(partial)!=spec['sha256']:raise RuntimeError('Downloaded artifact checksum mismatch')
   partial.replace(archive)
 if archive.stat().st_size!=spec['bytes'] or digest(archive)!=spec['sha256']:raise RuntimeError('Artifact checksum does not match artifacts.json')
 with zipfile.ZipFile(archive) as z:
  rows=json.loads(z.read('MANIFEST.json'));names=z.namelist()
  assert len(names)==len(set(names)) and len(rows)==len({r['path'] for r in rows})
  assert set(names)=={'MANIFEST.json'}|{r['path'] for r in rows}
  for row in rows:
   name=row['path'];dest=(ROOT/name).resolve()
   assert dest.is_relative_to(ROOT) and name.startswith(PREFIXES),name
   assert dest.suffix in {'.npz','.json','.csv','.gz'},name
   data=z.read(name)
   assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],name
   if dest.exists() and digest(dest)!=row['sha256']:raise RuntimeError('Existing numerical file differs; use a clean checkout: '+name)
  for row in rows:
   dest=ROOT/row['path']
   if not dest.exists():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(row['path']))
 print('Verified and installed',len(rows),'numerical files. Run python reproduce.py --smoke.')
if __name__=='__main__':main()
