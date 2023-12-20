
import requests
import json

# URL for the exchequer account (historical series) dataset from CSO
cso_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/"

# Making a GET request to the CSO website
response = requests.get(cso_url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Saving the data to a file named "cso.json"
    with open("cso.json", "w") as file:
        json.dump(data, file)

    print("Data has been successfully retrieved and saved to cso.json.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
