from PIL import Image, ImageDraw
import numpy as np
import math
from scipy import signal
import ncc

def MakePyramid(image, minsize):
    x = minsize[0]
    y = minsize[1]
    a = []
    im = Image.open(image)
    assert((minsize[0] < im.size[0]) and (minsize[1] < im.size[1])), "minsize must not be greater than the original image size"
    a.append(np.asarray(im))
    while ((im.size[0] > x) and (im.size[1] > y)):
        im = im.resize((int(im.size[0]*0.75),int(im.size[1]*0.75)), Image.BICUBIC)
        im = np.asarray(im)
        a.append(im)
        im = Image.fromarray(im)
    #test = a[(len(a)-1)]
    #testim = Image.fromarray(test)
    #testim.show()
    #print(testim.size)
    return a

def ShowPyramid(pyramid):
    img = Image.fromarray(pyramid[0])
    imsizex = img.size[0] * len(pyramid)
    imsizey = img.size[1]
    #images = Image.new("L", (imsize, img.size[1]), 255)
    #images = Image.new("L", (imsizex, imsizey), 255)
    images = Image.new("L", (imsizex, imsizey), 255)
    prev_posx = 0;
    prev_posy = 0;
    length = len(pyramid)
    for i in range(0, length):
        im = Image.fromarray(pyramid[i])
        images.paste(im,(prev_posx, prev_posy))
        prev_posx += im.size[0]
        #prev_posy += im.size[1]
    images.show()

rate = 1
#shrinkage/growth rate according to the size of faces in an image
def FindTemplate(pyramid, template, threshold, rate):
    tmp = Image.open(template)
    tmp_width = tmp.size[0]
    #tmp_width = 15
    tmp_height = tmp.size[1]
    for k in range(0, len(pyramid)):
        print("image:", k)
        template = tmp.resize((int(rate*tmp_width*math.pow(0.75, k)), int(rate*tmp_height*math.pow(0.75, k))), Image.BICUBIC)
        original = Image.fromarray(pyramid[k])
        nccim = ncc.normxcorr2D(original, template)
        x = []
        for i in range(0, len(nccim)):
            for j in range(0, len(nccim[0])):
                #print([i, j])
                if(nccim[i,j] >= threshold):
                    x.append([i,j])
                    #print(nccim[i,j])
                    res = np.array(x)
                    draw = ImageDraw.Draw(original)
                    for i in range(0,len(res)):
                        ymid = res[i,0]+1
                        xmid = res[i,1]+1
                        draw.line((xmid-(template.size[0]/2),ymid-(template.size[1]/2),xmid+(template.size[0]/2),ymid-(template.size[1]/2)),fill="red",width=2)
                        draw.line((xmid-(template.size[0]/2),ymid+(template.size[1]/2),xmid+(template.size[0]/2),ymid+(template.size[1]/2)),fill="red",width=2)
                        draw.line((xmid+(template.size[0]/2),ymid+(template.size[1]/2),xmid+(template.size[0]/2),ymid-(template.size[1]/2)),fill="red",width=2)
                        draw.line((xmid-(template.size[0]/2),ymid+(template.size[1]/2),xmid-(template.size[0]/2),ymid-(template.size[1]/2)),fill="red",width=2)
        final = original.convert('RGB')
        final.show()
        input("Press Enter to continue")

