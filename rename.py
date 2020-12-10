import glob, os, sys

"""
command: cd this folder
command: python rename.py target_path extension

argv
0: this name
1: path
2: extension
"""

if(len(sys.argv) != 3):
  print("len(sys.argv):{}".format(len(sys.argv)))
  print(sys.argv)
  sys.exit()

path = os.path.join('{0}'.format(sys.argv[1]), '*.{}'.format(sys.argv[2]))
paths = glob.glob(path)
print('path: {}'.format(path))
print('data count: {}'.format(len(paths)))

for i in range(len(paths)):
  new_name = "{0:04d}".format(i) + '.' + sys.argv[2]
  new_name = os.path.join(sys.argv[1], new_name)
  os.rename(paths[i], new_name)
