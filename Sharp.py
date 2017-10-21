"""
This code helps one perform the sharp operation.
Inputs: Two numpy vectors which need to undergo sharp operation.
Outputs: A matrix obtained after sharp operation - with any void cubes removed.
It has two functions - sharp and dis_sharp
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np

# a = np.array([1 0 1 0 1 1])
# b = np.array([1 1 0 1 0 1])
# Corner cases: Check if both are non-void cubes, both have the same length.


def sharp(a, b):
    # a and b are obtained in PCN format, We need to split them.
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    b_not = np.logical_not(b)
    temp1 = np.ones(a.shape)
    result = np.zeros(a.shape)
    for i in range(a.size):
        temp_ele = temp1[i]
        temp1[i] = b_not[i]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if result.size == 0:
            result = temp2
        else:
            np.vstack((result, temp2))

        temp1[i] = temp_ele
    final_result = np.logical_or(result[::2, :], result[1::2, :]).astype(int)
    final_result_sum = final_result[:, ::2] + final_result[:, 1::2]
    del_rows = np.array([])
    for i in range(final_result.shape[0]):
        if np.where(final_result_sum[i] == 0).size != 0:
            del_rows = np.append(del_rows, i)
    final_result = np.delete(final_result, del_rows, axis=0)
    return final_result


def dis_sharp(a, b):
    # TODO: Convert the string representation used into separate digits and then convert those to numbers.
    b_not = np.logical_not(b)
    temp1 = np.ones(a.shape)
    result = np.zeros(a.shape)
    for i in range(a.size):
        temp_ele = temp1[0:i + 1]
        temp1[0:i] = b[0:i]
        temp1[i] = b_not[i]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if result.size == 0:
            result = temp2
        else:
            np.vstack((result, temp2))

        temp1[0:i+1] = temp_ele
    final_result = np.logical_or(result[::2, :], result[1::2, :]).astype(int)
    final_result_sum = final_result[:, ::2] + final_result[:, 1::2]
    del_rows = np.array([])
    for i in range(final_result.shape[0]):
        if np.where(final_result_sum[i] == 0).size != 0:
            del_rows = np.append(del_rows, i)
    final_result = np.delete(final_result, del_rows, axis=0)
    return final_result




