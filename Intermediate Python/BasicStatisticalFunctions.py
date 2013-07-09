import numpy as np
import math
import sys
#1
def stats(arr):
    s = []
    current_min = sys.maxsize
    for i in range(0,len(arr)):
        if (arr[i] < current_min ):
            current_min = arr[i]
    s.append(current_min)
    
    current_max = 0
    for i in range(0,len(arr)):
        if (arr[i] > current_max ):
            current_max = arr[i]
    s.append(current_max)

    arr_sum = float(0)
    for i in range(0,len(arr)):
        arr_sum += arr[i]
    avg_arr = (arr_sum/len(arr))
    s.append(avg_arr)
    
    squared_diff = 0
    for i in range(0,len(arr)):
        squared_diff += (avg_arr - arr[i])**2
    variance = squared_diff / len(arr)

    std = math.sqrt(variance)
    s.append(std)

    return s

#1
n = np.array([5,6,7,14,67,8])
s = stats(n)
print (s)
