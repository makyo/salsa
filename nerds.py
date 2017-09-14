import csv
import os


wow = []
for dorks in os.listdir('_data'):
    with open('_data/{}'.format(dorks)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            wow.append(row['Where to find it'])

print('\n'.join(wow))
