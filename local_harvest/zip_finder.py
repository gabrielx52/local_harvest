import zipcode
import re

my_zip = zipcode.isequal('98119')
local_zips = zipcode.isinradius((my_zip.lat, my_zip.lon), 100)



zip_dict = {}

## good code!!!
for i in local_zips:
    state_city = i.state + ' ' + i.city
    if state_city not in zip_dict:
        zip_dict[state_city] = [i.zip]
    zip_dict[state_city].append(i.zip)
## good code!!!




print(zip_dict)

code_db = open('weather_codes.txt', 'r').read()

for i in zip_dict:
    #m = re.search('{}.+'.format(i), code_db)
    m = re.search(i + '.*[PKXQ]\w{3}\s\s', code_db)
    #cm = re.search('^[PKXQ]{4}', m.group)
    # m = re.findall(i +'\s^[PKXQ]{4}', code_db)
    try:
        print(m.group())
        cm = re.search('\s[PKXQ]\w{3}\s\s', m.group())
        print(cm.group())
    # print(m.groups())
    except:
        pass

    import zipcode
    import re


    def local_city_list_maker(starting_zip='98119', mile_radius=100):
        """returns a set of cities within radius of starting zip,
        formatted with state space city to use in weather_station_code_finder function"""
        zip_obj = zipcode.isequal(starting_zip)
        local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), mile_radius)
        return {' '.join([i.state, i.city]) for i in local_zips}


    def weather_station_code_finder(city_list):
        """returns list of weather station ICAO codes
        city_list: list of states and cities * needs to be in 'ST CITY' format
                   use return from local_city_list_maker()
        """
        city_code_list = []
        with open('weather_codes.txt', 'r') as text:
            code_db = text.read()

        for city in city_list:
            city_info = re.search(city + '.*[PKXQ]\w{3}\s\s', code_db)
            if city_info is not None:
                code = re.search('\s[PKXQ]\w{3}\s\s', city_info.group())
                city_code_list.append((city, code.group()))
            else:
                print('Sorry {} does not exist'.format(city))

        return city_code_list

        # print((weather_station_code_finder(['OK MUSKOGEE'])[0][1]).strip())