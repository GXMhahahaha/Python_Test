t = (10, [20, 30], 100)
print(t, type(t))
for i in range(0, 3):
    print(t[i], type(t[i]), id(t[i]))

# t[1] = [20, 30, 40]  不可以修改
t[1].append(40)
print(t[1], type(t[1]), id(t[1]))
