import csv
import os
import yaml


weeklies = {}
for weekly in os.listdir("_data"):
    if weekly[-3:] != 'csv':
        continue
    with open("_data/{}".format(weekly), 'r') as f:
        r = csv.DictReader(f)
        for row in r:
            n = row['Name'].strip()
            if n not in weeklies:
                weeklies[n] = []
            weeklies[n].append(row['Artist - Song Title'])

with open('_data/weeklyify.yml', 'w') as f:
    f.write(yaml.safe_dump(weeklies))


## NEEEERRRRRRRDS

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
