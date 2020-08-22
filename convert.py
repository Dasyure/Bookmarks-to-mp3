from pytube import YouTube
from sys import argv
import subprocess
import time
import os

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

def convert_webm_flac(directory):
    '''
    Description: Converts all the downloaded webm files into a flac files.
    Params:
      (directory): Where to get the downloaded webm files from.
    '''
    os.chdir(directory)

    for file in os.listdir():
        new_file = file[:-4] + "flac"
        cmds = ['ffmpeg.exe', '-i', file, new_file]
        p = subprocess.Popen(cmds)
        time.sleep(5)
        p.kill()
        print(f"\033[1;32;49m Converted {file} to {new_file}") # green

    os.chdir('..')


def download_audio(url, directory):
    '''
    Description: Given a url, converts the youtube link to an audio file into a
        directory.
    Params:
      (url): The youtube link as an URL.
      (directory): Where to store the downloaded webm file.
    '''
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True) # List of audio streams
    stream = get_audio_stream_hq(streams)
    stream.download(directory)


def print_download_status(success, url):
    '''
    Description: After attempt to download is complete, this function prints out
                 the success status of the attempt.
    Params:
      (success): Boolean, 1 if succeeded, 0 if failed.
      (url): String, the url that was downloaded, or attempted to do so.
    '''
    if success:
        print(f"\033[1;32;49m Success: {url}") # green
    elif ('youtube' in url.split('.')):
        print(f"\033[1;31;49m Failed: {url}") # red
    else:
        print(f"\033[1;35;49m Not_YT_Link: {url}") # purple


def read_url_list(f, f_out):
    '''
    Description: Reads a list of URLs and converts each URL to an audio file.
    Params:
      (f): File object, referring to the file with the list of URLs.
      (f_out): File object, referring to the file with the list of
               failed Youtube URLs.
    '''
    directory = argv[1]
    success = True
    retry_limit = 3
    for line in f:
        url = line
        for i in range(0,retry_limit): # retry download three times, if download fails
            try:
                download_audio(url, directory)
                success = True
                break # no need to retry, download succeeded
            except:
                success = False
                # if there's a yt link and it's the last retry
                if 'youtube' in url.split('.') and i == (retry_limit - 1):
                    f_out.write(url + '\n')
                elif 'youtube' in url.split('.'):
                    pass # retry download
                else:
                    break # no need to retry, not a yt link
        print_download_status(success, url)
    convert_webm_flac(directory)


if __name__ == '__main__':
    if len(list(argv)) != 2:
        raise Exception(f'Usage: python {argv[0]} name_of_directory')

    input_file = 'url_list.txt' # list of URLs to be converted
    output_file = 'url_cant_open.txt' # for failed youtube URLs

    f = open(input_file, 'r')
    f_out = open(output_file, 'a')
    read_url_list(f, f_out)

    f.close()
    f_out.close()

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