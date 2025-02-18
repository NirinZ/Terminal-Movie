# %%
from tkinter import image_names
from PIL import Image
import numpy as np
import os
import MuchColors as mc
import colorama
import sys
# from colorama import Fore, Back, Style
colorama.init(autoreset=True)

is_horizontal = False
if len(sys.argv) > 3 and sys.argv[3] == 'h':
    is_horizontal = True

if len(sys.argv) > 2 and sys.argv[2].isnumeric():
    MAX_WIDTH = int(sys.argv[2])
elif len(sys.argv) > 2 and sys.argv[2] == 'm':
    MAX_WIDTH = 363
elif len(sys.argv) > 2 and sys.argv[2] == 'h':
    MAX_WIDTH = 113
else:
    MAX_WIDTH = 56

print(os.getcwd())
if len(sys.argv) < 2:
    img_name = input("Image name: ")
else:
    img_name = sys.argv[1]
img_obj = Image.open(img_name)
if is_horizontal:
    img_obj = img_obj.rotate(90, expand=True)
width, height = img_obj.size
resio = width / height
img = np.array(img_obj.resize((MAX_WIDTH, int(MAX_WIDTH/(resio*2)))).convert('RGB'))
# Image.fromarray(img, 'RGB').show()
new_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
li = []
for i in range(img.shape[0]):
    lj = []
    for j in range(img.shape[1]):
        # new_image[i, j] = [0,0,255]
        img_color = img[i, j]
        rgb = mc.RGB(img_color[0], img_color[1], img_color[2])
        normal_color = mc.get_cloosest_color(rgb)
        lj.append(normal_color)
        new_image[i, j] = normal_color.rgb.to_list()
    li.append(lj)
    print(f'{100 * i/img.shape[0]:.1f}',"%", end='           \r')

print()
for i in li:
    t = ''
    for j in i:
        t += f"{j.fore}{j.back}M\33[0m"
    print(t)

# ima = Image.fromarray(new_image, 'RGB')
# ima.show()
# ima.save("save.png")
# %%
