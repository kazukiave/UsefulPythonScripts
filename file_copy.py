import os
import shutil

src_folder = r"C:\Users\kazuj\Documents\AnacondaProjects\anaconda_keras_gpu_myScripts\Abstract_Painting_256GAN\ResultImages_v0_v1"
dist_folder = r"C:\Users\kazuj\Documents\AnacondaProjects\anaconda_keras_gpu_myScripts\Abstract_Painting_256GAN\ResultImages_v0_v1_selected"
select_paths = r"C:\Users\kazuj\Documents\UsefulPythonScripts\MyResearch\selectedImages.txt"
with open(select_paths, 'r') as f:
    for line in f.readlines():
        line = line.replace('\n' , '' )
        dist_path = os.path.join(dist_folder, os.path.basename(line))
        shutil.copy(line, dist_path)
    