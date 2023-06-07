# 最短寻道优先，电梯(扫描算法)

if __name__ == '__main__':
    ans = 0
    order = []
    print('初始位置:')
    now = int(input())
    print('进程请求访问顺序:')
    a = [int(i) for i in input().split()]
    a.sort()
    l = 0
    r = len(a)
    while l < r:
        mid = (l + r + 1) >> 1
        if a[mid] <= now:
            l = mid
        else:
            r = mid - 1
    left = a[l]
    l = 0
    r = len(a)
    while l < r:
        mid = (l + r) >> 1
        if a[mid] >= now:
            r = mid
        else:
            l = mid + 1
    right = a[l]
    if abs(left - now) <= abs(right - now):
        ans += abs(left - now)
        now = left
        order.append(now)
    else:
        ans += abs(right - now)
        now = right
        order.append(now)
    now_index = a.index(now)
    print(now)
    flag = [False] * len(a)
    flag[now_index] = True
    while False in flag:
        if False in flag[0:now_index] and False in flag[now_index+1::]:
            l = now_index - 1
            while flag[l] and l > 0:
                l -= 1
            r = now_index + 1
            while flag[r] and r < len(a) - 1:
                r += 1
            left = a[l]
            right = a[r]
            if abs(left - now) <= abs(right - now):
                ans += abs(left - now)
                now = left
                order.append(now)
                now_index = l
            else:
                ans += abs(right - now)
                now = right
                order.append(now)
                now_index = r
        elif False in flag[0:now_index] and False not in flag[now_index+1::]:
            l = now_index - 1
            while flag[l] and l > 0:
                l -= 1
            left = a[l]
            ans += abs(left - now)
            now = left
            order.append(now)
            now_index = l
        else:
            r = now_index + 1
            while flag[r] and r < len(a) - 1:
                r += 1
            right = a[r]
            ans += abs(right - now)
            now = right
            order.append(now)
            now_index = r
        flag[now_index] = True
        print(now)

    print('访问顺序:', *order)
    print('磁头总共移动了', ans, '个磁道')
    print('平均查找长度{:.3f}'.format(ans / len(a)))

'''
100
23 376 205 132 19 61 190 398 29 4 18 40
'''
