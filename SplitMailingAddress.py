import googlemaps
import pandas as pd


df = pd.read_csv('/Users/surajnavkudkar/Desktop/fraddress.csv')
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


gmaps = googlemaps.Client(key="google_key")
for index in range(len(df["mailing_address_display"])):
    if df["mailing_address_display"][index] is not None:
        geocode_result = gmaps.geocode(df["mailing_address_display"][index])
        if geocode_result is not None and len(geocode_result) > 0:
            address_components = get_address_components(geocode_result[0])
            address_line_1 = ""
            if address_components["street_number"] is not None:
                address_line_1 += address_components["street_number"] + " "
            if address_components["route"] is not None:
                address_line_1 += address_components["route"]

            df.at[index, 'address_line_1'] = address_line_1
            df.at[index, 'address_line_2'] = address_components["locality"]
            df.at[index, 'city'] = address_components["administrative_area_level_2"]
            df.at[index, 'state'] = address_components["administrative_area_level_1"]
            df.at[index, 'postal_code'] = address_components["postal_code"]

            print(address_components)


df.to_csv('/Users/surajnavkudkar/Desktop/frdatanew.csv', index=False)
