#!/bin/bash
yt-dlp http://twitch.tv/$1 -o - | ffmpeg -i pipe: -listen 1 -s 720x480 -vcodec mpeg2video -b:v 1000k -f mpegts - 
