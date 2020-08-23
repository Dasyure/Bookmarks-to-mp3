''' Converts audio file into flac file.

The function "convert_audio_type" changes into the directory where the file is
stored. After finding the file, it uses ffmpeg to convert the file into a new
audio format such as flac. To use another audio format instead of "flac"
simply change the variable "new_audio_type".

IMPORTANT:
1) This file uses ffmpeg installed locally from: https://ffmpeg.org/download.html
2) You must add ffmpeg to your PATH, for example:
   export PATH=$PATH:/<...path to ffmpeg...>/ffmpeg/bin
3) On Windows, the executable is named "ffmpeg.exe", if on MAC or Linux you
   may have to change the variable "ffmpeg_name".
'''

from glob import glob
from os import chdir, path
from subprocess import Popen
from time import sleep

def convert_audio_type(directory):
    '''
    Description: Converts all the downloaded webm files into a flac files.
    Params:
      (directory): Where to get the downloaded webm files from.
    '''
    chdir(directory)

    ffmpeg_name = 'ffmpeg.exe'
    all_files = glob("*")
    all_files.sort(key=path.getmtime) # sorts the files by date
    new_audio_type = "flac"
    for file in all_files:
        new_file = file.split(".")[0] + "." + new_audio_type
        cmds = [ffmpeg_name, '-i', file, new_file]
        p = Popen(cmds)
        sleep(5)
        p.kill()
        print(f"\033[1;32;49m Converted {file} to {new_file}") # green
        sleep(0.5)
        print()

    chdir('..')
    