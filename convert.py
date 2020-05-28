import json
from get_json import get_json

file = get_json()
root = file["roots"]
bookmark_bar = root["bookmark_bar"]
print(bookmark_bar)
print(len(bookmark_bar))


print(bookmark_bar["date_added"]+'\n')


for i in bookmark_bar:
    print(i)