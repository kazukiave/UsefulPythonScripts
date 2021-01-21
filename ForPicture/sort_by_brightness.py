
#env = conda py36
import numpy as np
import scipy.stats as sstats
import cv2
import glob
import os

target_path = "/Users/kazuki/Pictures/Lightroom_Saved_Photos/201113_osu/ForInstagram"

brightness_list = []
names_list = []


def get_brightness_mean(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = np.array(img).flatten()

    return img.mean()

def get_rgb_mean(path):
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    b = img.T[0].flatten().mean()
    g = img.T[1].flatten().mean()
    r = img.T[2].flatten().mean()
    return r + b + g

pictures = glob.glob(target_path + "/*.jpg")
idx = 0
for picture in pictures:
    print(picture)
    brightness = get_rgb_mean(picture)
    #brightness = get_brightness_mean(picture)
    brightness_list.append(brightness)
   
    base_name = os.path.basename
    names_list.append(base_name)

for i in range(len(brightness_list)):
    count = 0
    for l in brightness_list:
        if(brightness_list[i] > l):
            count += 1
    
    old_name = pictures[i]
    new_name = os.path.join(target_path, '{0:04d}'.format(count)  + ".jpg")
    os.rename(old_name, new_name)

    print(str(count))
    count = 0