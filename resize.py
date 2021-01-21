import glob
import os
from PIL import Image

files = glob.glob(r'C:\Users\kazuj\Documents\NeuralNetworkConsole\Dataset\201222anstraction_0\selected_renamed_dataset\*.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((256, 256))
    title, ext = os.path.splitext(f)
    dir_path = r"C:\Users\kazuj\Documents\NeuralNetworkConsole\Dataset\201222anstraction_0\selected_renamed_dataset_resize"
    img_resize.save(title + ext)