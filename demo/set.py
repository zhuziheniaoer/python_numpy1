# 集合  无序不重复元素
animals = {'cat', 'dog'}
print('cat' in animals)  # True
print('fish' in animals)  # False
animals.add('fish')
print('fish' in animals)  # True
print(len(animals))  # 3
animals.add('cat')  # 添加已经在集合中的元素不会有任何操作
print(len(animals))  # 3
animals.remove('cat')
print(animals)


# loops
animals2 = {'cat', 'dog', 'fish'}
for ani in animals2:
    print(ani)

for idx, ani in enumerate(animals2):
    print('#%d: %s' % (idx, ani))

# 集合生成式 Set comprehensions
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)   # {0, 1, 2, 3, 4, 5}

