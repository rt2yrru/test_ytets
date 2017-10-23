from __future__ import unicode_literals
import os,json,sys
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import youtube_dl
print(youtube_dl.version.__version__)
