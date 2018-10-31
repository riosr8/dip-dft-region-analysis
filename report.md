# Report

## DFT.py

For this part of the assignment we have been tasked with completing four functions to compute the forward fourier transform, inverse fourier transform, discrete cosine fourier transform, and the magnitude of a DFT. This was done by implementing all of the corresponding equations using the math and cmath modules for the mathematical operations. A similar approach using list comprehensions was used for all functions implemented where I iterate through each cell in the resulting matrix. At each entry, I am summing up the result of the corresponding function (i.e FFT, IFT, DCT, Magnitude of DFT) by iterating through the entire input matrix within another list comprehension and storing the result. 


##Filtering.py

For this part of the assignment we have been tasked with completing six functions that performed low and high ideal pass, butterworth, and gaussian filters and returned a mask based on the result. For the butterworth and gaussian low pass filters I have have created a numpy matrix using list comprehensions that use the shape for iteration and at each location storing the result of the computation. This is in exception to the ideal low pass filter whose value is 1 or 0 depending on the value of the distance function being less than or equal to the cutoff. If the distance between the point (u,v) in the frequency domain and the center was less than or equal to the cutoff then a 1 was placed in the location (u,v), otherwise a 0 was placed. To get the mask for the high pass filters, I simply subtracted the mask of the corresponding low pass filter from 1.

In the filtering function, I have made use of the inbuilt fft functions. I first select the appropriate mask using the given handle depending on the argument given for the mask to be used. I then take the original image and compute the fft and then shift the fft to center the low frequencies. The shifted fft is then compressed so that the saved image may be visible. I have then filtered the shifted fft by multiplying it with the selected mask, and compressing this filtered fft so that it may be visible when saved. Finally, I applied an inverse fft shift operation followed by an inverse fft operation on the filtered fft. To transform the resulting inverse fft to a meaningful image I have calculated its magnitude and performed a full scale contrast stretch as a post processing step.
