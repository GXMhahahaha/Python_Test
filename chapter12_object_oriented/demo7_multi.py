# 动态语言不关心继承关系，有这个方法就行
class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗会吃')


class Cat(Animal):
    def eat(self):
        print('猫会吃')


class Person(object):
    @ staticmethod
    def eat():
        print('人会吃')


def pp(obj):  # 传入一个对象
    obj.eat()


p1 = Person()
c1 = Cat()
pp(p1)
pp(c1)
