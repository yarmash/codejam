#!/usr/bin/env python3

"""Render README files out of the json dump file."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    with open('dump.json') as f:
        years = [year for year in json.load(f) if Path(year['name']).is_dir()]

    templates_dir = Path(__file__).resolve().parents[1] / 'templates'

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['md']),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    generate_root_readme(env, years)
    generate_year_readmes(env, years)


def generate_root_readme(env, years):
    template = env.get_template('README-root.md.jinja')

    with open('README.md', 'w') as f:
        f.write(template.render(years=years))


def generate_year_readmes(env, years):
    template = env.get_template('README-year.md.jinja')

    for year in years:
        with open(f'{year["name"]}/README.md', 'w') as f:
            f.write(template.render(year=year))


if __name__ == '__main__':
    main()
