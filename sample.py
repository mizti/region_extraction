from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import skimage.data
import selectivesearch

def draw_rect_on_image(image_array, x, y, w, h):
    im = Image.fromarray(image_array)
    draw = ImageDraw.Draw(im)
    draw.rectangle(((x, y),(x+w, y+h)), outline="red")
    del draw
    return im
    

img = skimage.data.astronaut()
img_lbl, regions = selectivesearch.selective_search(img, scale=500, sigma=0.9, min_size=10)

for index, region in enumerate(regions):
    rect = regions[index]['rect']
    im = draw_rect_on_image(img, rect[0], rect[1], rect[2], rect[3])
    im.save('test' + str(index) + '.png')

#draw = ImageDraw.Draw(pil_im)
#draw.rectangle(((50,70),(100,300)), outline = "red")
## point of left-top and right-bottom
#del draw
#
## write to stdout
##pil_im.save(sys.stdout, "PNG")
#
#pil_im.save('test2.png')
