# Address Geocoding with Google Maps API

This script is used to process a CSV file containing addresses, extract detailed address components using the Google Maps Geocoding API, and save the enriched data to a new CSV file.

# Features

Reads a CSV file with address data.

Uses the Google Maps Geocoding API to retrieve address components.

Extracts and organizes address details such as:

Street Number

Route

Locality

Administrative Area Levels (State, City)

Country

Postal Code

Writes the processed data back to a new CSV file.

# Requirements

Python 3.x

googlemaps library

pandas library

# Setup

Install the required Python libraries:

pip install googlemaps pandas

Replace google_key in the code with your Google Maps API key.

Ensure your input CSV file is formatted correctly and contains a column named mailing_address_display with address data to be geocoded.

Update the file paths in the code:

Input file: /Users/surajnavkudkar/Desktop/fraddress.csv

Output file: /Users/surajnavkudkar/Desktop/frdatanew.csv

# Usage

Place the input CSV file (fraddress.csv) in the specified directory.

Run the script.

The output file (frdatanew.csv) will be generated with additional columns:

address_line_1

address_line_2

city

state

postal_code

# Function Details

get_address_components(geocode_result)

This function extracts address components from the Google Maps Geocoding API response and organizes them into a dictionary with keys such as:

street_number

route

locality

administrative_area_level_1

administrative_area_level_2

country

postal_code

# Main Script Logic

Reads the input CSV using pandas.

Iterates through each row in the mailing_address_display column.

Calls the Google Maps API to geocode the address.

Extracts address components and populates corresponding columns in the DataFrame.

Saves the updated DataFrame to the output CSV file.

# Notes

Ensure your Google API key has access to the Geocoding API.

Handle API rate limits and errors (e.g., invalid addresses) as needed.

# Example Input

fraddress.csv:

mailing_address_display
1600 Amphitheatre Parkway, Mountain View, CA

# Example Output

frdatanew.csv:

mailing_address_display,address_line_1,address_line_2,city,state,postal_code
1600 Amphitheatre Parkway, Mountain View, CA,1600 Amphitheatre Pkwy,Mountain View,Santa Clara,CA,94043

License

This project is licensed under the MIT License.
