import os
lst = os.listdir()
re = []
for i in lst:
    if i.endswith('.py'):
        print(i)

