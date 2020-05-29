import json
from get_json import get_json, find_json_folder
import requests

file = get_json()
folder_path = ["Youtube stuff (songs mainly)"]
folder = find_json_folder(file['roots']['bookmark_bar'], folder_path)

for bookmark in folder['children']:
    print(bookmark)

# print(len(folder))

# # STRUCTURE:
# children
# date_added
# date_modified
# guid
# id
# name
# sync_transaction_version
# type