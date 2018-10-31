# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv
import numpy as np
import math as math

class Filtering:
    image = None
    filter = None
    cutoff = None
    order = None

    def __init__(self, image, filter_name, cutoff, order=0):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        filter_name: the name of the mask to use
        cutoff: the cutoff frequency of the filter
        order: the order of the filter (only for butterworth
        returns"""
        self.image = image
        if filter_name == 'ideal_l':
            self.filter = self.get_ideal_low_pass_filter
        elif filter_name == 'ideal_h':
            self.filter = self.get_ideal_high_pass_filter
        elif filter_name == 'butterworth_l':
            self.filter = self.get_butterworth_low_pass_filter
        elif filter_name == 'butterworth_h':
            self.filter = self.get_butterworth_high_pass_filter
        elif filter_name == 'gaussian_l':
            self.filter = self.get_gaussian_low_pass_filter
        elif filter_name == 'gaussian_h':
            self.filter = self.get_gaussian_high_pass_filter

        self.cutoff = cutoff
        self.order = order


    def get_ideal_low_pass_filter(self, shape, cutoff):
        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""
        (p, q) = shape
        mask = np.array([[1 if math.sqrt(math.pow((u - (p / 2)), 2) + math.pow((v - (q / 2)), 2)) <= cutoff else 0 for v in range(q)] for u in range(p)])
        return mask


    def get_ideal_high_pass_filter(self, shape, cutoff):
        """Computes a Ideal high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        mask = 1 - self.get_ideal_low_pass_filter(shape, cutoff)
        return mask

    def get_butterworth_low_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth low pass mask"""

        (p, q) = shape
        mask = np.array([[(1 / (1 + math.pow((math.sqrt(math.pow((u - (p / 2)), 2) + math.pow((v - (q / 2)), 2))/cutoff), 2 * order))) for v in range(q)] for u in range(p)])

        return mask

    def get_butterworth_high_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        mask = 1 - self.get_butterworth_low_pass_filter(shape, cutoff, order)
        return mask

    def get_gaussian_low_pass_filter(self, shape, cutoff):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""

        (p, q) = shape
        mask = np.array([[math.exp(-1 * (math.pow(math.sqrt(math.pow((u - (p / 2)), 2) + math.pow((v - (q / 2)), 2)), 2)/(2 * math.pow(cutoff, 2)))) for v in range(q)] for u in range(p)])
        return mask

    def get_gaussian_high_pass_filter(self, shape, cutoff):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        mask = 1 - self.get_gaussian_low_pass_filter(shape, cutoff)
        return mask

    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage)
        """

        min_gray_level = np.min(image)
        max_gray_level = np.max(image)
        (h, w) = image.shape

        fsimage = np.array([[(((255 - 1) / (max_gray_level - min_gray_level)) * (image[i][j] - min_gray_level)) for j in range(w)] for i in range(h)], dtype=np.uint8)

        return fsimage


    def filtering(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT        
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape, cutoff, order)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        take negative of the image to be able to view it (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8 
        """

        if self.order > 0:
            mask = self.filter(self.image.shape, self.cutoff, self.order)
        else:
            mask = self.filter(self.image.shape, self.cutoff)

        image_fft = np.fft.fft2(self.image)
        shifted_fft = np.fft.fftshift(image_fft)
        compressed_fft = np.uint8(np.log(np.absolute(shifted_fft)) * 10)

        filtered_dft = shifted_fft * mask
        compressed_filtered_fft = np.uint8(np.log(np.absolute(filtered_dft)) * 10)

        inverse_shift = np.fft.ifftshift(shifted_fft)
        inverse_fft = np.fft.ifft2(inverse_shift)
        magnitude = np.absolute(inverse_fft)
        fsimage = self.post_process_image(magnitude)

        return [fsimage, compressed_fft, compressed_filtered_fft]
