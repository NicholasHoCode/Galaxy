from PIL import Image, ImageDraw
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
# Computes the cost of given boundaries. Good boundaries have zero cost.
def get_boundaries_cost( boundaries, good_boundaries ):
return np.sum( boundaries != good_boundaries );
# ADDED, the original method did not provide a desirable result
# Computes the cost of given boundaries. Good boundaries have zero cost.
def get_boundaries_cost2( boundaries, good_boundaries ):
cost = []
for i in boundaries:
j = 0
for k in good_boundaries:
if ( i != k ):
j = j + 1
if ( j == len(good_boundaries) ):
cost.extend([1])
return np.sum(cost)
# Finds the indices of color_histograms given a series of cluster centres.
def cluster2boundaries(histograms, centres):
# Find the cluster assignment of each histogram
distances = cdist( histograms, centres )
idx = np.argmin( distances, 1 )
# Find the points where the index changes
boundaries = np.zeros( len(idx)+1, dtype = np.bool )
for i in range( len(idx)-1 ):
boundaries[i+1] = idx[i] != idx[i+1];
return boundaries
# Computes histograms from gray images
def compute_gray_histograms( grays, nbins ):
gray_hs = np.zeros(( nframes, nbins ), dtype = np.float );
for i in range( len(grays) ):
gray_im = grays[i]
v1 = np.histogram(gray_im.flatten(),bins=nbins, range=(0,255))
gray_hs[i] = v1[0]
return gray_hs;
def compute_color_histograms( colors, nbins ):
# === Main Function ===
color_hs = np.zeros(( nframes, nbins * 3 ), dtype = np.float );
for i in range( len(colors) ):
red_im = colors[i][0]
v1 = np.histogram(red_im.flatten(), bins=nbins, range=(0, 255))
green_im = colors[i][1]
v2 = np.histogram(green_im.flatten(), bins=nbins, range=(0, 255))
blue_im = colors[i][2]
v3 = np.histogram(blue_im.flatten(), bins=nbins, range=(0, 255))
color_hs[i] = np.concatenate((v1[0], v2[0], v3[0]))
return color_hs;
# === Main code starts here ===
fname = 'colours' # folder name
nframes = 151 # number of frames
im_height = 90 # image height
im_width = 120 # image width
# define the list of (manually determined) shot boundaries here
good_boundaries = [33, 92, 143];
# convert good_boundaries list to a binary array
gb_bool = np.zeros( nframes+1, dtype = np.bool )
gb_bool[ good_boundaries ] = True
# Create some space to load the images into memory
colors = np.zeros(( nframes, im_height, im_width, 3), dtype = np.uint8);
grays = np.zeros(( nframes, im_height, im_width ), dtype = np.uint8);
# Read the images and store them in color and grayscale formats
for i in range( nframes ):
imname = '%s/dwc%03d.png' % ( fname, i+1 )
im = Image.open( imname ).convert( 'RGB' )
colors[i] = np.asarray(im, dtype = np.uint8)
grays[i] = np.asarray(im.convert( 'L' ), dtype=float)
# Initialize color histogram
nclusters = 4;
nbins = range(2,13)
gray_costs = np.zeros( len(nbins) );
gray_costs = []
color_costs = np.zeros( len(nbins) );
color_costs = []
# === GRAY HISTOGRAMS ===
for n in nbins:
c2bBoundaries = []
grayhs = compute_gray_histograms(grays, n)
cs, distortion = kmeans(grayhs, nclusters)
c2b = cluster2boundaries(grayhs, cs)
for i in range(1,len(c2b)):
if ( c2b[i] == True ) :
c2bBoundaries.extend([i])
gray_costs.extend([get_boundaries_cost2(c2bBoundaries, good_boundaries)])
# === END GRAY HISTOGRAM CODE ===
plt.figure(1);
plt.xlabel('Number of bins')
plt.ylabel('Error in boundary detection')
plt.title('Boundary detection using gray histograms')
plt.plot(nbins, np.array(gray_costs))
plt.axis([2, 13, -1, 10])
plt.grid(True)
plt.show()
# === COLOR HISTOGRAMS ===
for n in nbins:
c2bBoundaries = []
colorhs = compute_color_histograms(colors, n)
cs, distortion = kmeans(colorhs, nclusters)
c2b = cluster2boundaries(colorhs, cs)
for i in range(1,len(c2b)):
if ( c2b[i] == True ) :
c2bBoundaries.extend([i])
color_costs.extend([get_boundaries_cost2(c2bBoundaries, good_boundaries)])
# === END COLOR HISTOGRAM CODE ===
plt.figure(2);
plt.xlabel('Number of bins')
plt.ylabel('Error in boundary detection')
plt.title('Boundary detection using color histograms')
plt.plot(nbins, color_costs)
plt.axis([2, 13, -1, 10])
plt.grid(True)
plt.show()
#fdiffs = np.zeros( nframes )
# === ABSOLUTE FRAME DIFFERENCES ===
f1 = range(0, nframes, 1)
fdiffs = np.array([sum(sum(abs((grays[j] - grays[i])))) for i,j in zip(f1, f1[1:])])
plt.figure(4)
plt.xlabel('Frame number')
plt.ylabel('Absolute frame difference')
plt.title('Absolute frame differences')
plt.plot(fdiffs)
plt.show()
sqdiffs = np.zeros( nframes )
# === SQUARED FRAME DIFFERENCES ===
s1 = range(0, nframes, 1)
sqdiffs = np.array([sum(sum(np.sqrt((grays[j] - grays[i])^2))) for i,j in zip(s1, s1[1:])])
plt.figure(5)
plt.xlabel('Frame number')
plt.ylabel('Squared frame difference')
plt.title('Squared frame differences')
plt.plot(sqdiffs)
plt.show()
avgdiffs = np.zeros( nframes )
# === AVERAGE GRAY DIFFERENCES ===
a1 = range(0, nframes, 1)
avgdiffs = np.array([np.average((grays[j] - grays[i])^2) for i,j in zip(a1, a1[1:])])
plt.figure(6)
plt.xlabel('Frame number')
plt.ylabel('Average gray frame difference')
plt.title('Average gray frame differences')
plt.plot(avgdiffs)
plt.show()
histdiffs = np.zeros( nframes )
# === HISTOGRAM DIFFERENCES ===
grayhs = compute_gray_histograms( grays, 10 )
h1 = range(0, nframes, 1)
histdiffs = np.array([sum(np.sqrt((grayhs[j] - grayhs[i])**2)) for i,j in zip(h1, h1[1:])])
plt.figure(7)
plt.xlabel('Frame number')
plt.ylabel('Histogram frame difference')
plt.title('Histogram frame differences')
plt.plot(histdiffs)
plt.show()