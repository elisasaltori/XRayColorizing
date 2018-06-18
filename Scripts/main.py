import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib as mat
import filters as ft
import equalize as eq
import colorize as cl
import sys

"""
Main file for XRayColorizing project.
Takes arguments from command line.

Usage:
    python3 main.py (test name) (input image name) (smoothing filter method)
    (smoothing filter size) (smoothing filter sigma) (sharpening filter method)
    (equalization method) (color_method)

Arguments:
    test name: added to input_image_name for the final name of the output image
    
    input image name: name (or path) of the input image
    
    smoothing filter method: an integer ranging from 1 to 3
        1 - average filter
        2 - median filter
        3 - gaussian filter
    
    smoothing filter size: a positive integer

    smoothing filter sigma: a floating point number, used for gaussian filtering

    sharpening filter method: an integer ranging from 0 to 2
        0 - no filter
        1 - laplacian filter
        2 - sobel operator

    equalization method: an integer ranging from 0 to 2
        0 - no equalization
        1 - normalization
        2 - normalization + histogram equalization

    color method: an integer ranging from 0 to 5
        0-2: baggage specialized methods
        3-5: generic colormap methods from matplotlib

"""
def main():

    #read test name (for output img naming)
    test_name = str(sys.argv[1])

    #read img name and read img
    img_name = str(sys.argv[2])
    img = imageio.imread(img_name)

    #smoothing filter
    smooth_method = int(sys.argv[3]) #method number
    smooth_n = int(sys.argv[4]) #filter size
    smooth_sigma = float(sys.argv[5])

    #sharpening filter
    sharpen_method = int(sys.argv[6]) #method number

    #equalization
    eq_method = int(sys.argv[7])

    #colorizing
    color_method = int(sys.argv[8])

    img_out = ft.smoothing_filter(img, method=smooth_method, n=smooth_n, sigma=smooth_sigma)
    img_out = ft.sharpening_filter(img, method=sharpen_method)

    if(eq_method != 0):

        #always normalize img if method != 0
        img_out = eq.equalize(img_out, 1)

        #calls the equalization after normalization
        if(eq_method != 1):
            img_out = eq.equalize(img_out, eq_method)
    
    imageio.imwrite('./output/'+img_name+'_'+test_name+'_grey.png', img_out)

    img_out = cl.colorize_image(img_out.astype(np.uint8), color_method)

    imageio.imwrite('./output/'+img_name+'_'+test_name+'.png', img_out)

main()

   