from __future__ import unicode_literals
import youtube_dl
url = input()
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download ([url])
