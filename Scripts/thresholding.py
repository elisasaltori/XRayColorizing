"""

"""
import numpy as np
import matplotlib.pyplot as plt

def otsu_method(img_in):

    print("beginning otsu")
    #building cumulative histogram
    hist, bin_edg = np.histogram(img_in, 256, (0,256))
    hist = hist/np.size(img_in) #probability

    level = 0
    w0 = 0
    sum0 = 0
    max_var = 0
    sum1 = np.sum(np.multiply(list(range(0,256)), hist))

    for i in range(0,256):
        w0 = w0 + hist[i];
        w1 = 1 - w0
        if(w0==0 or w1 == 0):
            continue
        sum0 = sum0 + i * hist[i]
        m1 = (sum1 - sum0) /w1
        var = w0 * w1 * ((sum0/w0) - m1) * ((sum0/w0) - m1)
        if(var > max_var):
            level = i
            max_var = var

    print(level)
    return level

def otsu_method_three(img_in):
    """
    Multi otsu method for 3 levels.

    Parameters:
        img_in - input image
    Returns:
        level1, level2: the thresholds that maximize inter class variance
    """

    #building probability histogram
    hist, bin_edg = np.histogram(img_in, 256, (0,256))
    hist = hist/np.size(img_in) #probability
    hist[0] =0

    #initializing variables
    level1 = 0
    level2 = 0
    w0 = 0
    w1 = 0
    sum0 = 0
    sum1 = 0
    max_var = 0

    mt = np.sum(np.multiply(list(range(0,256)), hist))

    #main loop for finding thresholds
    #outer loop: first threshold
    #inner loop: second threshold
    for i in range(0,256):

        w0 = w0 + hist[i] #cumulative probability pi
        sum0 = sum0 + i * hist[i] # sum(pi * i)

        m0 = sum0/w0 #mean sum(pi*i)/pi
        
        w1 = 0
        sum1 = 0

        for j in range(i+1, 256):

            w1 = w1 + hist[j] #cumulative probability pi
            sum1 = sum1 + j * hist[j] # sum(pi * i)

            m1 = sum1/w1 #mean sum(pi*i)/pi
            
            w2 = 1 - w1 - w0
            if(w2 <= 0):
                break

            sum2 = mt - sum1 - sum0
            m2 = sum2/w2

            #inter class variance
            var = w0 *(m0-mt)*(m0-mt)+w1*(m1-mt)*(m1-mt)+w2*(m2-mt)*(m2-mt) 

            #if current variance is larger than max_var
            if(var > max_var):
       
                level1 = i
                level2 = j
                max_var = var


    return level1, level2

