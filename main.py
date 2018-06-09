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
    img_name = "B0009_0001.png"
    #img_name = "00000061_002.png"
    #img_name = "B0023_0001.png"
    #reads original image
    img = imageio.imread(img_name)
    plt.subplot(131)
    plt.imshow(img, cmap="gray")
    """
    img_out = average_filter(img, 5)
    img_out = 255*(img_out-np.min(img_out))/(np.max(img_out)-np.min(img_out))
    plt.subplot(132)
    plt.imshow(img_out, cmap="gray")
    """

    img_out = ft.median_filter(img, 3)
    img_out = eq.equalize(img_out, 1)
    plt.subplot(132)
    plt.imshow(img_out, cmap="gray")

    method=3
    img_out = cl.colorize_image(img, method)
    plt.subplot(133)
    plt.imshow(img_out)

    plt.show()
    imageio.imwrite('./test.png', img_out)


main()

   