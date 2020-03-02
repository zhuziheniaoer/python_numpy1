def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# print(quick_sort([3, 9, 10, 6, 2, 9, 20]))

# basic data types
x = 3
print(type(3))  # <class 'int'>
print(x ** 4)  # 81,四次方

y = 2.5
print(type(y))  # <class 'float'>

t = True
f = False
print(type(t))  # <class ' bool'>
print(t and f)  # False
print(t or f)  # True
print(not t)  # False
print(t != f)  # True

hello = 'hello'
world = 'world'
print(len(hello))  # 5
hw = hello + ' ' + world
print(hw)   # hello world

hw12 = '%s %s %d' % (hello, world, 12)   # 字符串格式化
print(hw12)  # hello world 12

s = "hello"
print(s.capitalize())  # 首字母大写 Hello
print(s.upper())  # 字母转为大写 HELLO
print(s.rjust(7))  # 右对齐字符串,并用空格填充
print(s.ljust(9))  # 左对齐?
print(s.center(7)) # 居中字符串,用空格填充
print(s.replace('l', '(ell)'))  # 替换
print('   world'.strip())  # 去掉空格
