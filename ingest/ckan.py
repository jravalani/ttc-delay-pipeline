import requests

BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

def get_resources(dataset_id):
    response = requests.get(BASE_URL + "/api/3/action/package_show",
                            params={"id": dataset_id})
    response.raise_for_status()
    return response.json()["result"]["resources"]


def find_resource(resources, name, format):
    found = None
    for item in resources:
        if item["name"] == name and item["format"] == format:
            found = item
            break

    if found is None:
        raise SystemExit(f"Could not find the {name} resource. Did the name or format change?")

    return found


def download_resource(resource, path):
    with requests.get(resource["url"]) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)