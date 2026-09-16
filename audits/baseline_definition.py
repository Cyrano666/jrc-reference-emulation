from pathlib import Path
import csv,json,math,collections
from scipy.stats import hypergeom
W=Path(__file__).resolve().parent;P=W.parent
rows=list(csv.DictReader((P/'revision6/summaries/campaign_cells.csv').open()))
groups=collections.defaultdict(list)
for r in rows:
 if r['score']=='LAC' and float(r['tolerance'])==.5:
  groups[(r['dataset'],r['policy'])].append(float(r['actual_inflation']))
means={f'{d}:{p}':sum(v)/len(v) for (d,p),v in groups.items()}
rank=[]
for N in [120,240,480,960]:
 k=math.ceil((N+1)*.9-1e-12);t=N//2
 rank.append(dict(N=N,t=t,k=k,upper_025=int(hypergeom.ppf(.975,N,k-1,t))+1,upper_05=int(hypergeom.ppf(.95,N,k-1,t))+1))
(W/'audit.json').write_text(json.dumps(dict(window_inflation=means,rank_comparison=rank),indent=2))
print(json.dumps(dict(uschad={k:v for k,v in means.items() if k.startswith('uschad:')},ranks=rank)))
