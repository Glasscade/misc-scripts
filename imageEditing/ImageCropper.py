# Script for extracting a portrait image from 16:9 video game screenshots for use in diagrams and Wiki Entries

from PIL import Image
from pathlib import Path

folderPathStr = "[INPUT_DIRECTORY]"
saveToPathStr = "[EXPORT_DIRECTORY]"
folderPath = Path(folderPathStr)
saveToPath = Path(saveToPathStr)
cropBoxScale = 750

def CropAndSave(folderPath, saveToPath):
    for filePath in folderPath.iterdir():
        if filePath.is_file():
            image = Image.open(filePath)
            
            width, height = image.size
            imageMiddle = width/2
            # (left, upper, right, lower)
            cropBox = (imageMiddle-(cropBoxScale/2), 0,imageMiddle+(cropBoxScale/2),cropBoxScale) 
            croppedImage = image.crop(cropBox)
            croppedImage.save(saveToPathStr+filePath.name)

CropAndSave(folderPath, saveToPath)
