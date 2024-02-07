import numpy as np

# 1번 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

numpy_1 =  np.concatenate((a,b),axis=0)
print(numpy_1)

# 2번

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

numpy_2 =  np.concatenate((a,b),axis=0)
print(numpy_2)

# 3번

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

numpy_3 =  np.concatenate((a,b),axis=1)
print(numpy_3)

# 4번

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])

a_new = a[:, np.newaxis]

numpy_4 =  np.concatenate((a_new,b),axis=0)
print(numpy_4)

# 5번 