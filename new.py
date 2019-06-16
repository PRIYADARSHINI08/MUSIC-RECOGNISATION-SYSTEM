#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import json

if __name__ == '__main__':
    config = {
        'host':'identify-ap-southeast-1.acrcloud.com',
        'access_key':'bf333059bea5a1ee44cbddc277ed4205',
        'access_secret':'VxCkxxFjX9RJ8RYsVJKAeA8yd167kKUNaCgoqlLC',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)
    loc=r"C:\Users\SriniVas\Desktop\acrcloud_sdk_python-master\windows\win32\python3\test.mp3"

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    data1=re.recognize_by_file(loc, 0, 10)
    #print(data1)
    print(type(data1))
    data=json.loads(data1)
    print(type(data))

    '''print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(loc)))

    buf = open(loc, 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print(re.recognize_by_filebuffer(buf, 0, 10))
'''
    for dt in data:
        if(dt=='metadata'):
            print("metadata")
            temp=data[dt]
            for i in temp:
                if(i=='music'):
                    temp1=temp[i]
                    print("music")
                    for j in temp1[0]:
                        if(j=='external_metadata'):
                            temp2=temp1[0][j]
                            for k in temp2:
                                if(k=='spotify'):
                                    print('spotify')
                                    l=temp2[k]
                                    for q in l:
                                        if q=='album':
                                            al=l[q]
                                            for m in al:
                                                if(m=='name'):
                                                   print("Album : "+al['name'])
                                        if q=='artists':
                                            temp3=l[q]
                                            n=len(temp3)
                                            print("Artists : ",end="")
                                            for i in range(0,n):
                                                if 'name' in temp3[i]:
                                                    print(temp3[i]['name'],end=",")
                                            print()
                        if(j=='genres'):
                            temp4=temp1[0][j]
                            for k in temp4[0]:
                                if(k=='name'):
                                    print("Genres : "+temp4[0][k])
                        if(j=='release_date'):
                            print("Release Date : "+temp1[0][j])
                                
