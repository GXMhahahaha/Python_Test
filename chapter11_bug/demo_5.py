def sum_demo(x, y):
    for _ in range(10):
        x += 1
        y += 1
        result = x + y
    return result


def tee():
    i = 1
    while i < 10:
        i += 1
    print(i)


if __name__ == '__main__':
    result = sum_demo(1, 1)
    import nt as nn

    tee()
    print(result)
