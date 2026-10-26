import requests
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
	
# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/
	
# To hit our API, you'll be making requests to:
	
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
	
# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
	
url = base_url + "/api/3/action/package_show"
	
params = { "id": "ttc-subway-delay-data"}
	
package = requests.get(url, params = params).json()

resources = package["result"]["resources"]

csv_resource = None
for item in resources:
    if item["name"] == "TTC Subway Delay Data since 2025.csv" and item["format"] == "CSV":
        csv_resource = item
        break

if csv_resource is None:
    raise Exception("Could not find the 2025+ CSV resource. Did the name or format change?")

print(csv_resource["url"])

# Download the CSV file
csv_url = csv_resource["url"]

with requests.get(csv_url) as r:
    r.raise_for_status()
    with open(DATA_DIR / "ttc_subway_delay_data_since_2025.csv", "wb") as f:
        f.write(r.content)