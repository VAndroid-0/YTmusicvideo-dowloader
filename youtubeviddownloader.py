# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q1gJcSFMQDvaY4Z0Wll0rgpB4YixEN1W
"""

!pip install --upgrade youtube_dl

from __future__ import unicode_literals
import youtube_dl
url = input()
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download ([url])