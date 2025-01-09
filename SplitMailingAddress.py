import googlemaps
import pandas as pd
import os

def get_address_components(geocode_result):
    address_info = {
        'street_number': None,
        'route': None,
        'locality': None,
        'administrative_area_level_1': None,
        'administrative_area_level_2': None,
        'country': None,
        'postal_code': None,
    }

    if geocode_result and 'address_components' in geocode_result:
        for component in geocode_result['address_components']:
            for address_type in address_info.keys():
                if address_type in component['types']:
                    address_info[address_type] = component['long_name']
                    break

    return address_info

def process_addresses(input_file, output_file, api_key):
    gmaps = googlemaps.Client(key=api_key)

    # Read the input CSV file
    df = pd.read_csv(input_file)

    for index in range(len(df["mailing_address_display"])):
        if pd.notnull(df["mailing_address_display"][index]):
            geocode_result = gmaps.geocode(df["mailing_address_display"][index])
            if geocode_result and len(geocode_result) > 0:
                address_components = get_address_components(geocode_result[0])
                address_line_1 = ""
                if address_components["street_number"]:
                    address_line_1 += address_components["street_number"] + " "
                if address_components["route"]:
                    address_line_1 += address_components["route"]

                df.at[index, 'address_line_1'] = address_line_1
                df.at[index, 'address_line_2'] = address_components["locality"]
                df.at[index, 'city'] = address_components["administrative_area_level_2"]
                df.at[index, 'state'] = address_components["administrative_area_level_1"]
                df.at[index, 'postal_code'] = address_components["postal_code"]

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    # Dynamic input for file paths and API key
    input_file = input("Enter the path to the input CSV file: ").strip()
    output_file = input("Enter the path to save the output CSV file: ").strip()
    api_key = input("Enter your Google Maps API key: ").strip()

    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
    else:
        process_addresses(input_file, output_file, api_key)
