# 偏函数的使用

def func():
    print(int('2222'))
    print(int('2222', base=8))
    print(int2('533', 8))
    print(int_custom('533'))


def int2(x, base=2):
    return int(x, base)


def int_custom(x):
    kw = {'base': 8}
    return int(x, **kw)


if __name__ == '__main__':
    print('''偏函数的使用''')
    func()
