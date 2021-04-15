import csv
import math

src_path = r"C:\Users\kazuj\Documents\DataSet\AbstractPaitnt\abstract_images.csv"
dist_path = r"C:\Users\kazuj\Documents\DataSet\AbstractPaitnt\abstract_images_classfied.csv"

with open(src_path) as src:
    with open(dist_path, 'w',  newline="") as dist:
        writer = csv.writer(dist)
        writer.writerow(["images", "x", "y", "z", "round_x", "round_y", "round_z"])

        reader = csv.reader(src)
        header = False 
        for row in reader:
            print(row)
            if header is not True:
                header = True
            else:
                round_x = int(round(float(row[1]),1) * 10)
                round_y = int(round(float(row[2]),1) * 10)
                round_z = int(round(float(row[3]),1) * 10)
                writer.writerow([row[0], row[1], row[2], row[3], round_x, round_y, round_z])