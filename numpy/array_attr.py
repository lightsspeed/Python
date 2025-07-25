import numpy as np

arr = np.array([1, 2, 3])  # 1D array
matrix = np.array([[1, 2], [3, 4]])  # 2D array


print(arr.shape)  # Output: (3,) (shape of array)
print(matrix.ndim)  # Output: 2 (number of dimensions)
print(matrix.dtype)  # Output: int64 (data type)