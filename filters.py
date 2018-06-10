import numpy as np

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
    
def smoothing_filter(img_in, method, n):

    if(method==1):
        return average_filter(img_in, n)
    if(method==2):
        return median_filter(img_in, n)

def sharpening_filter(img_in, method, n, sigma=0.5):

    if(method==1):
        return laplacian_filter(img_in, n, sigma)

    if(method==2):
        return sobel_op(img_in)

def laplacian_filter(img_in, n, sigma):
    """
    Create a matrix corresponding to a Laplacian of Gaussian filter

    Arguments:
        sigma: standard deviation
        n: size of the filter (nxn matrix)
    """

    f_matrix = np.zeros((n,n))

    #index of central position in matrix
    c_pos = int(n/2)
    if(n%2==0): #even-sized matrix
        c_pos = c_pos-0.5 #center is between indices

    #how much 1 unit displacement in index is worth in the "circle"
    inc_factor = 5.0/(c_pos)

    #begins building the filter
    for i in range(0, n):
        for j in range(0, n):
            f_matrix[i][j] = ( (1 - ( (inc_factor*(i-c_pos))**2 + ((inc_factor*(j-c_pos))**2) ) / (2*sigma*sigma) ) 
            * np.exp(-1*( (inc_factor*(i-c_pos))**2 + ((inc_factor*(j-c_pos))**2) )/(2*sigma*sigma)) )

    #final filter operation
    f_matrix *= -1.0/(np.pi*(sigma**4))

 
    #normalizing filter -1*(positives/negatives) for negative values
    f_matrix[f_matrix<0] = f_matrix[f_matrix<0] *( -1.0*np.sum(f_matrix[f_matrix>0])/np.sum(f_matrix[f_matrix<0]) )


    return img_in+frequency_filtering(img_in, f_matrix, n)



def sobel_op(img_in):
    """
    Apply the sobel operator to given img. 

    Arguments:
        img_in: input img
    """

    #dimensions of in matrix
    x, y = np.shape(img_in)

    #filter used for the sobel operator
    fx = np.asarray( [ [1, 0, -1], [2, 0, -2], [1, 0, -1] ])
    fy = np.asarray( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ])

    #pads img in order to apply filters
    pad_img = np.pad(img_in, ((1,1),(1, 1)), 'constant', constant_values=(0, 0))

    #intermediate matrices
    ix = np.zeros((x,y))
    iy = np.zeros((x,y))

    #applies filters to input img
    for i in range(0, x):
        for j in range(0, y):
            ix[i][j] = np.sum(np.multiply(pad_img[i:i+3, j:j+3], fx))
            iy[i][j] = np.sum(np.multiply(pad_img[i:i+3, j:j+3], fy)) 


    #combines both intermediate imgs
    img_out = img_in+ np.power( (np.power(ix, 2)) + np.power(iy, 2), 0.5 )

    return img_out