import json
import time

with open('coco_imglab.json') as json_file:
    data = json.load(json_file)
    #print(data)
    #print("----")
    #print(data['images'][0]['file_name'])
    
    fileNames = {}
    for val in data['images']:
     fileNames[str(val['id'])] = val['file_name']



    cats = {}
    for val in data['categories']:
     cats[str(val['id'])] = val['name']

    bbox = {}
    for val in data['annotations']:
     bbox[str(val['image_id']) + "|" + str(cats[str(val['category_id'])]) + "|" + str(time.time_ns())] = val['bbox']
     

    jsonOut = "[\n"
     


    
    for key, val in fileNames.items():
     jsonOut += '\n\t{"image":"'
     jsonOut += str(val)
     jsonOut += '",\n\t\t"annotations":\n\t\t[\n'
     for k, v in bbox.items():
       kk = k.split('|')
       if kk[0] == str(key):
        jsonOut += '\n\t\t\t{"label":"'
        jsonOut += str(kk[1])
        jsonOut += '","coordinates":{"x":' + str(round(v[0])) + ',"y":' + str(round(v[1])) + ',"width":' + str(round(v[2])) + ',"height":' + str(round(v[3])) + '}}'
        jsonOut += ','
     jsonOut = jsonOut[0:-1]
     jsonOut += '\n\t\t]\n'
     jsonOut += '\t},'
    jsonOut = jsonOut[0:-1]
    jsonOut += "\n]"

#print(jsonOut)
with open('annotations.json', 'w') as fp:
    fp.write(jsonOut)
