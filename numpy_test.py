# import numpy as np

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# print(arr.shape)
# print(arr*4)

# print(np.mean(arr))

# /**************************************************************
# Cratea an arr and store 3 Days data ,and there sum and use axis =0 = coloumn down
# axis=1 =row 

import numpy as np


arr = np.array([
    [10, 20, 30],   
    [15, 25, 35],  
    [20, 30, 40]    
])

print("Array:\n", arr)


print("Total Sum:", np.sum(arr))


print("Column Sum (axis=0):", np.sum(arr, axis=0))
print("Row Sum (axis=1):", np.sum(arr, axis=1))













