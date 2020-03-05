# @Time : 2020/3/4 16:49 
# @Author : hqjiang
# @File : image.py
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread

img = imread('../assets/cat.jpg')
plt.subplot(1, 2, 1)

# 注意使用的是imshow方法
plt.imshow(img)
img_tinted = imread('../assets/cat_tinted.jpg')
plt.subplot(1, 2, 2)
plt.imshow(img_tinted)
plt.show()
