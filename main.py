import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib as mat
import filters as ft
import equalize as eq
import colorize as cl
import sys


def main_input():

    #read test name (for output img naming)
    test_name = str(input()).rstrip()

    #read img name and read img
    img_name = str(input()).rstrip()
    img = imageio.imread(img_name)

    #smoothing filter
    smooth_method = int(input()) #method number
    smooth_n = int(input()) #filter size
    if(smooth_method == 3): #gaussian filter
        smooth_sigma = float(input())
    else:
        smooth_sigma = 0

    #sharpening filter
    sharpen_method = int(input()) #method number
    sharpen_n = int(input()) #filter size
    if(sharpen_method == 1): #laplacian filter
        sharpen_sigma = float(input())
    else:
        sharpen_sigma = 0

    #equalization
    eq_method = int(input())

    #colorizing
    color_method = int(input())


    #plots 3 images side by side: original, enhanced and colorized   
    plt.subplot(131)
    plt.imshow(img, cmap="gray")
    

    img_out = ft.smoothing_filter(img, method=smooth_method, n=smooth_n, sigma=smooth_sigma)
    img_out = ft.sharpening_filter(img, method=sharpen_method, n=sharpen_n, sigma=sharpen_sigma)

    if(eq_method != 0):

        #always normalize img if method != 0
        img_out = eq.equalize(img_out, 1)

        #calls the equalization after normalization
        if(eq_method != 1):
            img_out = eq.equalize(img_out, eq_method)


    #plot enhanced img
    plt.subplot(132)
    plt.imshow(img_out, cmap="gray")

    
    img_out = cl.colorize_image(img_out.astype(np.uint8), color_method)
    plt.subplot(133)
    plt.imshow(img_out)

    plt.show()
    imageio.imwrite('./output/'+img_name+'_'+test_name+'.png', img_out)


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
    sharpen_n = int(sys.argv[7]) #filter size
    sharpen_sigma = float(sys.argv[8])

    #equalization
    eq_method = int(sys.argv[9])

    #colorizing
    color_method = int(sys.argv[10])


    img_out = ft.smoothing_filter(img, method=smooth_method, n=smooth_n, sigma=smooth_sigma)
    img_out = ft.sharpening_filter(img, method=sharpen_method, n=sharpen_n, sigma=sharpen_sigma)

    if(eq_method != 0):

        #always normalize img if method != 0
        img_out = eq.equalize(img_out, 1)

        #calls the equalization after normalization
        if(eq_method != 1):
            img_out = eq.equalize(img_out, eq_method)
    
    img_out = cl.colorize_image(img_out.astype(np.uint8), color_method)

    imageio.imwrite('./output/'+img_name+'_'+test_name+'.png', img_out)


main()

   