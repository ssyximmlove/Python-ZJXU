def hanoi_tower_iterative(n, source, target, auxiliary):
    """
    非递归实现汉诺塔问题

    参数：
    n -- 盘子的数量
    source -- 源柱子
    target -- 目标柱子
    auxiliary -- 辅助柱子
    """
    task_queue = []
    # 将初始调用压入任务队列中，格式为 (n, source, target, auxiliary, direction)
    # direction 用于标记移动方向，True 表示从源到目标，False 表示从源到辅助
    task_queue.append((n, source, target, auxiliary, True))

    step_count = 1  # 记录步骤数

    while task_queue:
        n, source, target, auxiliary, direction = task_queue.pop()

        if n == 1:
            # 如果只有一个盘子，直接移动
            print(f"第 {step_count} 步：移动第 1 个盘子：从 {source} 座到 {target} 座")
            step_count += 1
        else:
            if direction:
                # 如果方向是从源到目标
                # 需要先将 n-1 个盘子从源移动到辅助柱
                task_queue.append((n - 1, source, auxiliary, target, False))
                # 再将第 n 个盘子从源移动到目标柱
                task_queue.append((1, source, target, auxiliary, True))
                # 最后将 n-1 个盘子从辅助柱移动到目标柱
                task_queue.append((n - 1, auxiliary, target, source, True))
            else:
                # 如果方向是从源到辅助
                # 需要先将 n-1 个盘子从源移动到目标柱
                task_queue.append((n - 1, source, target, auxiliary, True))
                # 再将第 n 个盘子从源移动到辅助柱
                task_queue.append((1, source, auxiliary, target, True))
                # 最后将 n-1 个盘子从目标柱移动到辅助柱
                task_queue.append((n - 1, target, auxiliary, source, False))


# 测试程序
n = int(input("请输入盘子的数量: "))
hanoi_tower_iterative(n, 'A', 'C', 'B')
