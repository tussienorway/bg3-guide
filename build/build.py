#!/usr/bin/env python3
"""Bygger index.html og bg3-nybegynnerguide.html fra content.py + template.html."""
import base64, json, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import DATA, DU
ROOT = os.path.dirname(HERE)
tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
data_js = json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/')
du_b64 = base64.b64encode(json.dumps(DU, ensure_ascii=False).encode('utf-8')).decode('ascii')
out = tpl.replace('__DATA__', data_js).replace('__DU_B64__', du_b64)
assert '__DATA__' not in out and '__DU_B64__' not in out
p = os.path.join(ROOT, 'index.html')
open(p, 'w', encoding='utf-8').write(out)
shutil.copyfile(p, os.path.join(ROOT, 'bg3-nybegynnerguide.html'))
print('skrev', p, len(out.encode('utf-8')), 'byte')
