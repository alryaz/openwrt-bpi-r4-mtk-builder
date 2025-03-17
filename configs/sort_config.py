#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print(sys.argv[0], "<file>")
    exit()

config_file = sys.argv[1]
new_config = ""
current_section_title = None
sections = {}

with open(config_file, "r", encoding="utf-8") as fp:
    for line in map(str.strip, fp):
        if line.startswith('##'):
            current_section_title = line
        elif line and current_section_title:
            sections.setdefault(current_section_title, []).append(line)

with open(config_file, "w", encoding="utf-8") as fp:
    for section_title in sorted(sections, key=str.casefold):
        print(section_title, file=fp)
        for line in sorted(sections[section_title]):
            print(line, file=fp)
        print(file=fp)

