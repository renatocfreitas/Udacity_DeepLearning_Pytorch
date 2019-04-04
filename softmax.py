# Udacity: Deep Learning with Pytorch
#Quiz: Coding Softmax
#Let's code the formula for the Softmax function in Python.

# Duck  : 2 -> e²/(e²+e¹+e⁰) = 0.67
# Beaver: 1 -> e¹/(e²+e¹+e⁰) = 0.24
# Walrus: 0 -> e⁰/(e²+e¹+e⁰) = 0.09

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
                         # L = list of values
    expL = np.exp(L)     # calculate the exp of all elements of input array
                         # expL = list of exp values
    sumExpL = sum(expL)  # sumExpL = scalar sum of expL elements
    result = []          # result = empty list of softmax values
    for i in expL:
        result.append(i/sumExpL)
    return result        # result = list of softmax values from L

    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())

def softmax2(L):
    expL = np.exp(L)
    return np.divide (expL, expL.sum()) # expL array, expL.sum() scalar
                                        # returns array

def main():
    L = [1, 2, 3]
    O, O2 = [], []
    O = softmax(L)
    O2 = softmax2(L)
    print ('L  = ', L)
    print ('O  = ', O)
    print ('O2 = ', O2)

## main ()
if __name__ == '__main__':
    main()
