import glob
import mutagen
from mutagen.easyid3 import EasyID3
from pydub import AudioSegment
import os



dir_path = os.path.dirname(os.path.realpath(__file__))
print("current directory: "+dir_path)
filelist=glob.glob('*.mp3')

print("found mp3 files:")
print(filelist)

for file in filelist:
    inputfile=mutagen.File(file)
    chapters=list()
    #print(test['TIT2'])
    for key in inputfile.keys():
        if key[:5]=="CHAP:":
            chapters.append(key)
    print(chapters)

    print("loading mp3 file - this might take a while")
    song = AudioSegment.from_mp3(file)
    print(file+" loaded")
    chapnr=0

    for key in chapters:
        print(inputfile[key])
        string= str(inputfile[key].pprint())
        #print(string)

        timeinfo=string.find("time=")
        endtimeinfo=string[timeinfo:].find(" ")
        times=string[timeinfo+5:timeinfo+endtimeinfo].split("..")
        print(times)
        chaptertitle=(string[string.find("TIT2=")+5:])


        # Saving


        exportpath="out\\"+file[:-4]+" - "+str(chapnr) +'.mp3'


        print(exportpath)
        song[int(times[0]):int(times[1])].export(exportpath, format="mp3")
        print(chaptertitle+ " saved")

        outputfile = EasyID3(exportpath)
        print(outputfile.keys())
        outputfile["title"] = str(chaptertitle)
        outputfile["tracknumber"]=str(chapnr)
        source = EasyID3(file)
        outputfile["artist"] = source["artist"]
        outputfile["album"] = source["album"]
        outputfile.save()
        chapnr+=1










