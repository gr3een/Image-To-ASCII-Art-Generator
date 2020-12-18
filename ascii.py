
from PIL import Image
import numpy as np
from collections import namedtuple
from colorama import Fore, Back, Style 

Size = namedtuple('Size', ['width', 'height'])

tile_size = Size(width = 10, height = 20)
image_size = Size(width = 2000, height = 2000) #change the size of from changing width and height
no_horizontal_tiles = int(image_size.width / tile_size.width) 
no_vertical_tiles = int(image_size.height / tile_size.height)

img = Image.open('skull.jpg') #input image file
img = img.convert('L')
img = img.resize(image_size)

def find_tile_brightness(img_section):
    width, height = img_section.size
    pixels = np.array(img_section)
    return np.average(pixels.reshape(width * height))


brightness_grid = []

for y in range(0, image_size.height, tile_size.height):
    row = []
    for x in range(0, image_size.width, tile_size.width):
        img_tile = img.crop((x,y,x + tile_size.width, y + tile_size.height))
        row.append(find_tile_brightness(img_tile))
    brightness_grid.append(row)

def print_art():
    print(Fore.LIGHTBLUE_EX + "ASCII ART: \n")

    for x in range(0, no_vertical_tiles):
        for y in range(0, no_horizontal_tiles):
            filler = ''
            #import Fore to change color of each element
            if brightness_grid[x][y] < 10:
                filler = Fore.CYAN + '?' 
            elif brightness_grid[x][y] >= 10 and brightness_grid[x][y] < 20:
                filler = Fore.BLUE + ','
            elif brightness_grid[x][y] >= 20 and brightness_grid[x][y] < 50:
                filler = Fore.BLACK + '+'
            elif brightness_grid[x][y] >= 50 and brightness_grid[x][y] < 100:
                filler = Fore.RED + '='
            elif brightness_grid[x][y] >= 100 and brightness_grid[x][y] < 140:
                filler = Fore.MAGENTA + 's'
            elif brightness_grid[x][y] >= 140 and brightness_grid[x][y] < 180:
                filler = Fore.CYAN+'.'
            elif brightness_grid[x][y] >= 180 and brightness_grid[x][y] < 200:
                filler = Fore.LIGHTBLACK_EX +'$'
            elif brightness_grid[x][y] >= 200 and brightness_grid[x][y] < 220:
                filler = Fore.GREEN+ '#'
            elif brightness_grid[x][y] >= 220:
                filler = Fore.YELLOW + '@'


            print(filler, end="")

        print("", end="\n")


print_art()


