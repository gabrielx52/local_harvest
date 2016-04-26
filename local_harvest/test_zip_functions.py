import unittest

from zip_functions import local_city_grabber, weather_station_code_grabber


class ZipFunTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_weather_station_code_finder(self):
        self.assertEqual((weather_station_code_grabber(['OK MUSKOGEE'])[0]), 'KMKO')

    def test_local_city_set_maker(self):
        self.assertNotIn('NY MEDUSA', local_city_grabber())
        self.assertIn('NY HUDSON', local_city_grabber('12120'))

