"""
This code helps one perform the consensus operation on two given vectors.
Inputs: Two numpy vectors with data in PCN format.
Outputs: A matrix with the consensus operator applied on the two vectors.
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
# Corner cases: Check if both are non-void cubes, both have the same length.


def consensus(a, b):
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    result = np.zeros(a.shape)
    temp = np.logical_and(a, b).astype(int)
    for i in range(a.size):
        temp_ele = temp[i]
        temp[i] = a[i] or b[i]
        if result.size == 0:
            result = temp
        else:
            np.vstack((result, temp))
        temp[i] = temp_ele
    final_result = np.logical_or(result[::2, :], result[1::2, :]).astype(int)
    final_result_sum = final_result[:, ::2] + final_result[:, 1::2]
    del_rows = np.array([])
    for i in range(final_result.shape[0]):
        if np.where(final_result_sum[i] == 0).size != 0:
            del_rows = np.append(del_rows, i)
    final_result = np.delete(final_result, del_rows, axis=0)
    return final_result
