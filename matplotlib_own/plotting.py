# @Time : 2020/3/4 16:27 
# @Author : hqjiang
# @File : plotting.py

import numpy as np
import matplotlib.pyplot as plt

# compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)   # 从0 ~ 3 * pi 的距离内,每隔0,1产生一个点
y = np.sin(x)

# 画图
# plt.plot(x, y)
# plt.show()  # you must call plt.show() to make graphics appear

y_cos = np.cos(x)

plt.plot(x, y)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
