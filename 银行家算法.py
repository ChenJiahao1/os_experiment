def calculate_need():
    for i in range(n):
        for j in range(m):
            Need[i][j] = Max[i][j] - Allocation[i][j]


def comparation(index):
    for i in range(m):
        if Need[index][i] > Available[i]:
            return False
    return True


def output():
    print('剩余可用资源:', *Available)
    print('\tMax \tAllocation\tNeed')
    for i in range(n):
        print('P{:d}'.format(i + 1), end=' ')

        print('\t', *Max[i], end=' ')
        if i != 2:
            print('', end=' ')
        if Finish[i]:
            tmp = [0] * m
            print('\t', *tmp, end=' ')
            print('\t', *tmp, end=' ')
        else:
            print('\t', *Allocation[i], end=' ')
            print('\t', *Need[i], end=' ')
        print('\t', Finish[i], end=' ')
        print()
    print()


if __name__ == '__main__':
    print('进程数量:')
    n = int(input())
    print('资源种数：')
    m = int(input())
    print('每类资源的现有数量:')
    Available = [int(i) for i in input().split()]
    print('每个进程对每类资源的最大需求:')
    Max = []
    for _ in range(n):
        Max.append([int(i) for i in input().split()])
    print('系统每类资源当前已分配给每种进程的资源数:')
    Allocation = []
    for _ in range(n):
        Allocation.append([int(i) for i in input().split()])
    Need = [[0] * m for _ in range(n)]
    calculate_need()

    test_num = input('进程')
    print('请求资源:')
    test = [int(i) for i in input().split()]
    for i in range(m):
        if Available[i] < test[i]:
            print('不存在安全序列!')
            exit()

    Finish = [False] * n
    output()
    ans = []
    while False in Finish:
        for i in range(n):
            if Finish[i]:
                continue
            if comparation(i):
                for j in range(m):
                    Available[j] += Allocation[i][j]
                    Finish[i] = True
                ans.append(i+1)
                output()
                break
    print('安全序列:', end=' ')
    for i in range(len(ans)):
        print('P{:d}'.format(ans[i]), end=' ')
'''
5
3
2 3 3
5 5 9
5 3 6
4 0 11
4 2 5
4 2 4
2 1 2
4 0 2
4 0 5
2 0 4
3 1 4
'''
