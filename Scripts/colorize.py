import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import thresholding as tr

def baggage_colorize_fixed(img_in):
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

    img_out = mat.colors.hsv_to_rgb(img_out)

    return img_out


def baggage_colorize(img_in):
    
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

def sine_colormap(img_in):
    
    x,y = np.shape(img_in)
    img_out = np.zeros((x,y,3)).astype(np.uint8)
    img_out[:,:,0] = np.sin(2*np.pi*img_out/255)+(np.pi/2) 
    img_out[:,:,1] = np.sin(2*np.pi*img_out/255)+(np.pi/4)
    img_out[:,:,2] = np.sin(2*np.pi*img_out/255)+(np.pi/6)  

    return img_out

def colorize_image(img_in, method):

    if (method==0):
        return baggage_colorize_fixed(img_in)

    if (method==1):
        return baggage_colorize(img_in)

    if (method==2):
        return hot_colormap(img_in)

    if(method==3):
        return inferno_colormap(img_in)