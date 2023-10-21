# Importing framework // Remember to install in console: "pip install Pillow"
from PIL import Image

# Image path // Remember to change the path to your machine
path = "C:\Users\Windows\Desktop\Reading_JPG.RGB\panda_img.jpg"
panda = Image.open(path)

# Image data
matrix = panda.getdata()

# Image size
width, height = panda.size

# New image based on the original
avr_img = Image.new('L', (width, height)) 

# Analyzing image pixels
for y in range(height):
    for x in range(width):
        
        # Average image pixels
        r, g, b = panda.getpixel((x, y))
        avr_pixel = (r + g + b) // 3
        avr_img.putpixel((x, y), avr_pixel)

# Image saved
avr_img.save("gray_panda_img.jpg")

# Show image
avr_img.show()