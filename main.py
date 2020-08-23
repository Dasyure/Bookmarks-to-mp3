''' This program downloads the audio from a Youtube link and then converts it
    to the desired audio format.

The function "read_url_list" reads in the URLs from the first text file
named "input_file" and downloads the audio. If the download fails, the URL is
put into the second text file named "output_file".

INSTRUCTIONS:
1)  After installing python, install the dependencies on the terminal:
        pip install -r requirements.txt
2)  Install ffmpeg and add to PATH (see section below)
3)  Copy paste list of URLs into "url_list.txt"
4)  Typical usage example on terminal, directory in this case is "New_Folder":
        python main.py New_Folder

IMPORTANT:
1) This file uses ffmpeg installed locally from: https://ffmpeg.org/download.html
2) You must add ffmpeg to your PATH, for example:
   export PATH=$PATH:/<...path to ffmpeg...>/ffmpeg/bin
3) On Windows, the executable is named "ffmpeg.exe", if on MAC or Linux you
   may have to change the variable "ffmpeg_name" in "convert.py".

FILE STRUCTURE:
    main.py
    -> read_url_list
       -> print_download_status
       -> download_audio
          -> get_audio_stream_hq
    -> convert_audio_type

Created: 2020-08-22
'''
from sys import argv
from read_list import read_url_list
from convert import convert_audio_type

if __name__ == '__main__':
    if len(list(argv)) != 2:
        raise Exception(f'CLI Usage: python {argv[0]} name_of_directory')

    input_file = 'url_list.txt' # list of URLs to be converted
    output_file = 'url_cant_open.txt' # for failed youtube URLs
    directory = argv[1]

    f = open(input_file, 'r')
    f_out = open(output_file, 'a')
    read_url_list(f, f_out, directory) # URLs > Webm
    convert_audio_type(directory) #Webm > Flac

    f.close()
    f_out.close()
