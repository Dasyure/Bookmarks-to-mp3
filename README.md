# Bookmarks to MP3
This program downloads the audio from a Youtube link and then converts it to the desired audio format.

## Instructions:
1. After installing python, navigate to the directory with ```main.py``` and type:

    ```pip install -r requirements.txt```
2. Install ffmpeg from https://ffmpeg.org/download.html 
and add ffmpeg to PATH, for example:

    ```export PATH=$PATH:/<...path to ffmpeg...>/ffmpeg/bin```
3. Copy and paste your list of Youtube URLs from your bookmarks into ```url_list.txt```
4. Typical usage; if we want ```New_Folder``` as the folder where we download to, type:

    ```python main.py New_Folder```

## Important:
1) This file uses ffmpeg installed locally from: https://ffmpeg.org/download.html
2) You must add ffmpeg to your PATH, as shown above.
3) On Windows, the executable is named ```ffmpeg.exe```, if on MAC or Linux you
   may have to change the variable ```ffmpeg_name``` in ```convert.py```.

## File Structure:
    main.py
    -> read_url_list
       -> print_download_status
       -> download_audio
          -> get_audio_stream_hq
    -> convert_audio_type

Created: 2020-08-22