"""
This program helps one to find the cofactor w.r.t an implicant.
Inputs: Two vectors - first one is from the function and the second one w.r.t which you have to find the cofactor.
Outputs: Cofactor implicant
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np


def intersect(a, b):
    result = np.logical_and(a, b).astype(int)
    result_sum = result[::2]+result[1::2]
    if np.where(result_sum == 0).size == 0:
        return 1, result
    else:
        return 0, result


def cofactor(a, b):
    flag, result = intersect(a, b)
    b_not = np.logical_or(b)
    if flag == 0:
        return np.zeros(a.size)
    else:
        cof = np.logical_or(a, b_not)
        cof_sum = cof[::2] + cof[1::2]
        if np.where(cof_sum == 0).size == 0:
            return cof_sum
        else:
            return np.zeros(a.size)
