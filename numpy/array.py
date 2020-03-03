import numpy as np

a = np.array([1, 2, 3])   # create a rank 1 array 一维数组
print(type(a))    # <class 'numpy.ndarray'>
print(a.shape)    # (3,)
print(a[0], a[1], a[2])   # 1 2 3
a[0] = 5
print(a)   # [5, 2, 3]

b = np.array([[1, 2, 3], [4, 5, 6]])   # create a rank 2 array 二维数组
print(b.shape)    # (2, 3)
print(b[0, 0], b[0, 1], b[1, 0])   # 1 2 4

c = np.zeros((2, 2))   # 创建两行两列的全0数组
print(c)    # [[0., 0.]
            #  [0., 0.]]

d = np.ones((1, 2))  # 创建一行二列的全1数组
print(d)    # [[1., 1.]]

e = np.full((2, 2), 7)   # 创建二行二列全为7的数组
print(e)     # [[7, 7]
             #  [7, 7]]
e[0, 1] = 5
print(e)

f = np.eye(2)   # 创建2*2的单位矩阵
print(f)      # [[1., 0.]
              #  [0., 1.]]
g = np.random.random((2, 2))   # 创建2行2列的随机数组
print(g)

h = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(h)
i = h[:2, 1:3]  # 前两行,一二列,前闭后开
print(i)

# 数组的一个切片是对相同数据的一个视图,
# 因此对切片的修改将改变原始数据
print(h[0, 1])   # 2
i[0, 0] = 77   # i[0, 0] is the same piece of data as a[0, 1]
print(h[0, 1])   # 77

j = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row_r1 = j[1, :]  # 整数索引和切片索引混合,产生一维数组
row_r2 = j[1:2, :]  # 两个切片索引,维数不变
print(row_r1, row_r1.shape)   # [5 6 7 8] (4,)
print(row_r2, row_r2.shape)     # [[5 6 7 8]] (1, 4)

col_r1 = j[:, 1]  # 整数索引与切片索引混合
col_r2 = j[:, 1:2]
print(col_r1, col_r1.shape)  # [2 6 10] (3,)
print(col_r2, col_r2.shape)  # [[2]
                             #  [6]
                             #  [10]]  (3, 1)

k = np.array([[1, 2], [3, 4], [5, 6]])
print(k[[0, 1, 2], [0, 1, 0]])  # a [1 4 5] 整数数组索引
print(np.array([k[0, 0], k[1, 1], k[2, 0]]))  # [1 4 5] 与a行效果相同

print(k[[0, 0], [1, 1]])  # b [2 2]  整数索引可是使用数组中的相同元素,例子中使用k[0,1]两次
print(np.array([k[0, 1], k[0, 1]]))   # [2 2] 效果同b行

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(m)
n = np.array([0, 2, 0, 1])
print(m[np.arange(4), n])  # [ 1 6 7 11] 使用n中定义的索引在m的每一行取出一个元素
m[np.arange(4), n] += 10  # 使用n中定义的索引改变m中的某些值
print(m)

o = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (o > 2)   # 找出数组中大于2的元素
                     # 返回Boolean结果数组
                     # 形状和o相同
print(bool_idx)
print(o[bool_idx])  # [3 4 5 6]
print(o[o > 2])  # [3 4 5 6] 效果同上




