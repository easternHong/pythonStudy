# -*- coding:gbk -*-
# װ����ʹ��

# python��һ�нԶ���

# ��������ʱ����


def readFile(filePath):
    print("read file by line: ")
    # һ������
    contentInLine = u"./data/NCDC/�Ϻ�/����/9705626661750dat.txt"
    with open(filePath) as f:
        for line in f:
            for i in range(len(contentInLine)):
                if contentInLine[i] > u'\u4e000' and contentInLine[i] < u'\u9fff':
                    print(contentInLine[i])


if __name__ == '__main__':
    readFile('')
    print("good")
