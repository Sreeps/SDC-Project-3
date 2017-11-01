"""
This code helps one perform the sharp operation.
Inputs: Two numpy vectors which need to undergo sharp operation.
Outputs: A matrix obtained after sharp operation - with any void cubes removed.
It has two functions - sharp and dis_sharp
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void as CV
# a = np.array([1 0 1 0 1 1])
# b = np.array([1 1 0 1 0 1])
# Corner cases: Check if both are non-void cubes, both have the same length.


def sharp(a, b):
    # a and b are obtained in PCN format, We need to split them.
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    # The above has been implemented in the URP file.
    b_not = np.logical_not(b).astype(int)
    temp1 = np.ones(a.shape, dtype=int)
    result = np.zeros(a.shape, dtype=int)
    for i in range(a.size):
        temp_ele = temp1[i]
        temp1[i] = b_not[i]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if np.count_nonzero(result) == 0:
            result = temp2
        else:
            result = np.vstack((result, temp2))
        temp1[i] = temp_ele
    final_result = CV.check(result)
    print(final_result)
    return final_result



def dis_sharp(a, b):
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    # The above has been implemented in the URP file.
    b_not = np.logical_not(b)
    temp1 = np.ones(a.shape, dtype=int)
    result = np.zeros(a.shape, dtype=int)
    for i in range(int(a.size/2)):
        if i == 0:
            temp_ele = temp1[0:2]
            temp1[0:2] = b_not[0:2]
        else:
            temp_ele = temp1[0:2*i+2]
            temp1[0:2*i] = b[0:2*i]
            temp1[2*i:2*i+2] = b_not[2*i:2*i+2]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if np.count_nonzero(result) == 0:
            result = temp2
        else:
            result = np.vstack((result, temp2))
        if i == 0:
            temp1[0:2] = temp_ele
        else:
            temp1[0:2*i+2] = temp_ele
    final_result = CV.check(result)
    print(final_result)
    return final_result




