import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    left_diag = 0
    right_diag = 0
    arr_size = len(arr)
    i = 0
    j = arr_size - 1
    while i < arr_size and j >= 0:
        left_diag += arr[i][i]
        right_diag += arr[i][j]
        i += 1
        j -= 1
    if left_diag > right_diag:
        return left_diag - right_diag
    else:
        return right_diag - left_diag


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    # fptr.close()
