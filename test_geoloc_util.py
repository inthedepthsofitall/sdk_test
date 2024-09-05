import unittest
from unittest.mock import patch
import requests
from geoloc_util import fetch_coordinates

class TestFetchCoordinates(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_coordinates_city(self, mock_get):
        mock_response = {
            'lat': 40.7128,
            'lon': -74.0060,
            'name': 'New York',
            'state': 'NY'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [mock_response]

        result = fetch_coordinates("New York, NY")
        self.assertEqual(result['latitude'], 40.7128)
        self.assertEqual(result['longitude'], -74.0060)
        self.assertEqual(result['place_name'], 'New York')
        self.assertEqual(result['state'], 'NY')

    @patch('requests.get')
    def test_fetch_coordinates_zip(self, mock_get):
        mock_response = {
            'lat': 90210,
            'lon': -118.4065,
            'name': 'Beverly Hills',
            'state': 'CA'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [mock_response]

        result = fetch_coordinates("90210")
        self.assertEqual(result['latitude'], 90210)
        self.assertEqual(result['longitude'], -118.4065)
        self.assertEqual(result['place_name'], 'Beverly Hills')
        self.assertEqual(result['state'], 'CA')

    @patch('requests.get')
    def test_fetch_coordinates_no_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        result = fetch_coordinates("InvalidLocation")
        self.assertIsNone(result)

    @patch('requests.get')
    def test_fetch_coordinates_request_exception(self, mock_get):
        mock_get.side_effect = requests.RequestException

        with self.assertRaises(requests.RequestException):
            fetch_coordinates("New York, NY")

if __name__ == '__main__':
    unittest.main()
