import os
import json
import shutil
import re


#get json 3d data and sepalate 3d json(MAYA) people to each human
maya_path = "/home/kazuki/Documents/myWork/3d-pose-baseline-openpose/maya"
with open(os.path.join(maya_path, "3d_data.json"), 'r') as f:
  maya_3d_data = json.load(f)


#get human count in each image
pre_json3d_path = '/home/kazuki/Documents/myWork/openpose/data/Dotonbori/Result/v2_json/pre_json3d'

with open(os.path.join(pre_json3d_path, "people_count"), 'r') as f:
  people_count = f.read()
people_count_arr = people_count.split(',')

#Divid maya json in each human json
openpose_result_2d = '/home/kazuki/Documents/myWork/openpose/data/Dotonbori/Result/v2_json/Individual2Djson'
baseline_result_3d = '/home/kazuki/Documents/myWork/openpose/data/Dotonbori/Result/v2_json/Individual3Djson'
for_unitys_output = '/home/kazuki/Documents/myWork/openpose/data/Dotonbori/Result/v2_json/ForUnity'


oponpose_2d_jsons = os.listdir(openpose_result_2d)
oponpose_2d_jsons.sort()

"""
baseline_3d_jsons = os.listdir(baseline_result_3d)
baseline_3d_jsons.sort()
"""

image_count = 0
human_count = 0
for count in people_count_arr:
  if not str.isdigit(count):#is end of process
    break
  #make a folder for each image
  image_folder = os.path.join(for_unitys_output, 'image' + str(image_count))

  for i in range(int(count)):
    #make a 3d json
    if str(human_count) in maya_3d_data.keys():
      src_json = maya_3d_data[str(human_count)]
      print(maya_3d_data[str(human_count)])
      dist = os.path.join(di)
      break
    #copy 2d json to unity output
    else:
      print(human_count)
    human_count += 1

  image_count += 1
  if(image_count > 2): break
