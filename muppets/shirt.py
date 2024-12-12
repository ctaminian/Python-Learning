import sys
import pathlib
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py before.jpg after.jpg")

image_types = [".jpg", ".jpeg", ".png"]
before_image = sys.argv[1].lower()
after_image = sys.argv[2].lower()

before_image_extension = pathlib.Path(before_image).suffix
after_image_extension = pathlib.Path(after_image).suffix

if not before_image_extension in image_types or not after_image_extension in image_types:
    sys.exit("Image files must be jpg, jpeg or png")

if before_image_extension != after_image_extension:
    sys.exit("Input and output images must have the same extension")

try:
    with Image.open(before_image) as im:
        im = ImageOps.fit(im,(600,600))
        with Image.open("shirt.png") as overlay:
            im.paste(overlay, (0,0), overlay)
            im.save(after_image)   
except FileNotFoundError:
    sys.exit("File does not exist")