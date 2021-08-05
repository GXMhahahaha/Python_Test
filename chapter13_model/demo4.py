import sys
import time
import urllib.request
import math

print(sys.getsizeof(24))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

# print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)

import numpy as np

a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)
