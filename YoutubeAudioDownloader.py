#!/usr/bin/env python

"""Youtube audio and subtitles downloader"""
__author__ = "Luke Lancaster"
__copyright__ = "Copyright (c) 2018, Luke Lancaster"

__license__ = "MIT"
__version__ = "0.0.4"
__email__ = "lancaster.lucas.a@gmail.com"
__status__ = "Development"

from pytube import YouTube, Playlist
from pytube.helpers import safe_filename

def download_playlist(playlist_url):
  # Init Playlist
  pl = Playlist(playlist_url)
  pl.populate_video_urls()

  # Process each video
  for video_url in pl.video_urls:
    yt = YouTube(video_url)
    
    # Download audio file
    yt.streams.filter(only_audio=True).first().download(filename="{}_audio".format(yt.title))

    # Downloard subtitles file
    caption = yt.captions.get_by_language_code('en')
    file_name = safe_filename(yt.title)
    with open("{}_subtitles.srt".format(file_name), "w") as srt_file:
      print(caption.generate_srt_captions(), file=srt_file)


if __name__ == "__main__":
  # INPUT PLAYLIST URL HERE
  input_playlist_url = "https://www.youtube.com/watch?v=GnGLTThwpLU&list=PLp-wXwmbv3z-tgjTsJZMITTZvPoX_s5PV" 
  
  download_playlist(input_playlist_url)
