#JSONCombiner.py
#if running twice in same day, make sure to 

import os
import json
from datetime import datetime

folder_path = "Files"

# List all files in the folder
files = os.listdir("Files")

python_objects = []


# Loop through each file
for file_name in files:
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith('.json'):
        # Process the file as needed
        print(f"Processing file: {file_name}")
        
        # Example: Read the content of the file
        with open(os.path.join(folder_path, file_name), 'r') as file:
            python_objects.append(json.load(file))

# Dump all the Python objects into a single JSON file.
with open(os.path.join(f"combined_{datetime.now().strftime('%Y-%m-%d')}.json"), "w") as f:
    json.dump(python_objects, f, indent=4)