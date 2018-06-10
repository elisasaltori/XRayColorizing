import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib as mat
import filters as ft
import equalize as eq
import colorize as cl


def main():

    #reading input
    #img_name = str(input()).rstrip()
    #img_name = "B0009_0001.png"
    #img_name = "00000061_002.png"
    #img_name = "00000132_002.png"
    img_name = "B0023_0001.png"
    #img_name = "B0011_0001.png"
    #reads original image
    img = imageio.imread(img_name)
    plt.subplot(131)
    plt.imshow(img, cmap="gray")
    

    img_out = ft.smoothing_filter(img, method=2, n=3)
    img_out = ft.sharpening_filter(img, method=1, n=7, sigma=0.5)
    img_out = eq.equalize(img_out, 1)
    img_out = eq.equalize(img_out, 2)
    plt.subplot(132)
    plt.imshow(img_out, cmap="gray")

    method=3   
    img_out = cl.colorize_image(img_out.astype(np.uint8), method)
    plt.subplot(133)
    plt.imshow(img_out)

    plt.show()
    imageio.imwrite('./test.png', img_out)


main()

   