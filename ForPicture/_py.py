import glob
import os

target_path = "/Users/kazuki/Pictures/Lightroom Saved Photos/201113_osu/ForInstagram"

pictures = glob.glob(target_path + "/*")


for i in pictures:
    os.rename(i, i + ".jpg")