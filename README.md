# sdk_test

## Requirements
Python 3.11 or higher
`requests` library

## Description
A command-line utility to fetch geographical coordinates and place information based on city/state or zip codes using the OpenWeather Geocoding API.

## Setup
1.Clone the Repository:
`git clone https://github.com/inthedepthsofitall/sdk_test.git`
`cd sdk_test`

2.Create and Activate a Virtual Environment
`python -m venv .venv`
`source .venv/bin/activate`


## Create a requirements.txt file
3.ensure it has the necessary dependencies which is the instance is requirements
after run the following command:
`pip install -r requirements.txt`

## Geolocation Utility

## Description
A command-line utility to fetch geographical coordinates and place information based on city/state or zip codes using the OpenWeather Geocoding API.


## Usage

`geoloc_util.py`: Contains the utility script for fetching geolocation data.
`test_geoloc_util.py`: Contains the test cases for validating the functionality of the utility script.
`requirements.txt`: Lists the dependencies required to run the utility.

To run use this command and adjust accordingly: python geoloc_util.py <location> [<location> ...](can be run through env or machine)
ex: 
`python geoloc_util.py "Madison, WI"`

for multiple locations it should look as follows:
`python geoloc_util.py "Madison, WI" "12345" "Chicago, IL" "10001"`


to run all test casses:
`python -m unittest test_geoloc_util.py`

## Links to resource for code documentation:
https://docs.python.org/3/library/argparse.html
https://docs.python.org/3/library/unittest.html

## License
Licensed under the MIT License.

