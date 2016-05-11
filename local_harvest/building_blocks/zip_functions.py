import zipcode
import re
import requests
import pprint
import logging


def local_city_grabber(starting_zip='98119', mile_radius=100):
    """returns set of cities within radius of starting zip"""
    zip_obj = zipcode.isequal(starting_zip)
    local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
    return {'{} {}'.format(i.state, i.city) for i in local_zips}


def weather_station_code_grabber(cities=local_city_grabber()):
    """returns list of weather station ICAO codes
    city_list: list of states and cities * needs to be in 'ST CITY' format
               use return from local_city_list_maker()
    """
    city_codes = []
    with open('weather_codes.txt', 'r') as text:
        code_db = text.read()
    for city in cities:
        city_info = re.search(city + '.*[PKXQ]\w{3}\s\s', code_db)
        try:
            code = re.search('\s[PKXQ]\w{3}\s\s', city_info.group())
            city_codes.append((code.group()).strip())
        except:
            pass
    return city_codes

def weather_report_grabber(city_codes=weather_station_code_grabber())
# #starting to get weather data. need to make mock produce data for cross reference

# for i in codes:
#     #print(i)
#     r = requests.get('https://www.wunderground.com/history/airport/{}/2016/4/0/MonthlyHistory.html?format=1'.format(i))
#     print(r.text)
# #
# # r = requests.get('https://www.wunderground.com/history/airport/{}/2016/4/0/MonthlyHistory.html?format=1'.format('KSEA'))
# # print(r.text)



pprint.pprint(local_city_grabber('06424'))
pprint.pprint(weather_station_code_grabber())