import csv
import requests
import re


def zone_getter():
    root_site = 'https://shop.arborday.org/LookUp.aspx?zipcode='
    zip_db = csv.reader(open('zipcodes.csv', 'r'))

    ## ** Creates Header **
    ## with open('zonedata.csv', 'a') as outfile:
    ##     zone_writer = csv.writer(outfile)
    ##     zone_writer.writerow(['Zipcode', 'State', 'City', 'Grow zone'])

    ## Finds last zip added
    # with open('zonedata.csv') as file:
    #     last_line = file.readlines()
    #     last_zip = last_line[-1][:5]
    # print(last_zip)

    for row in zip_db:
        req_obj = requests.get(root_site + '{}'.format(row[0]))
        zone = (re.search('\s\d\-*\d*', re.search('Zones?\s\d+\-*\d*', req_obj.text).group())).group().strip()

        with open('zonedata.csv', 'a') as outfile:
            zone_writer = csv.writer(outfile)
            zone_writer.writerow([row[0], row[2], row[1], zone])


def zone_code_compiler():
    """ Writes new csv file with Airport Code to cities if applicable
        ** csv does not append so new file is necessary ** """
    zone_db = csv.reader(open('zonedata.csv', 'r'))
    with open('weather_codes.txt') as file_obj:
        code_db = file_obj.read()
    for row in zone_db:
        line_match = re.search(row[1] + ' ' + row[2] +'.*[PKXQ]\w{3}\s\s', code_db)
        with open('alldata.csv', 'a') as outfile:
            data_writer = csv.writer(outfile)
            try:
                code = re.search('\s[PKXQ]\w{3}\s\s', line_match.group())
                data_writer.writerow([row[0], row[2], row[1], row[3], code.group().strip()])
            except:
                data_writer.writerow([row[0], row[2], row[1], row[3]])


print(zone_code_compiler())