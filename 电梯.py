# 最短寻道优先，电梯(扫描算法)

if __name__ == '__main__':
    order = []
    print('该磁盘的最大磁道号:')
    MAX = int(input())
    print('初始位置:')
    now = int(input())
    print('此刻磁头的运动方向:(1)向磁道号减小大的方向,(2)向磁道号增大的方向')
    direct = int(input())
    print('进程请求访问顺序:')
    a = [int(i) for i in input().split()]
    a.sort()
    if direct == 2:
        ans = (a[-1] - now) + (a[-1] - a[0])
        l = 0
        r = len(a)
        while l < r:
            mid = (l + r) >> 1
            if a[mid] >= now:
                r = mid
            else:
                l = mid + 1

        for i in range(l, len(a)):
            now = a[i]
            order.append(now)
        for i in range(l - 1, -1, -1):
            now = a[i]
            order.append(now)
    else:
        ans = now + a[-1]
        l = 0
        r = len(a)
        while l < r:
            mid = (l + r + 1) >> 1
            if a[mid] <= now:
                l = mid
            else:
                r = mid - 1
        for i in range(l, -1, -1):
            now = a[i]
            order.append(now)
        for i in range(l+1, len(a)):
            now = a[i]
            order.append(now)
    print('访问顺序:', *order)
    print('磁头总共移动了', ans, '个磁道')
    print('平均查找长度{:.3f}'.format(ans / len(a)))
'''
399
100
2
23 376 205 132 19 61 190 398 29 4 18 40
'''
