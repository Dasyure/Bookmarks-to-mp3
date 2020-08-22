from pytube import YouTube
from sys import argv

def get_audio_stream_hq(streams):
    '''
    Description: Given a list of audio stream objects from pytube, returns the
        object with the highest audio quality.
    Params:
      (list of streams object): List of audio stream objects.
    Returns:
      (stream object) : The audio stream with highest audio quality.
    Raises:
      Exception : if no audio streams given
    '''
    if len(streams) == 0:
        raise Exception('get_audio_stream_hq: No audio streams given')
    kbps = 0
    hq_stream = streams[0]
    for stream in streams:     # Get highest quality audio stream
        s_kbps = int(stream.abr.split('k')[0])
        hq_stream = stream if (s_kbps > kbps) else hq_stream
    return hq_stream


def download_audio(url, directory):
    '''
    Description: Given a url, converts the youtube link to an audio file into a
        directory.
    Params:
      (url): The youtube link as an URL.
    '''
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True) # List of audio streams
    stream = get_audio_stream_hq(streams)
    stream.download(directory)


def read_url_list(f):
    '''
    Description: Reads a list of URLs and converts each URL to an audio file.
    Params:
      (f): File object, referring to the file with the list of URLs.
    '''
    success = True
    for line in f:
        DIRECTORY = argv[1]
        URL = line
        try:
            download_audio(URL, DIRECTORY)
            success = True
        except:
            success = False
            if (len(URL) > 32) and (URL[12:19] == 'youtube'): # if it's a yt link
                with open(output_file, 'a') as output_file:
                    output_file.write(URL)
            else:
                pass
        if success:
            print(f"\033[1;32;49m {URL}")   # green url printed
        else:
            print(f"\033[1;31;49m {URL}")   # red url printed


if __name__ == '__main__':
    if len(list(argv)) != 2:
        raise Exception(f'Usage: python {argv[0]} name_of_directory')

    input_file = 'url_list.txt'
    output_file = 'url_cant_open.txt'

    f = open(input_file, 'r')
    read_url_list(f)
    f.close()


# import json
# from get_json import get_json, find_json_folder
# import requests

# file = get_json()
# folder_path = ["Youtube stuff (songs mainly)"]
# folder = find_json_folder(file['roots']['bookmark_bar'], folder_path)

# for bookmark in folder['children']:
#     print(bookmark)

# Export URL list to text file

# Use youtube-dl to download each URL



# # STRUCTURE:
# children
# date_added
# date_modified
# guid
# id
# name
# sync_transaction_version
# type