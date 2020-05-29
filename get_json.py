import json

def get_json():
    """
    Place the file 'Bookmarks' into the same directory as get_json.py.
    You can find the 'Bookmarks' file from:
        C:\\Users\\<USERNAME>\\AppData\\Local\\Google\\Chrome\\User Data\\Default

    Returns: 
        (json): Chrome bookmarks as a JSON file is returned
    """
    with open('Bookmarks', 'r') as f:
        return json.load(f)

def find_child(folder, child_name):
    """Returns the folder named 'child_name'"""
    for bookmark in folder:
        if bookmark['name'] == child_name:
            return bookmark

def find_json_folder(json_file, folder_path):
    """
    Finds the folder which contains the Youtube links

    Params:
      json_file (json): The return value of get_json(), in other words, the 'Bookmarks' file jsonified
      folder_path (list): List of the folder names, with the last folder being the folder you're looking for
                          e.g. ["root", "bookmark_bar"]
    Returns: 
        (json): The sub directory inside the original JSON file, the directory being "folder_path[-1]"
    """
    # Error checking: no path given
    if not folder_path:
        raise ValueError("Folder path not given")

    # Error checking: Can't find folder
    find_this_folder = folder_path[0]
    # if find_this_folder not in json_file:
    #     if 'children' not in json_file:
    #         raise ValueError ("Folder doesn't exist") 
    #     if find_this_folder not in json_file['children']:
    #         raise ValueError ("Folder doesn't exist 2")


    folder = find_child(json_file['children'], find_this_folder)

    # Base case: return folder
    if len(folder_path) == 1:
        return folder

    # Recursive case: keep finding folder
    else:
        return find_json_folder(folder, folder_path[1:])