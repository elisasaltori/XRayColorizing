import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
from . import thresholding as tr

def baggage_colorize_fixed(img_in):
    """
    Colorize an image using predefined thresholds.
    Colors:
        blue: higher density objects
        green: medium density objects
        orange: low density objects

    input:
        img_in - input image
    """
    #image dimensions
    x,y = np.shape(img_in)

    #thresholds for color mapping using the HSV system
    #mapping lighter intensity to orange, intermediate to green and high intensity to blue
    #predefined thresholds
    low_thresh = 150
    up_thresh = 215

    rev = 255-img_in
    img_out = np.zeros((x,y,3))


    img_out[:,:,0]=rev

    #defining hue
    #orange
    img_out[img_out<low_thresh]=47.0/360.0
    #blue
    img_out[img_out>=up_thresh]=236.0/360.0 
    #green
    img_out[img_out>=low_thresh]=100.0/360.0
    

    value = np.copy(img_in).astype(float)
   

    img_out[:,:,1]=rev/255.0*1.5 #saturation
    img_out[:,:,2]=img_in/255.0*0.95 #value

    img_out[img_out>1]=1

    img_out = mat.colors.hsv_to_rgb(img_out)

    return img_out


def baggage_colorize(img_in):
    """
    Colorize an image using thresholds defined by a 3 level multi otsu method.
    Colors:
        blue: higher density objects
        green: medium density objects
        orange: low density objects

    input:
        img_in - input image
    """

    #image dimensions
    x,y = np.shape(img_in)

    #thresholds for color mapping using the HSV system
    #mapping lighter intensity to orange, intermediate to green and high intensity to blue
    #uses otsu method for defining thresholds
    low_thresh, up_thresh = tr.otsu_method_three(img_in)

    rev = 255-img_in
    img_out = np.zeros((x,y,3))


    img_out[:,:,0]=rev

    #defining hue
    #orange
    img_out[img_out<low_thresh]=47.0/360.0
    #blue
    img_out[img_out>=up_thresh]=236.0/360.0 
    #green
    img_out[img_out>=low_thresh]=100.0/360.0
    

    value = np.copy(img_in).astype(float)
   

    img_out[:,:,1]=rev/255.0*1.5 #saturation
    img_out[:,:,2]=img_in/255.0*0.95 #value

    img_out[img_out>1]=1

    img_out = mat.colors.hsv_to_rgb(img_out)

    return img_out


def hot_colormap(img_in):
    """
    Colorize an image using the matplotlib colormap Hot.
    Hot is a sequencial colormap.

    input:
        img_in - input image
    """
    
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out = plt.cm.hot(img_in)

    return img_out

def inferno_colormap(img_in):
    """
    Colorize an image using the matplotlib colormap Inferno.
    Inferno is a perceptually uniform colormap.

    input:
        img_in - input image
    """
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out = plt.cm.inferno(img_in)

    return img_out

def spectral_colormap(img_in):
    """
    Colorize an image using the matplotlib colormap Spectral.
    Spectral is a diverging colormap.

    input:
        img_in - input image
    """
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out = plt.cm.Spectral(img_in)

    return img_out


def sine_colormap(img_in):
    """
    Colorize an image using an RGB sine colormap which highlights high-density
    threats. As seen on the masters thesis by Kannan Kase (2002)

    input:
        img_in - input image
    """    
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3))
   
    img_out[:,:,0] = np.fabs((np.sin(0.666667*np.pi*img_in/255-0.02*np.pi)))
    img_out[:,:,1] = np.fabs((np.sin(0.666667*np.pi*img_in/255-1.2*np.pi)))
    img_out[:,:,2] = np.fabs((np.sin(0.666667*np.pi*img_in/255-1.3333*np.pi)))
    
    return img_out


def colorize_image(img_in, method):
    """
    Colorize a grayscale image using the method selected.
    Methods 0-2 are specialized for use in baggages.
    Methods 3-5 are generic and can be used for any image.

    Parameters:
        img_in: input image
        method: number of desired method

    Output:
        colorized image
    """
    if (method==0):
        return baggage_colorize_fixed(img_in)

    if (method==1):
        return baggage_colorize(img_in)

    if(method==2):
        return sine_colormap(img_in)

    if (method==3):
        return hot_colormap(img_in)

    if(method==4):
        return inferno_colormap(img_in)

    if(method==5):
        return spectral_colormap(img_in)
   