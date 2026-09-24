"""Rebuild current quantitative figures from frozen scientific summaries."""
from pathlib import Path
import subprocess,sys,shutil
ROOT=Path(__file__).resolve().parent.parent
(ROOT/'figures').mkdir(exist_ok=True)
subprocess.run([sys.executable,str(ROOT/'revision7/figures.py')],check=True,cwd=ROOT)
for n in range(4,8):
    for ext in ['pdf','eps','png']:
        source=ROOT/'revision7/figures'/f'Fig{n}.{ext}'
        if source.exists():shutil.copy2(source,ROOT/'figures'/source.name)
subprocess.run([sys.executable,str(ROOT/'visualization/replot_summary_bars.py')],check=True,cwd=ROOT)
print('Quantitative Figures 2-7 rebuilt from frozen records into figures/.')
