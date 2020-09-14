# mp3chaptersplit
splitting podcast mp3 into chapters using their metadata.
You have one large podcast file with chapter-marks. You want several mp3 files with one cheapter each. this script does that.

## how to use
1. install ffmpeg, or copy it in the same directory as the script. Install pydub and mutagen via pip
2. copy mp3 file(s) that should be split and have chapter marks in the same folder
3. create folder out in the scripts directory
4. run script


## dependencies
this python script uses *pydub* with *ffmpeg* to split the mp3 files and *mutagen* to handle metadata. 
