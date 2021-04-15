import glob, os

t_path = r"C:\Users\kazuj\Desktop\GeometryRecursion"
extension = "png"

path = os.path.join('{0}'.format(t_path), '*.{}'.format(extension))
paths = glob.glob(path)
print('path: {}'.format(path))
print('data count: {}'.format(len(paths)))

for i in range(len(paths)):
  new_name = "{0:05d}".format(i) + '.' + extension
  new_name = os.path.join(t_path, new_name)
  os.rename(paths[i], new_name)