print('------------------封装------------------')


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动')


car1 = Car('宝马')
car1.start()
print(car1.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有类型，可以在类内被使用

    def show(self):
        print(self.name, self.__age)


stu1 = Student('Bill', 20)
print(stu1.name + 'fasdf')
stu1.show()

print(stu1.name)
# print(stu1.__age)
