import os 
import sys
from PIL import Image,ImageFilter
newFolder,imagesFolder = None,None

# image folders
if len(sys.argv) == 3:
    imagesFolder = sys.argv[1]
    newFolder = sys.argv[2]

    if not os.path.exists(f'./{newFolder}'):
        folderPath = os.path.join(f'./{newFolder}')
        os.mkdir(folderPath)

    for image in os.listdir(f'./{imagesFolder}'):
        img = Image.open(f'./{imagesFolder}/{image}')
        img.save(f'./{newFolder}/{image}.png', 'png')





