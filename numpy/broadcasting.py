# @Time : 2020/3/4 9:56 
# @Author : hqjiang
# @File : broadcasting.py

# broadcasting-广播机制,按位运算

import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # create an empty matrix with the same shape as x

# add v to each row of the matrix x with an explicit-明显的,显示的 loop,显示循环
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

# when the matrix x is  veryr large, explicit loop in python could be slow
yy = np.empty_like(x)
vv = np.tile(v, (4, 1))  # stack 4 copies of v on top of each other
print(vv)
test = np.tile(v, (4, 3))  # 列重复3次
# print(test)
yy = x + vv
print(yy)

# 广播机制
yyy = np.empty_like(x)
yyy = x + v   # add v to each row of x using broadcasting
print(yyy)

m = np.array([1, 2, 3])
n = np.array([4, 5])
print(m, n)
print(np.reshape(m, (3, 1)))   # 将m转换为三行一列(3, 1) * (1, 2) => (3, 2)
print(np.reshape(m, (3, 1)) * n)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a + m)  # 将m 转换为(2, 3) 逐元素相加

# (2, 3) + (1, 2) => (3, 2) + (1, 2)
# => (3, 2) + (3, 2) => (3, 2) => (2, 3)
print((a.T + n).T)

# (2, 3) + (1, 2) => (2, 3) + (2, 1)
# => (2, 3) + (2, 3) => (2, 3)
print(a + np.reshape(n, (2, 1)))

print(a * 2)
