from PIL import Image
import numpy as np
import math
from scipy import signal

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

# signal.convolve2d and signal.correlated2d will produce different results if the filter is not symetric due to the associative property of convolution in essence
# convolution is used when multiple symmteric filters are pre-convolved and those multiple filters are then convolved to a single filter.

im = Image.open('bb.jpg')
im.show()
im = im.convert('L')
im_arr = np.asarray(im)
nim = gaussconvolve2d(im_arr, 3)
fim = Image.fromarray(nim)
if fim.mode != 'L':
    fim = fim.convert('L')
fim.save('bb_filtered.jpg')

# Since convolution with a Gaussian is seperable a 2D Gaussian filter can be obtianed by multiplying two 1D Gaussian filter a more efficient implementation will be to first convolve each row with a 1D fillter
# then convolve each column with a 1D filter which results in O(n) complexity instead of O(n^2) complexity.
