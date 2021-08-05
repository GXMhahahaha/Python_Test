class Student:
    native_place = '长春'  # 类属性  所有对象所共享的
    class_num = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法  必须由一个实例来使用
    def eat(self):
        print('学生在吃饭')

    # 静态方法  不能使用类内的变量和函数
    @staticmethod
    def method():
        print('静态方法')

    # 类方法  可以使用类内的变量和函数
    @classmethod
    def cm(cls):
        cls.class_num += 1
        print('类方法', cls.class_num)


stu1 = Student('张三', 100)
print(id(stu1), type(stu1), stu1)

stu1.eat()
print(stu1.age)

Student.eat(stu1)  # 需要传入一个对象
Student.method()

print(Student.native_place)
stu2 = Student('李四', 40)
print(stu1.native_place, stu2.native_place)

Student.cm()
