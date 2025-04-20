import argparse
import os
from queue import Queue
from shutil import copyfile
from threading import Thread


def copyFile(src, dst, num):
    '''使用 num 个线程复制 src 目录下的文件到 dst 目录中'''
    # 源文件夹必须存在
    assert os.path.isdir(src), f'{src} must be an existing directory.'
    # 如果目标文件夹不存在，创建一个
    if not os.path.isdir(dst):
        os.makedirs(dst)
    # 最多容纳 10 个元素的队列
    q = Queue(10)

    def add(src):
        # 把源文件夹中所有项目添加到队列中
        for f in os.listdir(src):
            f = os.path.join(src, f)
            if os.path.isfile(f):
                # 往队列中放数据，满了会自动等待
                q.put(f)
            elif os.path.isdir(f):
                q.put(f)
                # 递归
                add(f)
        # 用来通知工作线程再没有文件需要复制了
        for _ in range(num):
            q.put(None)

    # 创建并启动往队列中存放元素的线程
    t_add = Thread(target=add, args=(src,))
    t_add.start()

    def copy(name):
        # 工作线程函数
        while True:
            srcItem = q.get()
            if srcItem is None:
                print(name, 'quit...')
                break
            # 替换字符串，生成目标路径
            dstItem = srcItem.replace(src, dst)
            print(f'{name}:{srcItem}==>{dstItem}')
            # 复制文件
            if os.path.isfile(srcItem):
                # 根据需要创建目标文件夹
                dstDir = os.path.split(dstItem)[0]
                if not os.path.isdir(dstDir):
                    try:
                        os.makedirs(dstDir)
                    except FileExistsError as e:
                        pass
                copyfile(srcItem, dstItem)
            elif os.path.isdir(srcItem):  # 创建目标文件夹
                try:
                    os.makedirs(dstItem)
                except FileExistsError as e:
                    pass

    # 创建指定数量的线程来复制文件
    for i in range(num):
        t = Thread(target=copy, args=('Thread' + str(i),))
        t.start()


if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='copy files from src to dst')
    parser.add_argument('-s', '--src')
    parser.add_argument('-d', '--dst')
    parser.add_argument('-n', '--num', default='5')
    args = parser.parse_args()
    if args.src is not None and args.dst is not None:
        copyFile(args.src, args.dst, int(args.num))
    else:
        print('please use the following command to see how to use:')
        print('python task1.py -s <source_directory> -d <destination_directory> -n <number_of_threads>')
