#!/usr/bin/env python3

"""Render README files out of the json dump file."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    with open('dump.json') as f:
        years = json.load(f)

    templates_dir = Path(__file__).resolve().parents[1] / 'templates'

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['md']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    generate_root_readme(env, years)
    generate_year_readmes(env, years)


def generate_root_readme(env, years):
    template = env.get_template('README-root.md.jinja')

    with open('README.md', 'w') as f:
        print(template.render(years=years), file=f)


def generate_year_readmes(env, years):
    template = env.get_template('README-year.md.jinja')

    for year in years:
        if Path(year['name']).is_dir():
            with open(f'{year["name"]}/README.md', 'w') as f:
                print(template.render(year=year), file=f)


if __name__ == '__main__':
    main()
