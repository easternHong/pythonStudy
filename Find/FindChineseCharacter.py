# -*- coding:gbk -*-
# 装饰器使用

# python中一切皆对象

# 看不懂暂时放下


def readFile(filePath):
    print("read file by line: ")
    # 一行文字
    contentInLine = u"./data/NCDC/上海/虹桥/9705626661750dat.txt"
    with open(filePath) as f:
        for line in f:
            for i in range(len(contentInLine)):
                if contentInLine[i] > u'\u4e000' and contentInLine[i] < u'\u9fff':
                    print(contentInLine[i])


if __name__ == '__main__':
    readFile('')
    print("good")
