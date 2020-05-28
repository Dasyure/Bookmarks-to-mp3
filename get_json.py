import json

def get_json():
    with open('Bookmarks', 'r') as f:
        return json.load(f)
