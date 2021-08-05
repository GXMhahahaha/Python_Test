class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 10)
stu2 = Student('李四', 20)
stu1.eat()

print('-------------动态绑定属性和方法---------------------')
stu1.gender = 'male'
print(stu1.gender)


def show():
    print('在类之外')


stu1.show = show
stu1.show()