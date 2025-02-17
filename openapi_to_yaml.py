import requests
import yaml
import json

url = "http://127.0.0.1:8000/openapi.json"
response = requests.get(url)

if response.status_code == 200:
    openapi_json = response.json()

    with open("openapi.yaml", "w", encoding="utf-8") as yaml_file:
        yaml.dump(openapi_json, yaml_file, allow_unicode=True, default_flow_style=False)

    print("OpenAPI spesifikasyonu openapi.yaml olarak kaydedildi!")
else:
    print("OpenAPI JSON alınamadı!")