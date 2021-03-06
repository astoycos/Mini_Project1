#!/usr/bin/env python

#CopyRight 2018 Andrew Stoycos astoycos@bu.edu

#Source
#https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
#https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
#http://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/

import subprocess
import shutil

#command line input for ffmpeg video converter 
VID = ['ffmpeg', '-r', '1','-f', 'image2', '-s', '1920x1080', '-i','pic_downloads/%d.jpg', '-vcodec', 'libx264', '-crf',  '25',  '-pix_fmt', 'yuv420p', 'tweet_video.mp4','-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2']

subprocess.call(VID)

#remove directory and all pictures 
shutil.rmtree('pic_downloads') 

