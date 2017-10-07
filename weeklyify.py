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
