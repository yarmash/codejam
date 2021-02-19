#!/usr/bin/env python3

"""Render README.md out of the json dump file."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    with open('dump.json') as f:
        context = json.load(f)

    templates_dir = Path(__file__).resolve().parents[1] / 'templates'

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['md']),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template('README.md.jinja')
    print(template.render(years=context))


if __name__ == '__main__':
    main()
