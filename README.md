# Digital Image Processing 
Assignment #3

## Tasks

1. DFT:
Write code for computing forward fourier transform, inverse fourier transform, discrete cosine transfrom and magnitude of the fourier transform. 
The input to your program is a 2D matrix of size 15X15.

  - DFT/DFT.py: Edit the functions "forward_transform", "inverse_transform", "discrete_cosine_tranform" and "magnitude", you are welcome to add more function.
  - For this part of the assignment, please implement your own code for all computations, do not use inbuilt functions like "fft" or "dft" from numpy, opencv or other libraries

  - This part of the assignment can be run using dip_hw3_dft.py (there is no need to edit this file)
    ### Usage: 
  
        python dip_hw3_dft.py


  - Any output images or files must be saved to "output/" folder (dip_hw3_dft.py automatically does this)
  

2. Frequency Filtering:
Write Code to perfrom image filtering in the frequency domain by modifying the DFT of images using different masks. Filter images using six different filters: ideal low pass (ideal_l), ideal high pass (ideal_h), butterworth low pass (butterworth_l), butterworth high pass (butterworth_h), gaussian low pass (gaussian_l) and gaussian high pass filter (gaussian_h). The input to your program is an image, name of the mask, cuttoff frequency and order(only for butterworth filter).

- DFT/Filtering.py:
  - \__init__(): Will intialize the required variable for filtering (image, mask function, cutoff, order). There is no need to edit this function  
  - get_mask_freq_pass_filter(): There are six function definitions one for each of the filter. write your code to generate the masks for each filter here. 
  - filtering(): Write your code to perform image filtering here. The steps can be used as a guideline for filtering. All the variable have already been intialized and can be used as self.image, self.cutoff, etc. The varaible self.filter is a handle to each of the six fitler functions. You can call it using self.filter(shape, cutoff, ...)
    - The function returns three images, filtered image, magnitude of the DFT and magnitude of filtered dft 
    - To be able to display magnitude of the DFT and magnitude of filtered dft, perform a logrithmic compression and convert the value to uint8
  - post_process_image(): After fitlering and computing the inverse DFT, scale the image pixels to view it. You can write code to do a full contrast stretch here and in some cases you would also have to take a negative of the image. 
-  For this part of the assignment, You can use inbuilt functions to compute the fourier transform
- For example, you are welcome to use fft and dft libraries that are available in numpy and opencv

- This part of the assignment can be run using dip_hw3_filter.py (there is no need to edit this file)
  ### Usage: 

      ./dip_hw3_filter -i image -m ideal_l -c 50
      python dip_hw3_filter.py -i image -m ideal_l -c 50
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Any output images or files must be saved to "output/" folder (dip_hw3_filter.py automatically does this)


Two images are provided for testing: Lenna.png and Lenna0.jpg

