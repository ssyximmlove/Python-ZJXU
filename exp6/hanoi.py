def hanoi_tower(n, source, target, auxiliary):
    """
    模拟汉诺塔问题的移动过程

    参数：
    n -- 盘子的数量
    source -- 源柱子
    target -- 目标柱子
    auxiliary -- 辅助柱子
    """
    # 初始化三个柱子上的盘子
    a = list(range(n, 0, -1))  # A柱子初始有n个盘子，从大到小排列
    b = []  # B柱子初始为空
    c = []  # C柱子初始为空

    # 定义移动函数
    def move_disk(disk, source, target):
        """
        移动一个盘子，并打印移动步骤和当前状态

        参数：
        disk -- 要移动的盘子编号（从1开始）
        source -- 源柱子
        target -- 目标柱子
        """
        # 将盘子从源柱子移动到目标柱子
        if source == 'A':
            a.remove(disk)
        elif source == 'B':
            b.remove(disk)
        elif source == 'C':
            c.remove(disk)

        if target == 'A':
            a.append(disk)
        elif target == 'B':
            b.append(disk)
        elif target == 'C':
            c.append(disk)

        # 按照从大到小的顺序排列，以便打印时大的在下，小的在上
        a.sort(reverse=True)
        b.sort(reverse=True)
        c.sort(reverse=True)

        # 打印移动步骤
        print(f"Step {step_count[0]}: Move disk {disk} from {source} to {target}")

        # 打印当前状态
        print(f"A: {a if a else []}")
        print(f"B: {b if b else []}")
        print(f"C: {c if c else []}")
        print("-" * 20)

        # 步骤计数加1
        step_count[0] += 1

    # 使用非局部变量来记录步骤计数
    step_count = [1]

    # 递归函数实现汉诺塔算法
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            # 如果只有一个盘子，直接从源柱子移动到目标柱子
            move_disk(1, source, target)
        else:
            # 将n-1个盘子从源柱子移动到辅助柱子
            hanoi(n - 1, source, auxiliary, target)
            # 将第n个盘子从源柱子移动到目标柱子
            move_disk(n, source, target)
            # 将n-1个盘子从辅助柱子移动到目标柱子
            hanoi(n - 1, auxiliary, target, source)

    # 调用递归函数开始移动
    hanoi(n, source, target, auxiliary)


# 测试程序
n = int(input("请输入盘子的数量: "))
hanoi_tower(n, 'A', 'C', 'B')
