# 列表
xs = [3, 1, 2]  # create a list
print(xs, xs[2])  # [3, 1, 2] 2
print(xs[-1])  # 2
xs[2] = 'foo'
print(xs)  # [3, 1, 'foo']
xs.append('bar')
print(xs)   # [3, 1, 'foo', 'bar']
x = xs.pop()
print(x, xs)  # bar [3, 1, 'foo']


# 切片slicing 获取子列表
nums = list(range(5))  # range is a built-in function that create a list of integers
print(nums)  # [0, 1, 2, 3, 4]
print(nums[2:4])  # [2, 3] 索引 2 到 4 前闭后开
print(nums[2:])  # [2, 3, 4]  索引 2 到 末尾
print(nums[:2])  # [0, 1]  索引从 0 到 2 前闭后开
print(nums[:])   # [0, 1, 2, 3, 4] 获取整个列表
print(nums[:-1])  # [0, 1, 2, 3] 获取从 0 到倒数第一个 前闭后开
nums[2:4] = [8, 9]
print(nums)   # [0, 1, 8, 9 4]


# 循环 Loop over
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

for index, animal in enumerate(animals):
    print('#%d: %s' % (index + 1, animal))


nums_square = [0, 1, 2, 3, 4]
squares = []
for num in nums_square:
    squares.append(num ** 2)
print(squares)      # [0, 1, 4, 9, 16]


# 使用 列表生成式 list comprehensions 简化
squares_two = [num ** 3 for num in nums_square]
print(squares_two)   # 三次方 [0, 1, 8, 27, 64]


# list comprehensions can also contains conditions
# 列表生成式可以包含条件
even_squares = [num ** 2 for num in nums_square if num % 2 == 0]
print(even_squares)  # [0, 4, 16]

