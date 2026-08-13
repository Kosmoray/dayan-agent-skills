#!/usr/bin/env python3
"""Verify the public discovery site and flagship demos."""
from __future__ import annotations
import re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FILES=[ROOT/'docs/index.html',ROOT/'docs/product-tour.html',ROOT/'docs/demos/control-library.html',ROOT/'docs/demos/wenzhen.html',ROOT/'docs/demos/deck.html',ROOT/'docs/demos/reviewer.html']
def verify():
    errors=[]
    for path in FILES:
        if not path.is_file(): errors.append(f'missing {path.relative_to(ROOT)}');continue
        text=path.read_text(encoding='utf-8')
        for token in ('<title>','<meta name="viewport"','<main','prefers-reduced-motion'):
            if token not in text: errors.append(f'{path.relative_to(ROOT)} missing {token}')
        if re.search(r'(?:/Users|/home)/|/Desktop/|API_KEY|PRIVATE KEY',text,re.I): errors.append(f'{path.relative_to(ROOT)} contains public redline')
        for target in re.findall(r'(?:href|src)="([^"]+)"',text):
            if target.startswith(('http://','https://','#','mailto:')): continue
            local=(path.parent/target.split('#',1)[0]).resolve()
            if target and not local.exists(): errors.append(f'{path.relative_to(ROOT)} broken link {target}')
    index=FILES[0].read_text(encoding='utf-8')
    for claim in ('56 Skills','112','Take the product tour','Run one route'):
        if claim not in index: errors.append(f'landing page missing claim {claim}')
    return errors
if __name__=='__main__':
    problems=verify()
    if problems:
        print('\n'.join('ERROR: '+x for x in problems));sys.exit(1)
    print('PASS: discovery site and four flagship demos satisfy the public contract')
