# import pillow
from PIL import Image

# open image
with Image.open(r"D:\Programming\Python-Projects\rgb\rgb-image.jpg") as image:
    # get image size
    width, height = image.size

    # load pixels from image
    pixels = image.load()

    # empty pixels
    red = 0
    green = 0
    blue = 0
    count = 0  # to round off

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            red += r
            green += g
            blue += b
            count += 1

    # dividing by count to get average
    avg_red = red/count
    avg_green = green/count
    avg_blue = blue/count

    # clipping values within range 0 - 255
    # rounding off avg values
    avg_red = max(0, min(255, round(avg_red)))
    avg_green = max(0, min(255, round(avg_green)))
    avg_blue = max(0, min(255, round(avg_blue)))
    
    print(f"Red pixels is: {avg_red}")
    print(f"Green pixels is: {avg_green}")
    print(f"Blue pixels is: {avg_blue}")

'''
# display image
image.show()

# read 1 pixel
print(pixel_map[1, 1])

With PIL you can easily access and change the data 
stored in the pixels of an image. 
To get the pixel map, call load() on an image. 
The pixel data can then be retrieved by indexing the 
pixel map as an array.

0

Since the possible range of the values r, g, b is in 0 - 255, 
max(x, 0) is to prevent the value to drop below 0 and min(255, max(x, 0)) 
is to prevent the value to go above 255.
Example: if r = -20, max(r, 0) = max(-20, 0) = 0
and if r = 280, max(255, min(r, 0)) = max(255, min(280, 0)) = max(255, 0) = 255.
'''

