import argparse
import os
import shutil
from queue import Queue
from threading import Thread


def remove_directory(src, num):
    '''使用 num 个线程删除 src 目录下的所有文件和子目录'''
    # 源文件夹必须存在
    assert os.path.isdir(src), f'{src} must be an existing directory.'
    # 最多容纳 10 个元素的队列
    q = Queue(10)

    def add(src):
        # 把源文件夹中所有项目添加到队列中
        for f in os.listdir(src):
            f = os.path.join(src, f)
            q.put(f)
            # 递归
            if os.path.isdir(f):
                add(f)
        # 用来通知工作线程再没有文件需要删除了
        for _ in range(num):
            q.put(None)

    # 创建并启动往队列中存放元素的线程
    t_add = Thread(target=add, args=(src,))
    t_add.start()

    def remove(name):
        # 工作线程函数
        while True:
            srcItem = q.get()
            if srcItem is None:
                print(name, 'quit...')
                break
            print(f'{name}: removing {srcItem}')
            # 删除文件或目录
            try:
                if os.path.isfile(srcItem):
                    os.remove(srcItem)
                elif os.path.isdir(srcItem):
                    shutil.rmtree(srcItem)
            except Exception as e:
                print(f'{name}: failed to remove {srcItem} - {e}')

    # 创建指定数量的线程来删除文件
    threads = []
    for i in range(num):
        t = Thread(target=remove, args=('Thread' + str(i),))
        t.start()
        threads.append(t)

    t_add.join()
    for t in threads:
        t.join()


if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='remove files and directories recursively from src')
    parser.add_argument('-s', '--src', required=True, help='source directory to remove')
    parser.add_argument('-n', '--num', type=int, default=5, help='number of threads to use')
    args = parser.parse_args()

    remove_directory(args.src, args.num)
    print('Done.')
