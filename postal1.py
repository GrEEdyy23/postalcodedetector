import requests
import csv
import os


zipcode = input("Enter the zip code: ")
country_code = input("Enter the country code (optional): ")
headers = {
    "apikey": "773bbea0-e1e0-11ed-9323-d50dbf271faf"
}

params = {
    "codes": f"{zipcode}",
}

if country_code:
    params["country"] = f"{country_code}"

response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)

fields = ['postal_code', 'country_code', 'latitude', 'longitude', 'city', 'state', 'city_en', 'state_en', 'state_code',
          'province', 'province_code']

data = response.json()
results = data['results'][f'{zipcode}']

for result in results:
    file_exists = os.path.isfile('locations.csv')
    # write the data to a CSV file
    with open('locations.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow(result)
    print("Location data saved to locations.csv")
