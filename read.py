import gzip
import json

output_path = '/openalex/extracted/extract1.json.gz'

with gzip.open(output_path, 'rt') as file:
    data = json.load(file)
    for entry in data:
        print(entry)
