import zipcode
import pprint
import csv
import re


def local_zipcodes(startingzip='98119', radius=100):
    """ Returns zipcodes within radius of startingzip"""
    zip_obj = zipcode.isequal(startingzip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
    return {i.zip for i in local_zips}


def local_info(zipcodes=local_zipcodes()):
    """ Returns city, tate, grow zone and airport code (if applicable) of zipcode(s) """
    with open('data_files/alldata.csv', 'r') as f:
        reader = csv.reader(f)
        return [row for row in reader if row[0] in zipcodes]


def veg_db_template(file='data_files/veg_list.txt'):
    """ Use to create persistent dict of vegetables with
        parameters from text file of vegetables """
    plant_dict = {}
    with open(file) as f:
        vegs = f.read()
        listv = vegs.split('\n')
    for i in listv:
        plant_dict[i] = {'Lower Max': None, 'Upper Max': None, 'Base Temp': None, 'Grow Zone': None,
                         'Optimum range': None, 'Season': None, 'Grow Time': None}
    with open('data_files/veg_data.txt', 'w') as outfile:
        outfile.write(str(plant_dict))
    return plant_dict


def veg_param_editor(veggies='data/veg_data.txt'):
    with open(veggies, 'r+') as infile:
        veg = eval(infile.read())
        for row in veg:
            print(row, veg[row])


veg_param_editor()