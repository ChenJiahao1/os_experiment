if __name__ == '__main__':
    m = 2000
    n = 32
    bitmap = [[1] * n for i in range(m)]
    # 从0开始 b = n * i + j+ 1
    # i = (b-1) // n
    # j = (b-1) % n
    for i in range(20):
        print(*bitmap[i])
    opt = 1
    while opt != 9:
        opt = int(input('请输入:(1)盘区分配;(2)释放盘块;(9)退出\n'))
        if opt == 1:
            cnt = 0
            flag = 0
            print('请输入字、位:')
            i, j = map(int, input().split())
            print('对应磁盘块号:', n * i + j + 1)
        if opt == 2:
            b = int(input('释放的盘块号:\n'))
            i = (b - 1) // n
            j = (b - 1) % n
            print('对应位示图:', i, j)
            bitmap[i][j] = 1
            for k in range(i-1, i+1 + 1):
                print(*bitmap[k])

