# 函数
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(sign(x))


# 定义具有可选参数函数
def hello(name, loud=False):
    if loud:
        print('HELLO, %s' % name.upper())
    else:
        print('hello, %s' % name)


hello('Judy', True)
hello('Jack')
