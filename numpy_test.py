import numpy as np

# Array（数组）
# rank
# a = np.array([1,2,3])
# type(a)
# <class 'numpy.ndarray'>
# a.shape
# (3,)
# a = a.reshape(1,-1)
# a.shape
# (1, 3)

# ###############################################
# a = np.arange(1, 7).reshape(3, -1)
# # a.shape
# a[2, 0] = 55

# ###############################################
# a = np.zeros((3, 2))
# a = np.ones((2, 3))
# a = np.full((2, 3), 1)
# a = np.eye(3, dtype=int)
# a = np.random.random((3, 4))
# a = 5 * np.random.random_sample((3, 2)) - 5


# Indexing,Slicing
# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])
# a[-2:, 1:3]
# array([[6,7],[10,11]])
# 两个结果一样，都为7
# a[1,-2]
# a[1][-2]
# b = a[-2:, 1:3]
# 1到3行第2列都+10
# a[np.arange(3), 1] += 10
# a[np.arange(3), [1, 1, 1]] += 10
# a[[0, 1, 2], [1, 1, 1]] += 10
# a[:3, 1] += 10
# result_index = a > 10
# a[result_index]
# a[a>10]


# ###############################################
# dtype
# a = np.array([1, 2], dtype=np.int16)
# a = np.array([1, 2.0], dtype=int)
# b = np.array(a, dtype=float)

# ###############################################
# 数学运算
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [6, 5]])
# a+b
# np.add(a, b)
# a - b
# np.subtract(a, b)
# a * b
# np.multiply(a, b)
# a / b
# np.divide(a, b)
# np.sqrt(a)
# np.square(a)

# b = np.array([[1, 2, 3], [4, 5, 6]])
# 矩阵乘法
# a.dot(b)
# np.dot(a,b)

# ###############################################
# 常用函数
# a = np.array([[1, 2], [3, 4]])
# a.sum()
# np.sum(a)
# np.sum(a, axis=0)
# np.sum(a, axis=1)
# a.mean()
# np.mean(a)
# np.tile(a, 2)
# np.tile(a,(2,3))
# np.argsort(a)

# 矩阵转置
# a.T
# a.transpose()

# ###############################################
# 广播
a = np.array([[1, 2, 3],
              [2, 3, 4],
              [12, 31, 22],
              [2, 2, 2]])

b = np.arange(1, 4).reshape(1, 3)
# a+b 广播操作，列数目要相等
# a + b
