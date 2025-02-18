# %%
from PIL import Image
import numpy as np
import os
import MuchColors as mc

print(os.getcwd())
img = np.array(Image.open(input("Image name: ")).convert('RGB'))
# Image.fromarray(img, 'RGB').show()
new_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_color = img[i, j]
        rgb = mc.RGB(img_color[0], img_color[1], img_color[2])
        normal_color = mc.get_cloosest_color(rgb)
        # new_image[i, j] = [0,0,255]
        new_image[i, j] = normal_color.rgb.to_list()
    print(f'{100 * i/img.shape[0]:.1f}',"%", end='           \r')

ima = Image.fromarray(new_image, 'RGB')
ima.show()
ima.save("save.png")

## import code
## code.interact(local=globals())

# %%
