''' Reads in the URLs one by one from a txt file and downloads the audio.

The function "read_url_list" reads in the URLs, then uses "download_audio" to
download the audio. The status of whether or not the download succeeded is then
printed by "print_download_status". If the download fails the link is put into
a second txt file, so the user knows which files failed to download.
'''
from download import download_audio

def print_download_status(success, url):
    '''
    Description: After attempt to download is complete, this function prints out
                 the success status of the attempt.
    Params:
      (success): Boolean, 1 if succeeded, 0 if failed.
      (url): String, the url that was downloaded, or attempted to do so.
    '''
    is_yt_in_link = ('youtube' in url.split('.'))
    if success:
        print(f"\033[1;32;49m Success: {url}") # green
    if not success and is_yt_in_link:
        print(f"\033[1;31;49m Failed: {url}") # red
    if not is_yt_in_link:
        print(f"\033[1;35;49m Not_YT_Link: {url}") # purple


def read_url_list(f, f_out, directory):
    '''
    Description: Reads a list of URLs and converts each URL to an audio file.
    Params:
      (f): File object, referring to the file with the list of URLs.
      (f_out): File object, referring to the file with the list of
               failed Youtube URLs.
      (directory): Where to store the downloaded webm file.
    '''
    success = True
    retry_limit = 3
    for line in f:
        url = line
        for i in range(0, retry_limit): # retry download three times, if download fails
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
