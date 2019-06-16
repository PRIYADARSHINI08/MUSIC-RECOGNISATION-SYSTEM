import json

#data = json.load(open('kaatru.json'))

data={"status":{"msg":"Success","code":0,"version":"1.0"},"metadata":{"music":[{"external_ids":{"isrc":"INS171806684","upc":"886447305652"},"play_offset_ms":9260,"external_metadata":{"deezer":{"album":{"id":72370382},"artists":[{"name":"A.R. Rahman","id":491}],"track":{"name":"Mazhai Kuruvi (From \"Chekka Chivantha Vaanam\")","id":"550476552"}},"spotify":{"album":{"name":"Mazhai Kuruvi (From \"Chekka Chivantha Vaanam\")","id":"1CsEvbpeEVcek0pxt8SIv4"},"artists":[{"name":"A.R. Rahman","id":"1mYsTxnqsietFxj1OgoGbG"},{"name":"Arvind Swami","id":"1U4sM1h3dqHhn7a8fgzFE3"},{"name":"STR","id":"00Y76ybB3PJCRrIlUXk7CZ"},{"name":"Vijay Sethupathi","id":"31lzE0FfEcg2oIMD8FlICU"},{"name":"Arun Vijay","id":"2FW2TPhMk43qnTiJrngSwv"},{"name":"Jyothika","id":"7mfFLMsTe5JAwIY5DZ7NTF"},{"name":"Aishwarya Rajesh","id":"4eiylYaB9g7znXt6m9KN3u"},{"name":"Aditi Rao Hydari","id":"147zpWRMJhUudkGSDZ5qJ0"}],"track":{"name":"Mazhai Kuruvi - From \"Chekka Chivantha Vaanam\"","id":"74IE3QmRR07So8TE0320Oa"}}},"artists":[{"name":"A.R. Rahman"}],"genres":[{"name":"Soundtrack (Tamil)"}],"title":"Mazhai Kuruvi (From \"Chekka Chivantha Vaanam\")","release_date":"2018-09-05","label":"Sony Music Entertainment India Pvt. Ltd.","duration_ms":347980,"album":{"name":"Mazhai Kuruvi (From \"Chekka Chivantha Vaanam\")"},"acrid":"881dd3d9d51fd8a4c1d3374cc726c2fe","result_from":3,"score":100},{"external_ids":{"isrc":"INS171806742","upc":"886447318041"},"play_offset_ms":9280,"external_metadata":{"spotify":{"album":{"name":"Neeli Kanumallo (From \"Nawab\")","id":"4ojNG37XY8g88XiMUNCGOs"},"artists":[{"name":"A.R. Rahman","id":"1mYsTxnqsietFxj1OgoGbG"},{"name":"Nakul Abhyankar","id":"45dUPHFa2AoC4lqFTcPmiD"},{"name":"Arvind Swami","id":"1U4sM1h3dqHhn7a8fgzFE3"},{"name":"Vijay Sethupathi","id":"31lzE0FfEcg2oIMD8FlICU"},{"name":"STR","id":"00Y76ybB3PJCRrIlUXk7CZ"},{"name":"Arun Vijay","id":"2FW2TPhMk43qnTiJrngSwv"},{"name":"Jyothika","id":"7mfFLMsTe5JAwIY5DZ7NTF"},{"name":"Aditi Rao Hydari","id":"147zpWRMJhUudkGSDZ5qJ0"},{"name":"Aishwarya Rajesh","id":"4eiylYaB9g7znXt6m9KN3u"}],"track":{"name":"Neeli Kanumallo - From \"Nawab\"","id":"7fe87XWffWlQUEPJ3QIuwT"}}},"artists":[{"name":"A.R. Rahman & Nakul Abhyankar"}],"title":"Neeli Kanumallo (From \"Nawab\")","release_date":"2018-09-07","label":"Sony Music Entertainment India Pvt. Ltd.","duration_ms":347080,"album":{"name":"Neeli Kanumallo (From \"Nawab\")"},"acrid":"2abe6d992fbe3d7b80b42bad5675e9c5","result_from":3,"score":100}],"timestamp_utc":"2019-03-21 15:56:07"},"cost_time":0.99599981307983,"result_type":0}
print(type(data))
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
                            
                        
                
