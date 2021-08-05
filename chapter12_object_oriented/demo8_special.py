class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name  # name是变量的一个属性
        self.age = age


x = C('Jack', 20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 类对象 属性以及方法

print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出父类
print(C.__base__)  # 输出离得最近的父类
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类
