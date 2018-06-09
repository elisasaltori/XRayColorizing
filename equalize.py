import numpy as np

def equalize(img_in, method):

    if (method==1):
        return normalize(img_in)
    if (method==2):
        return histrogram_equalize(img_in)

def normalize(img_in):

    return (255*(img_in-np.min(img_in))/(np.max(img_in)-np.min(img_in)))

def histrogram_equalize(img_in):
    pass
