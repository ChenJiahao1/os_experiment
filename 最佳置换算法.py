if __name__ == '__main__':
    ans = 0
    print('内存块数:')
    n = int(input())
    print('页面号引用串:')
    a = [int(i) for i in input().split()]
    memory = [-1] * n
    j = 0
    index = 0
    while j < n:
        if a[index] not in memory:
            memory[j] = a[index]
            ans += 1
            j += 1
        print('访问页面:', a[index])
        print('内存:', *memory)
        print()
        index += 1
    for i in range(index, len(a)):
        if a[i] not in memory:
            ans += 1
            f = 0
            tmp = a[i + 1::]
            flag = [0] * n
            for j in range(n):
                if memory[j] in tmp:
                    flag[j] = tmp.index(memory[j])
                else:
                    memory[j] = a[i]
                    f = 1
                    break
            if f == 0:
                memory[flag.index(max(flag))] = a[i]
        print('访问页面:', a[i])
        print('内存:', *memory)
        print()
    print('缺页次数:', ans)
    print('缺页率:', ans / len(a))

'''
3
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
'''
