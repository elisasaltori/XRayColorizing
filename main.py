import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib as mat


def frequency_filtering(img_in, f_matrix, n):

    x,y= np.shape(img_in)

    #fourier transforms img 
    img_out = np.fft.fft2(img_in)

    #pads filter with 0s to match img length
    f_matrix = np.pad(f_matrix,((0,x-n),(0,y-n)), 'constant', constant_values=(0, 0))
    four_f_matrix = np.fft.fft2(f_matrix)

    #element by element multiplication
    img_out = np.multiply(img_out, four_f_matrix)

    #gets output image with inverse fourier transform
    img_out = np.fft.ifft2(img_out)


    return img_out.real

def average_filter(img_in, n):
    """
    Apply an average filter of size n over img_in

    Parameters:
        img_in: input img
        n: size of filter

    Returns:
        output img
    """
    avg_filter = np.ones((n,n))
    avg_filter = avg_filter/(n*n)

    return frequency_filtering(img_in, avg_filter, n)


def median_filter(img_in, n):

    #get shape of matrix and allocate img_out
    x, y = np.shape(img_in)
    img_out = np.zeros((x, y))

    #pad img in circular manner
    pad_n = n // 2 
    img_in = np.pad(img_in, (pad_n), 'wrap')


    #get neighborhood matrices on auxiliar matrix
    aux_mat = np.zeros((x,y,n*n))
    for i in range(0, x):
        for j in range(0, y):
            aux_mat[i][j] = img_in[i:n+i, j:n+j].flatten()

    #calculates img out using collected matrices
    img_out = np.median(aux_mat, axis=2)

    return img_out
    
def colorize_image(img_in):

    x,y = np.shape(img_in)
    low_tresh = 130
    up_tresh = 200
    """
    #rgb
    img_out = np.zeros((x,y,3), dtype=np.uint8)
    """
    rev = 255-img_in
    img_out = np.zeros((x,y,3))
    #img_out[:,:,0]=rev/255.0*(2/3)
    #mapping lighter intensity to orange, intermediate to green and high intensity to blue
    
    img_out[:,:,0]=rev
    """
    #orange
    img_out[img_out<low_tresh]=47.0/360.0
    #blue
    img_out[img_out>=up_tresh]=236.0/360.0 
    #green
    img_out[img_out>=low_tresh]=100.0/360.0
    """

    #defining hue
    #orange
    img_out[img_out<low_tresh]=47.0/360.0
    #blue
    img_out[img_out>=up_tresh]=236.0/360.0 
    #green
    img_out[img_out>=low_tresh]=100.0/360.0
    

    value = np.copy(img_in).astype(float)
   

    img_out[:,:,1]=rev/255.0*2 #saturation
    img_out[:,:,2]=img_in/255.0 #value: map according to "faixa"
    #img_out[:,:,2]=value

    mask = rev
   # mask[mask==0]=0
    #mask[mask>0]=1
    #img_out[:,:,1] = np.multiply(img_out[:,:,1],mask)


    img_out = mat.colors.hsv_to_rgb(img_out)



    return img_out



def main():

    #reading input
    #img_name = str(input()).rstrip()
    img_name = "B0009_0001.png"
    #img_name = "00000061_002.png"
    img_name = "B0023_0001.png"
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

    img_out = median_filter(img, 3)
    img_out = 255*(img_out-np.min(img_out))/(np.max(img_out)-np.min(img_out))
    plt.subplot(132)
    plt.imshow(img_out, cmap="gray")

    img_out = colorize_image(img)
    plt.subplot(133)
    plt.imshow(img_out)

    plt.show()
    imageio.imwrite('./test.png', img_out)


main()

   