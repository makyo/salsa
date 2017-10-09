import csv
import os


wow = []
for dorks in os.listdir('_data'):
    with open('_data/{}'.format(dorks)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            what = row.get('Where to find it', row.get(
                'Why you dig it (HTML and Markdown okay)'))
            if what is not None and what not in wow:
                wow.append(what)

with open('dorks.txt', 'w') as f:
    f.write('\n'.join(wow))

header = """---
layout: page
title: "Things we've called Spotify"
---

"""
with open('dorks.md', 'w') as f:
    f.write(header)
    for what in wow:
        f.write('* {}\n'.format(what))
