import numpy as np

x = np.array([1, 2])
print(x.dtype)     # int64

y = np.array([1.0, 2.0])
print(y.dtype)     # float64

z = np.array([1, 2], dtype=np.int64)
print(z.dtype)     # int64

m = np.array([[1, 2], [3, 4]], dtype=np.float64)
n = np.array([[5, 6], [7, 8]], dtype=np.float64)

# 逐元素求和
print(m + n)
print(np.add(m, n))

# 逐元素求差
print(m - n)
print(np.subtract(m, n))

# 逐元素求积
print(m * n)
print(np.multiply(m, n))

# 逐元素求商
print(m / n)
print(np.divide(m, n))

# 逐元素求平方根
print(np.sqrt(m))

# 矩阵
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 向量
c = np.array([9, 10])
d = np.array([11, 12])

# 向量的內积  对应元素相乘再相加
print(c.dot(d))
print(np.dot(c, d))

# 矩阵与向量的积
print(a.dot(c))
print(np.dot(a, c))

# 矩阵与矩阵相乘
print(a.dot(b))
print(np.dot(a, b))

e = np.array([[1, 2], [3, 4]])
f = np.array([[5, 6], [7, 8]])

# 计算所有元素的和
print(np.sum(e))
print(np.sum(f))

# 计算每一列的和
print(np.sum(e, axis=0))

# 计算每一行的和
print(np.sum(e, axis=1))

g = np.array([[1, 2], [3, 4]])
h = np.array([1, 2, 3])
print(g)
print(g.T)

# 对一维数组做转置没有效果
print(h)
print(h.T)

