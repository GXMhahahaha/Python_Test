class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值  同一个对象
cpu1 = Cpu()
cpu2 = cpu1

print(cpu1, cpu2)

# 浅拷贝  对象不同了但是对象的子对象仍然相同
print('---------------------------------------------------------------------------')
disk = Disk()
computer = Computer(cpu1, disk)

import copy

computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# 深拷贝  子对象也要重新拷贝一份

print('----------------------------------------------------------------------------')

computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)