import requests
import argparse

def get_location_info(api_key, location):
    if ',' in location:
        # City and state combination
        city, state = location.split(', ')
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={api_key}'
    elif location.isdigit() and len(location) == 5:
        # Zip code
        url = f'http://api.openweathermap.org/geo/1.0/zip?zip={location},US&appid={api_key}'
    else:
        print(f'Invalid location format: {location}')
        return None

    response = requests.get(url)
    print(f'Response status code: {response.status_code}') 
    if response.status_code == 200:
        data = response.json()
        if data:
            if isinstance(data, dict):  # Zip code returns a single dictionary
                return {
                    'latitude': data.get('lat'),
                    'longitude': data.get('lon'),
                    'place_name': data.get('name'),
                    'state': data.get('state'),
                    'country': data.get('country')
                }
            elif isinstance(data, list) and data:
                # City and state endpoint returns a list of dictionaries
                data = data[0]
                return {
                    'latitude': data.get('lat'),
                    'longitude': data.get('lon'),
                    'place_name': data.get('name'),
                    'state': data.get('state'),
                    'country': data.get('country')
                }
        else:
            print(f'No data found for location: {location}')
            return None
    else:
        print(f'Failed to retrieve data for location: {location}. Status code: {response.status_code}')
        return None

def main():
    parser = argparse.ArgumentParser(description='Geolocation utility')
    parser.add_argument('locations', nargs='+', help='List of locations (city, state or zip code)')
    args = parser.parse_args()

    api_key = 'f897a99d971b5eef57be6fafa0d83239'
    for location in args.locations:
        location_info = get_location_info(api_key, location.strip())
        if location_info:
            print(f'Location: {location}')
            print(f'Latitude: {location_info["latitude"]}')
            print(f'Longitude: {location_info["longitude"]}')
            print(f'Place Name: {location_info["place_name"]}')
            print(f'State: {location_info["state"]}')
            print(f'Country: {location_info["country"]}')
            print('------------------------')

if __name__ == '__main__':
    main()
