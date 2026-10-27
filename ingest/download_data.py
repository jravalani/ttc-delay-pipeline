from pathlib import Path
from ckan import get_resources, find_resource, download_resource

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

resources = get_resources("ttc-subway-delay-data")

delays = find_resource(resources, "TTC Subway Delay Data since 2025.csv", "CSV")
download_resource(delays, DATA_DIR / "ttc_subway_delay_data_since_2025.csv")

delay_codes = find_resource(resources, "ttc-subway-delay-codes", "XLSX")
download_resource(delay_codes, DATA_DIR / "ttc_subway_delay_codes.xlsx")

readme = find_resource(resources, "ttc-subway-delay-data-readme", "XLSX")
download_resource(readme, DATA_DIR / "ttc_subway_delay_readme.xlsx")

codes = find_resource(resources, "Code Descriptions.csv", "CSV")
download_resource(codes, DATA_DIR / "code_descriptions.csv")