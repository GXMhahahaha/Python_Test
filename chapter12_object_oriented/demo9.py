class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


s1 = Student('Bill423423')
s2 = Student('JakeSSOO')

print(s1 + s2)
s = s1.__add__(s2)
print(s, type(s))

print('--------------------------------------------------')
lst = [11, 22, 33, 44]

print(lst.__len__())
print(len(lst))  # 其实调用的是lst的内置函数

print(len(s1))
print(s1.__len__())
