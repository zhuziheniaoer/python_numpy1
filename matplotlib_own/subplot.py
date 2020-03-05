# @Time : 2020/3/4 16:41 
# @Author : hqjiang
# @File : subplot.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# set up a subplot grid that has height 2
# and width 1
# 三个参数分别代表: 行数 列数 索引值
plt.subplot(2, 1, 1)  # 两行一列第一个
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(2, 1, 2)  # 两行一列第二个
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()
