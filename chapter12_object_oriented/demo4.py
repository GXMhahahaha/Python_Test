print('------------------继承------------------')


# 可以多继承

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_num):
        super().__init__(name, age)
        self.stu_num = stu_num


class Teacher(Person):
    def __init__(self, name, age, teaching_year):
        super().__init__(name, age)
        self.teaching_year = teaching_year


teacher = Teacher('jake', 20, 10)
print(teacher.teaching_year)
stu1 = Student('Bill', 20, 2160500088)
print(stu1.stu_num)

teacher.info()
