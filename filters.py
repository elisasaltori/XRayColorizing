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

def calculate_gaussian_filter(n, w):
    f = np.zeros((n,n), dtype=float)
    v = np.linspace(-5, 5, n)
    for i in np.arange(n):
        for j in np.arange(n):
            x = v[i]
            y = v[-1-j]
            f[i][j] = (1/(2*np.pi*w**2)) * np.exp(-(x**2+y**2)/(2*w**2))
    f = f/np.sum(f)
    return f
def gaussian_filter(img_in, n, w):
    f = calculate_gaussian_filter(n, w)
    return frequency_filtering(img_in, f, n)