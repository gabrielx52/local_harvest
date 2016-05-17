# used to convert json file to json fixture for django location model

import json

json_list = []
pk = 1

with open('alldata.json') as f:
    infile = json.load(f)
    for i in infile:
        try:
            json_item = {"model": "seasonal.location",
                         "pk": pk,
                         "fields": {
                             "zipcode": i['zipcode'],
                             "city": i['city'],
                             "state": i['state'],
                             "grow_zone": i['grow_zone'],
                             "airport_zone": i['airport_zone']}}
        except KeyError:
            json_item = {"model": "seasonal.location",
                         "pk": pk,
                         "fields": {
                             "zipcode": i['zipcode'],
                             "city": i['city'],
                             "state": i['state'],
                             "grow_zone": i['grow_zone'],
                             "airport_zone": None}}
        json_list.append(json_item)
        pk += 1
    with open('Location.json', 'w') as of:
        json.dump(json_list, of)
