# @Time : 2020/3/4 14:10 
# @Author : hqjiang
# @File : image_test.py

# scipy库第一次安装失败,也不知道什么原因,
# 怀疑是之前设置的manage repository里面的地址有问题,遂清空尝试,无效果
# 重启pycharm
# 执行pip install -i https://mirrors.aliyun.com/pypi/simple/ scipy 安装成功
# scipy库已经移除imgread..,安装imageio库代替
# from scipy.misc import imread, imsave, imresize

from PIL import Image
from imageio import imread, imsave
import numpy as np
img = imread('../assets/cat.jpg')
print(img.dtype, img.shape)   # uint8 (400, 248, 3)

img_tinted = img * [1, 0.95, 0.9]   # 改变RGB值

# resize
# img_tinted = imresize(img_tinted, (300, 300))   # scipy库中imresize已经废弃
# img_tinted = np.array(Image.fromarray(img_tinted).resize((300, 300)))  # 网上查到的解决方案,报错了
imsave('../assets/cat_tinted.jpg', img_tinted)

# imageio不知道怎么改变大小,Image不知道怎么按比例改变rgb,所以采用了这种方式.

image = Image.open('../assets/cat_tinted.jpg')
image_reshape = image.resize((300, 300), Image.ANTIALIAS)  # 改变大小
imsave('../assets/cat_reshape.jpg', image_reshape)
