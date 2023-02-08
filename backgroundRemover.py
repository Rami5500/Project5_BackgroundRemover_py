#Removes the background of images
from rembg import remove
from PIL import Image

in_path = 'trademark.jpg'
out_path = 'output.png'

input = Image.open(in_path)
output = remove(input)
output.save(out_path)
