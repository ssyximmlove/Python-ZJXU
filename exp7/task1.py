# coding=utf-8
import codecs
import random
import string

'''
演示如何使用 Python 标准库 random 来生成随机数据，这在需要
'''
# 常用汉字 Unicode 编码表
StringBase = [chr(i) for i in range(0x4e00, 0x9fff + 1)]


def getEmail():
    suffix = ['.com', '.org', '.net', '.cn']  # 常见域名后缀，可以随意扩展该列表
    characters = string.ascii_letters + string.digits + '_'
    username = ''.join((random.choice(characters) for i in
                        range(random.randint(6, 12))))
    domain = ''.join((random.choice(characters) for i in range(random.randint(3, 6))))
    return username + '@' + domain + random.choice(suffix)


def getTelNo():
    return ''.join((str(random.randint(0, 9)) for i in range(11)))


def getNameOrAddress(flag):
    '''flag=1 表示返回随机姓名，flag=0 表示返回随机地址'''
    result = ''
    if flag == 1:
        rangestart, rangeend = 2, 5  # 大部分中国人的姓名在 2-4 个汉字
    elif flag == 0:
        rangestart, rangeend = 10, 30  # 假设地址在 10-30 个汉字之间
    else:
        print('flag must be 1 or 0')
    for i in range(random.randint(rangestart, rangeend)):
        result += random.choice(StringBase)
    return result


def getSex():
    return random.choice(('男', '女'))


def getAge():
    return str(random.randint(18, 100))


def main(filename):
    with codecs.open(filename, 'w', 'utf-8') as fp:
        fp.write('Name,Sex,Age,TelNo,Address,Email\n')
        # quickly generate information of 2000 persons
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            email = getEmail()
            line = name + ',' + sex + ',' + age + ',' + '' + tel + ',' + address + ',' + email + '\n'
            fp.write(line)


def output(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        while True:
            line = fp.readline()
            if not line:
                return
            line = line.split(',')
            for i in line:
                print(i, end=',')
            print()


if __name__ == '__main__':
    filename = 'information.txt'
    main(filename)
    output(filename)

# 输出随机例子
# Name,Sex,Age,TelNo,Address,Email
