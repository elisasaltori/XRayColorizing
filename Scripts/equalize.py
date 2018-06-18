"""
Contains normalization and equalization methods
"""
import numpy as np


def equalize(img_in, method):
    """
    Normalize or histogram equalize an image

    input:
        img_in: input image
        method: number of desired method
    """
    
    if (method==1):
        return normalize(img_in)
    if (method==2):
        return histrogram_equalize(img_in)

def normalize(img_in):
    """
    Normalize an image

    Parameters:
        img_in: input image
    """
    img_in = img_in.astype(float)

    return (255*(img_in-np.min(img_in))/(np.max(img_in)-np.min(img_in))).astype(np.uint8)

def histrogram_equalize(img_in):
    """
    Equalizes an image using a histogram

    Keyword arguments:
        img: input img
    """

    #building cumulative histogram
    hist, bin_edg = np.histogram(img_in, 256, (0,256))
    hist = np.cumsum(hist)
    
    x,y = np.shape(img_in)
    size = np.size(img_in)

    #equalizing
    for i in range(0,x):
        for j in range(0,y):
            img_in[i][j]=255*hist[int(img_in[i][j])]/(size)


    return img_in