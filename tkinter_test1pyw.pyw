import os, sys
import json
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

window = Tk()

def file_chooser():
    loc=askopenfilename(filetypes = (("",".mp3"),("All files","*.*")))
    new=loc.split("/")
    filename.delete(0.0,END)
    filename.insert(END,new[len(new)-1])
    recognition(loc)

    
def recognition(loc):
    config = {
            'host':'identify-ap-southeast-1.acrcloud.com',
            'access_key':'bf333059bea5a1ee44cbddc277ed4205',
            'access_secret':'VxCkxxFjX9RJ8RYsVJKAeA8yd167kKUNaCgoqlLC',
            'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
            'debug':False,
            'timeout':10 # seconds
        }
    re = ACRCloudRecognizer(config)
    #loc=r"C:\Users\SriniVas\Desktop\acrcloud_sdk_python-master\windows\win32\python3\test.mp3"

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    data1=re.recognize_by_file(loc, 0, 10)
    data=json.loads(data1)
    #print(re.recognize_by_file(loc, 0, 10))

    #print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(loc)))
    
    #buf = open(loc, 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    #print(re.recognize_by_filebuffer(buf, 0, 10))

    #data=re.recognize_by_filebuffer(buf, 0, 10)

    result.delete(0.0,END)
    for dt in data:
        if(dt=='metadata'):
            #print("metadata")
            temp=data[dt]
            for i in temp:
                if(i=='music'):
                    temp1=temp[i]
                    #print("music")
                    for j in temp1[0]:
                        if(j=='external_metadata'):
                            temp2=temp1[0][j]
                            for k in temp2:
                                if(k=='spotify'):
                                    #print('spotify')
                                    l=temp2[k]
                                    for q in l:
                                        if q=='album':
                                            al=l[q]
                                            for m in al:
                                                if(m=='name'):
                                                   result.insert(END,"\nAlbum : "+al['name'])
                                        if q=='artists':
                                            temp3=l[q]
                                            n=len(temp3)
                                            result.insert(END,"\nArtists : ")
                                            for i in range(0,n):
                                                if 'name' in temp3[i]:
                                                    result.insert(END,temp3[i]['name']+",")
                                            #print()
                        if(j=='genres'):
                            temp4=temp1[0][j]
                            for k in temp4[0]:
                                if(k=='name'):
                                    result.insert(END,"\nGenres : "+temp4[0][k])
                        if(j=='release_date'):
                            result.insert(END,"\nRelease Date : "+temp1[0][j])
                            
window.title("Song Recognizer")
window.configure(background="white")
window.geometry('500x200')

Label (window,text="Select the song file: ",bg="white",fg="black",font="none 12 bold").grid(row=1,column=0,sticky=W)


filename = Text(window,width=40,height=1,bg="white")
filename.grid(row=1,column=1,columnspan=2,sticky=W)

result = Text(window,width=61,height=10,bg="white")
result.grid(row=3,column=0,columnspan=2,sticky=W)

Button(window,text="Select",width=6,command=file_chooser).grid(row=2,column=0,sticky=W)



window.mainloop()


