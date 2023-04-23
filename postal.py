import requests
import csv
import os

zipcode = input("Enter the zip code: ")
country_code = input("Enter the country code(optional): ")
headers = {
    "apikey": "773bbea0-e1e0-11ed-9323-d50dbf271faf"
}

params = (
    ("codes", f"{zipcode}"),
)
if country_code:
    params["country"] = f"{country_code}"

response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)

fields = ['postal_code', 'country_code', 'latitude', 'longitude', 'city', 'state', 'city_en', 'state_en', 'state_code',
          'province', 'province_code']

data = response.json()
if 'results' in data:
    results = data['results'][zipcode]
    filtered_results = [result for result in results if result['country_code'] == country_code]
    if filtered_results:
        file_exists = os.path.isfile('locations.csv')
        with open('locations.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            if not file_exists:
                writer.writeheader()
            for result in filtered_results:
                writer.writerow(result)
        print("Location data saved to locations.csv")
    else:
        print(f"No results found for zip code {zipcode} and country code {country_code}")
else:
    print("Error: Failed to retrieve location data.")