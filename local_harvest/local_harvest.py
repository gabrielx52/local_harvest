import zipcode
import pprint
import csv
import re


def local_zipcodes(startingzip='98119', radius=10):
    """ Returns zipcodes within radius of startingzip"""
    zip_obj = zipcode.isequal(startingzip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
    return {i.zip for i in local_zips}


def local_info(startingzip, radius):
    """ Returns zipcode data """
    zipcodes = local_zipcodes(startingzip, radius)
    with open('data/alldata.csv') as f:
        reader = csv.reader(f)
        return [row for row in reader if row[0] in zipcodes]


def veg_parser(*args):
    """ veg data parser"""
    with open('data/short_veg_data.txt') as infile:
        vegs = eval(infile.read())
    #for arg in args:
    #    if arg in vegs:
    parsed_veg = [arg for arg in args if arg in vegs]
    print(parsed_veg)
            #x, y = vegs[arg]['Grow Zone'].split('-')
            #print(arg, 'grow zones: ', list(range(int(x), int(y) + 1)))


def veg_db_template(file='data/veg_list.txt'):
    """ Use to create persistent dict of vegetables with
        parameters from text file of vegetables """
    plant_dict = {}
    with open(file) as f:
        vegs = f.read()
        listv = vegs.split('\n')
    for i in listv:
        plant_dict[i] = {'Lower Max': None, 'Upper Max': None,
                         'Grow Zone': None, 'Season': None,
                         'Grow Time': None, 'Sun': None}
    with open('data/short_veg_data.txt', 'w') as outfile:
        outfile.write(str(plant_dict))
    return plant_dict


def local_harvest(startingzip='98119', radius=10, *args):
    """ Returns produce in *args thats in zip's grow zone"""
    zip_obj = zipcode.isequal(startingzip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
    # list of all zipcodes in radius from starting zip
    zips_in_radius = [i.zip for i in local_zips]
    with open('data/alldata.csv') as f:
        reader = csv.reader(f)
        # list of local zip with data, csv format
        local_list = [row for row in reader if row[0] in zips_in_radius]
    zip_zone_lister = []
    for row in local_list:
        if len(row[3]) > 1:
            x, y = row[3].split('-')
            # list of grow zone range values
            zip_gz_range = list(range(int(x), int(y) + 1))
            zip_zone_lister.append((row[0], zip_gz_range))
            # print('zip =', row[0], zip_gz_range)
    print('***********', zip_zone_lister)
    with open('data/short_veg_data.txt') as infile:
        vegs = eval(infile.read())
    '''this will print out the arg-veg's grow zone info'''
    veg_zone_lister = []
    for i in args:
        if [i in x for x in vegs]:
            veg_gz = vegs[i]['Grow Zone']
            if len(veg_gz) > 1:
                x, y = veg_gz.split('-')
                gz_range = list((range(int(x), int(y))))
                veg_zone_lister.append((i, gz_range))
                print(i, gz_range)  # veg from *args (i) and its gz range
    print(veg_zone_lister[0][1])  # location of grow zones for veg


#local_harvest('98119', 10, 'Beet', 'Cabbage')

veg_parser('Beet', 'Cabbage')

