import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    key = arr[n-1]
    current_index = n-1

    while current_index > 0 and arr[current_index-1] >= key:
        arr[current_index] = arr[current_index - 1]
        current_index -= 1
        print(*arr)

    arr[current_index] = key
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
