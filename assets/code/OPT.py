from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
import numpy.linalg as lin


def boxfilter(n):
    assert (n%2 != 0),"Dimension must be odd"
    a = np.empty((n, n))
    a.fill(1/(n*n))
    return a

def gauss1d(sigma):
    arr_length = 6*sigma
    if arr_length % 2 == 0:
        val = ((arr_length)/2)+1
    elif arr_length.is_integer() == False:
        arr_length = np.ceil(arr_length)
        val = (arr_length + 1)/2
        if arr_length % 2 == 0:
            arr_length = arr_length + 1
            val = arr_length - 1
    elif arr_length % 2 != 0:
        val = (arr_length + 1)/2
    lst = list(range(int(val)))
    neg_lst = [-x for x in lst]
    neg_lst.remove(0)
    neg_lst.reverse()
    a_val = neg_lst + lst
    a_val = [math.exp(- (abs(x)*abs(x)) / (2*sigma*sigma)) for x in a_val]
    sum_aval = sum(a_val)
    a_aval = [(1/sum_aval)*x for x in a_val]
    return np.asarray(a_aval)

def gauss2d(sigma):
    f = gauss1d(sigma)
    return signal.convolve2d(f[np.newaxis], np.transpose(f[np.newaxis]))

def gaussconvolve2d(array,sigma):
    assert (array.ndim == 2),"Array must be 2D"
    filter = gauss2d(sigma)
    result = signal.convolve2d(array, filter, 'same')
    return result



def boxconvolve2d(image, n):
    filter = boxfilter(n)
    result = signal.convolve2d(image, filter, 'same')
    return result

def Estimate_Derivatives(im1, im2, sigma=1.5, n=3):
  
    im1_smoothed = gaussconvolve2d(im1,sigma)
    Ix, Iy = np.gradient(im1_smoothed)
    It = boxconvolve2d(im1, n) - boxconvolve2d(im2, n)
    return Ix, Iy, It

def Optical_Flow(im1, im2, x, y, window_size, sigma=1.5, n=3):
    assert((window_size % 2) == 1) , "Window size must be odd"
    Ix, Iy, It = Estimate_Derivatives(im1, im2, sigma, n)
    half = np.floor(window_size/2)

    win_Ix = Ix[y-half-1:y+half, x-half-1:x+half].T.flatten()

    win_Iy = Iy[y-half-1:y+half, x-half-1:x+half].T.flatten()
    win_It = It[y-half-1:y+half, x-half-1:x+half].T.flatten()
    A = np.vstack([win_Ix, win_Iy])
    V = np.dot((-1)*win_It,np.dot(lin.pinv(np.dot(A.T,A)), A.T))

    return V[1], V[0]

def AppendImages(im1, im2):

    im1cols, im1rows = im1.size
    im2cols, im2rows = im2.size
    im3 = Image.new('RGB', (im1cols+im2cols, max(im1rows,im2rows)))
    im3.paste(im1,(0,0))
    im3.paste(im2,(im1cols,0))
    return im3

def DisplayFlow(im1, im2, x, y, uarr, varr):

    im3 = AppendImages(im1,im2)
    offset = im1.size[0]
    draw = ImageDraw.Draw(im3)
    xinit = x+uarr[0]
    yinit = y+varr[0]
    for u,v,ind in zip(uarr[1:], varr[1:], range(1, len(uarr))):
        draw.line((offset+xinit, yinit, offset+xinit+u, yinit+v),fill="red",width=2)
        xinit += u
        yinit += v
    draw.line((x, y, offset+xinit, yinit), fill="yellow", width=2)
    im3.show()
    del draw
    return im3

def HitContinue(Prompt='Hit any key to continue'):
    input(Prompt)

x=278
y=277

window_size=17

# sigma of the 2D Gaussian (used in the estimation of Ix and Iy)
sigma=1.5

# size of the boxfilter (used in the estimation of It)
n = 3


# scale factor for display of optical flow (to make result more visible)
scale=10

PIL_im1 = Image.open('frame07.png')
PIL_im2 = Image.open('frame08.png')
im1 = np.asarray(PIL_im1)
im2 = np.asarray(PIL_im2)
dx, dy = Optical_Flow(im1, im2, x, y, window_size, sigma, n)
print('Optical flow: [', dx, ',', dy, ']')
plt.imshow(im1, cmap='gray')
plt.hold(True)
plt.plot(x,y,'xr')
plt.plot(x+dx*scale,y+dy*scale, 'dy')
print('Close figure window to continue...')
plt.show()
uarr = [dx]
varr = [dy]

print('frame 7 to 8')
DisplayFlow(PIL_im1, PIL_im2, x, y, uarr, varr)
HitContinue()

prev_im = im2
xcurr = x+dx
ycurr = y+dy
offset = PIL_im1.size[0]

for i in range(8, 14):
    im_i = 'frame%0.2d.png'%(i+1)
    print ('frame', i, 'to', (i+1))
    PIL_im_i = Image.open('%s'%im_i)
    numpy_im_i = np.asarray(PIL_im_i)
    dx, dy = Optical_Flow(prev_im, numpy_im_i, xcurr, ycurr, window_size, sigma, n)
    xcurr += dx
    ycurr += dy
    print(xcurr, ycurr)
    prev_im = numpy_im_i
    uarr.append(dx)
    varr.append(dy)
    #redraw the (growing) figure
    DisplayFlow(PIL_im1, PIL_im_i, x, y, uarr, varr)
    HitContinue()

