from PIL import Image, ImageDraw
import numpy as np
import csv
import math
import random

def ReadKeys(image):
    im = Image.open(image+'.pgm').convert('RGB')
    keypoints = []
    descriptors = []
    first = True
    with open(image+'.key','r') as f:
        reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC,skipinitialspace = True)
        descriptor = []
        for row in reader:
            if len(row) == 2:
                assert first, "Invalid keypoint file header."
                assert row[1] == 128, "Invalid keypoint descriptor length in header (should be 128)."
                count = row[0]
                first = False
            if len(row) == 4:
                keypoints.append(np.array(row))
            if len(row) == 20:
                descriptor += row
            if len(row) == 8:
                descriptor += row
                assert len(descriptor) == 128, "Keypoint descriptor length invalid (should be 128)."
                #normalize the key to unit length
                descriptor = np.array(descriptor)
                descriptor = descriptor / math.sqrt(np.sum(np.power(descriptor,2)))
                descriptors.append(descriptor)
                descriptor = []
    assert len(keypoints) == count, "Incorrect total number of keypoints read."
    print("Number of keypoints read:", int(count))
    return [im,keypoints,descriptors]

def AppendImages(im1, im2):
    """Create a new image that appends two images side-by-side.

    The arguments, im1 and im2, are PIL images of type RGB
    """
    im1cols, im1rows = im1.size
    im2cols, im2rows = im2.size
    im3 = Image.new('RGB', (im1cols+im2cols, max(im1rows,im2rows)))
    im3.paste(im1,(0,0))
    im3.paste(im2,(im1cols,0))
    return im3

def DisplayMatches(im1, im2, matched_pairs):
  
    im3 = AppendImages(im1,im2)
    offset = im1.size[0]
    draw = ImageDraw.Draw(im3)
    for match in matched_pairs:
        draw.line((match[0][1], match[0][0], offset+match[1][1], match[1][0]),fill="red",width=2)
    im3.show()
    return im3

def match(image1,image2):

    im1, keypoints1, descriptors1 = ReadKeys(image1)
    im2, keypoints2, descriptors2 = ReadKeys(image2)

    # Select a threshold that gives mostly good matches for the images “scene” and “book.” 
    threshold = 0.82

    # Repeat the random selection _ times and then select the largest consistent subset that was found
    repititions = 600
    
    # Consider all possible matched paires

    matched_pairs = []

    m = {}

    for r1 in range(len(descriptors1)):
        print(r1)
        for r2 in range(len(descriptors2)):
            # measure its angle to each vector from the second matrix. 
            dp = np.dot(descriptors1[r1], descriptors2[r2])
            # this is the inverse cosine (math.acos(x) function in Python) of the dot product of the vectors
            a = math.acos(dp)
            m[a] = (r1, r2)
       # use sorted to find the two smallest values in a list 
        sorted_m = sorted(m)
        # two smallest angles
        first_a = sorted_m[0]
        second_a = sorted_m[1]
        # compare the smallest (best) match angle to the second-best angle. A match should be selected only if this ratio is below a threshold. 
        ratio = first_a/second_a
        if (ratio) < threshold:
            # The vector with the smallest angle is the nearest neighbor (i.e., the best match)
            ind1, ind2 = m[first_a]
            matched_pairs.append([keypoints1[ind1], keypoints2[ind2]])
        m = {}
    mathched_pairs = RANSAC(matched_pairs, keypoints1, keypoints2, repititions)
    #
    # displays correct matches by comparing the keypoint descriptor vectors.
    im3 = DisplayMatches(im1, im2, matched_pairs)
    return im3

def RANSAC(matched_pairs, keypoints1, keypoints2, repititions):
    subset = []
    best = []
    # select just one match at random, and then check all the other matches for consistency with it
    for r in range(repititions):
        rm1, rm2 = random.choice(matched_pairs)
        subset.append([rm1, rm2])
        for m1, m2 in matched_pairs:
            # scale and orientation
            sc_r1 = rm1[2]
            or_r1 = rm1[3]
            sc_r2 = rm2[2]
            or_r2 = rm2[3]
            sc1 = m1[2]
            or1 = m1[3]
            sc2 = m2[2]
            or2 = m2[3]
        # check that the change of orientation (30 degree)
        if(abs(or_r1-or_r2-math.pi/6) < abs(or1-or2)
           and abs(or_r1-or_r2+math.pi/6) > abs(or1-or2)
        # check that the change of scale agrees within plus or minus 50%
           and abs(sc_r1-sc_r2)-abs(sc_r1-sc_r2)*0.5 < abs(sc1-sc2)
           and abs(sc_r1-sc_r2)+abs(sc_r1-sc_r2)*0.5 > abs(sc1-sc2)):
            subset.append([m1, m2])
        if((len(subset)-len(best)) > 0):
            best = subset
        subset = []
    return best

#Test run...
match('library2','library')