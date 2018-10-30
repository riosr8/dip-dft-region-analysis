# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np
import math
import cmath

class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        (h, w) = matrix.shape
        fft = np.array([[sum([(matrix[i][j] * cmath.exp(-1 * cmath.sqrt(-1) * ((2*cmath.pi)/h) * (u*i + v*j))) for i in range(h) for j in range(w)]) for v in range(w)] for u in range(h)])

        # fft_matrix = np.fft.fft2(matrix)
        # print(fft)
        # print('===================================================================================================================================================')
        # print(fft_matrix)

        return fft

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""

        (h, w) = matrix.shape
        ift = np.array([[sum([(matrix[u][v] * cmath.exp(cmath.sqrt(-1) * ((2 * cmath.pi) / h) * ((u * i) + (v * j)))) for u in range(h) for v in range(w)]) for j in range(w)] for i in range(h)])

        # not sure why it is not the same...
        # ift_builtin = np.fft.ifft2(matrix)

        return ift


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""

        (h, w) = matrix.shape
        dct = np.array([[sum([(matrix[i][j] * math.cos(((2*math.pi)/h) * (u*i + v*j))) for i in range(h) for j in range(w)]) for v in range(w)] for u in range(h)])

        # dct_builtin = fftpack.dct(matrix)

        return dct


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""

        (h, w) = matrix.shape
        dft_magnitude = np.array([[sum([(matrix[i][j] * (math.cos(((2*math.pi)/h) * (u*i + v*j)) - cmath.sqrt(-1)*cmath.sin(((2*math.pi)/h) * (u*i + v*j)))) for i in range(h) for j in range(w)]) for v in range(w)] for u in range(h)])

        return dft_magnitude