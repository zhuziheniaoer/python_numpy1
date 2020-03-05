# @Time : 2020/3/4 16:06 
# @Author : hqjiang
# @File : distance_points.py

import numpy as np
from scipy.spatial.distance import pdist, squareform

x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

# x每个点与x 间的距离
d = squareform(pdist(x, 'euclidean'))   # 欧几里得距离
print(d)
