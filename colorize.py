import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np


def baggage_colorize(img_in):
    
    #image dimensions
    x,y = np.shape(img_in)

    #tresholds for color mapping using the HSV system
    #mapping lighter intensity to orange, intermediate to green and high intensity to blue
    low_tresh = 150
    up_tresh = 215

    rev = 255-img_in
    img_out = np.zeros((x,y,3))


    img_out[:,:,0]=rev

    #defining hue
    #orange
    img_out[img_out<low_tresh]=47.0/360.0
    #blue
    img_out[img_out>=up_tresh]=236.0/360.0 
    #green
    img_out[img_out>=low_tresh]=100.0/360.0
    

    value = np.copy(img_in).astype(float)
   

    img_out[:,:,1]=rev/255.0*2 #saturation
    img_out[:,:,2]=img_in/255.0 #value

    img_out = mat.colors.hsv_to_rgb(img_out)

    return img_out


def hot_colormap(img_in):
    
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out = plt.cm.hot(img_in)

    return img_out

def inferno_colormap(img_in):

    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out = plt.cm.inferno(img_in)

    return img_out


def colorize_image(img_in, method):

    if (method==1):
        return baggage_colorize(img_in)

    if (method==2):
        return hot_colormap(img_in)

    if(method==3):
        return inferno_colormap(img_in)