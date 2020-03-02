# 元组 不可变有序列表 可作为字典的key和集合的元素
t = (5, 6, 7)
print(t)
print(type(t))  # <class 'tuple'>

# loop
for x in t:
    print(x)

for i, x in enumerate(t):
    print('#%d: %s' % (i, x))

tuple_gene = (x ** 2 for x in range(4))  # 这是一个generator,生成器对象
print(tuple_gene.__next__())  # 内置函数,不建议使用
tuples = tuple(tuple_gene)   # 转化为元组,或者使用 tuple_gene.__next__()遍历
print(tuples)

d = {(x, x + 1): x for x in range(4)}
print(d)
t2 = (2, 3)
print(d[t2])   # 2
print(d[(1, 2)])    # 1

