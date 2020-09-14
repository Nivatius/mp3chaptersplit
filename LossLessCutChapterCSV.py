
#makes csv files of all mp3 in folder for use with
# https://mifi.no/losslesscut/
# faster but more manual work


import glob
filelist=glob.glob('*.mp3')
import mutagen
import csv


print(filelist)
for file in filelist:
    print(file)
    inputfile=mutagen.File(file)
    print(inputfile.pprint())
    print("########################")

    print("Chapters found in: " + file)
    chapters = list()
    exportpaths= list()
    for key in inputfile.keys():
        if key[:5] == "CHAP:":
            chapters.append(key)


    filename= file[:-4]+".csv"
    with open(filename, mode='w', newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)




        for key in chapters:
            # parsing chapter info for start and end times and title
            #print(inputfile[key])
            string= str(inputfile[key].pprint())
            #print(string)

            timeinfo=string.find("time=")
            endtimeinfo=string[timeinfo:].find(" ")
            times=string[timeinfo+5:timeinfo+endtimeinfo].split("..")
            #print(times)
            chaptertitle=(string[string.find("TIT2=")+5:])

            employee_writer.writerow([str(int(times[0]) / 1000), str(int(times[1]) / 1000), chaptertitle])
            chaptertitle=chaptertitle.replace('"','""')
            print(str(int(times[0])/1000)+","+str(int(times[1])/1000)+',"'+chaptertitle+'"')


