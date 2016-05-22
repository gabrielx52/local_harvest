import zipcode
from .models import Produce


def local_zipcodes(startingzip='98119', radius=10):
    """ Returns zipcodes within radius of startingzip """
    zip_obj = zipcode.isequal(startingzip)
    try:
        local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
        return [i.zip for i in local_zips]
    except AttributeError:
        return 'No surrounding data available for ' + startingzip


def grow_zone_stripper(grow_zone):
    """ Strips brackets off grow zones """
    if ',' in grow_zone:
        grow_zone = grow_zone[1:-1]
        return grow_zone
    else:
        return grow_zone


def grow_zone_matcher(grow_zone):
    """ Returns produce in grow_zone(s) """
    produce = set()
    if len(grow_zone) > 1:
        grow_zone = grow_zone.replace(',', '')
        for i in grow_zone:
            produce.update([f.name for f in Produce.objects.filter(grow_zone__contains=i)])
    return produce
