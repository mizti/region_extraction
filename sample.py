from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import skimage.data
import selectivesearch
import numpy as np

def draw_rect_on_image(img, x, y, w, h):
    draw = ImageDraw.Draw(img)
    draw.rectangle(((x, y),(x+w, y+h)), outline="red")
    del draw
    return img

img = Image.open('train_4363.jpg')
print('image_loaded')
image_array = np.asarray(img)
img_lbl, regions = selectivesearch.selective_search(image_array, scale=500, sigma=0.9, min_size=100)

for index, region in enumerate(regions):
    rect = regions[index]['rect']
    img = draw_rect_on_image(img, rect[0], rect[1], rect[2], rect[3])

img.save('test.png')
print('completed')
