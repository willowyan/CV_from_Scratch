import numpy as np

def myImageFilter(img0, h):
    """
    Args:
        img: greyscale image.
        h: convolution filter.
    Returns
        img1: has the same size of img0.
    """
    # 1. Padding image with edge values
    h_height, h_width = h.shape
    pad_height = h_height//2
    pad_width = h_width//2

    img_padded = np.pad(img0, ((pad_height, pad_height), (pad_width, pad_width)), 'edge')

    # 2. Convolve image using kernel
    img1 = np.zeros_like(img0)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            img1[i][j] = np.sum(img_padded[i:i+h_height, j:j+h_width] * h) # Convolution

    return img1