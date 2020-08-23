''' Downloads the audio file from the Youtube link.

The function "download_audio" calls "get_audio_stream_hq" which returns the
object of type 'stream' with the highest kbps audio. It then downloads the
audio file into the directory given.
'''

from pytube import YouTube

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
    if not streams:
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
      (directory): Where to store the downloaded webm file.
    '''
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True) # List of audio streams
    stream = get_audio_stream_hq(streams)
    stream.download(directory)
