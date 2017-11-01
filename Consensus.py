"""
This code helps one perform the consensus operation on two given vectors.
Inputs: Two numpy vectors with data in PCN format.
Outputs: A matrix with the consensus operator applied on the two vectors.
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void as CV
# Corner cases: Check if both are non-void cubes, both have the same length.


def consensus(a, b):
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    # The above has been implemented in the URP file.
    result = np.zeros(a.shape)
    temp = np.logical_and(a, b).astype(int)
    for i in range(a.size):
        temp_ele = temp[i]
        temp[i] = a[i] or b[i]
        if np.count_nonzero(result) == 0:
            result = temp
        else:
            result = np.vstack((result, temp))
        temp[i] = temp_ele
    final_result = CV.check(result)
    print(final_result)
    return final_result
