import glob, os

paths = glob.glob("/home/kazuki/Documents/myWork/MachineLearningModels/U-2-Net/test_data/test_images/*")
print(len(paths))

for i in range(len(paths)):
  new_name = "{0:04d}".format(i) + '.jpg'
  os.rename(paths[i], new_name)
