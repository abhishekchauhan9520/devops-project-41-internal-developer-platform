#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / 'backstage' / 'templates'

def validate_catalog():
    catalog = ROOT / 'backstage' / 'catalog.yaml'
    text = catalog.read_text()
    required = ['kind: System', 'kind: Component', 'kind: API', 'kind: Resource']
    missing = [x for x in required if x not in text]
    if missing:
        raise SystemExit(f'missing catalog entities: {missing}')
    print('catalog validation: PASS')

def validate_templates():
    required = ['template.yaml']
    found = []
    for d in sorted(TEMPLATES.iterdir()):
        if d.is_dir():
            for name in required:
                p = d / name
                if not p.exists():
                    raise SystemExit(f'missing {p}')
                text = p.read_text()
                if 'fetch:template' not in text or 'publish:github' not in text:
                    raise SystemExit(f'incomplete template: {p}')
            found.append(d.name)
    if len(found) < 3:
        raise SystemExit('expected at least three golden-path templates')
    print(f'template validation: PASS ({", ".join(found)})')

def render(template, name, owner):
    src = TEMPLATES / template / 'skeleton'
    if not src.exists():
        raise SystemExit(f'skeleton not found: {src}')
    if not re.fullmatch(r'[a-z0-9-]+', name):
        raise SystemExit('name must match [a-z0-9-]+')
    out = ROOT / '.generated' / name
    if out.exists():
        raise SystemExit(f'already exists: {out}')
    for p in src.rglob('*'):
        if p.is_file():
            rel = p.relative_to(src)
            data = p.read_text()
            data = data.replace('${{ values.component_id }}', name)
            data = data.replace('${{ values.description }}', f'Generated {template} service')
            data = data.replace('${{ values.owner }}', owner)
            data = data.replace('${{ values.lifecycle }}', 'experimental')
            target = out / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(data)
    print(f'rendered: {out}')

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command', required=True)
sub.add_parser('validate-catalog')
sub.add_parser('validate-templates')
r = sub.add_parser('render')
r.add_argument('--template', required=True, choices=['python-api','node-api','static-web'])
r.add_argument('--name', required=True)
r.add_argument('--owner', required=True)
args = parser.parse_args()

if args.command == 'validate-catalog':
    validate_catalog()
elif args.command == 'validate-templates':
    validate_templates()
else:
    render(args.template, args.name, args.owner)
