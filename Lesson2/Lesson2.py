# -*- coding:gbk -*-
# װ����ʹ��

# python��һ�нԶ���

#��������ʱ����

def fun_wrap(func):
    def wrapper(*args, **kw):
        print('call %s:' % func.__name__)
        return func(*args, **kw)

    return wrapper()


@fun_wrap
def func():
    print('run func')


if __name__ == '__main__':
    print('this demo demonstrating decorator')
    func()
