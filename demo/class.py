# 类
class Greeter(object):
    # constructor
    def __init__(self, name):
        self.name = name   # 实例变量

    # 实例方法
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s' % self.name.upper())
        else:
            print('hello, %s' % self.name)


g = Greeter('Judy')
g.greet(True)
g.greet()


class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + 'run')


class Cat(Animal):
    def __init__(self, name, yell):
        Animal.__init__(self, name)
        self.yell = yell

    def yelled(self):
        print(self.name + ':' + self.yell)


cat = Cat('咪咪', 'mi')
cat.yelled()


class Person:
    def run(self, way):
        print('running on ' + way)


p = Person()
p.run('大明湖畔')
