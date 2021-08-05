def fib(n):
    a, b = 0, 1
    count = 0
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1


re = fib(10)
for i in re:
    print(i)
