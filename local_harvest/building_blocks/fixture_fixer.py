#  changes #-# format of grow zone to list of values

import json


with open('Location.json') as infile, open('RangeLocation.json', 'w') as outfile:
    json_data = json.load(infile)
    for row in json_data:
        if '-' in row['fields']['grow_zone']:
            x, y = row['fields']['grow_zone'].split('-')
            row['fields']['grow_zone'] = list(range(int(x), int(y) + 1))
        else:
            row = row
    outfile.write(json.dumps(json_data))
