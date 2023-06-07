class PCB:
    name = None  # 进程名
    state = 'w'  # w, r, f 等待、运行、结束
    atime = 0  # 到达时间
    ntime = 0  # 需要时间
    super = 1  # 优先级
    flag = 0  # 是否到达


def disp(p: PCB):
    print("qname \t state \t atime \t ntime \t super");
    print("|{:s}\t".format(p.name), end='')
    print("|{:s}\t".format(p.state), end='')
    print("|{:d}\t".format(p.atime), end='')
    print("|{:d}\t".format(p.ntime), end='')
    print("|{:.3f}\t".format(p.super), end='')
    print()


def running():
    global n, h, ans
    for i in range(n):
        if pcb[i].atime <= h and pcb[i].state != 'f':
            maxm = i
            pcb[i].state = 'r'
            break
    tmp = pcb[maxm]
    print("\n **** 当前正在运行的进程是:{:s}".format(tmp.name))
    disp(tmp)
    print("\n ****当前就绪队列状态为:")
    for i in range(n):
        if i == maxm:
            continue
        if pcb[i].atime <= h and pcb[i].state != 'f':
            disp(pcb[i])
    h += tmp.ntime
    print("进程{:s}已完成,其周转时间为:{:d},其带权周转时间为:{:.3f}\n".format(tmp.name, h - tmp.atime, (h - tmp.atime) / tmp.ntime))
    ans += (h - tmp.atime) / tmp.ntime
    tmp.state = 'f'
    for i in range(1, n):
        if pcb[i].atime <= h and pcb[i].state != 'f':
            pcb[i].super = (h- pcb[i].atime) / pcb[i].ntime + 1
    pcb.sort(key=lambda x: x.super, reverse=True)


if __name__ == '__main__':
    h = 0  # cpu当前运行时间
    ans = 0  # 周转时间之和
    n = int(input())
    pcb = [PCB() for _ in range(n)]
    for i in range(n):
        name = input()
        atime, ntime = map(int, input().split())
        pcb[i].name = name
        pcb[i].atime = atime
        pcb[i].ntime = ntime
    pcb.sort(key=lambda x: x.atime)
    for i in range(n):
        running()
    print("所有进程已完成，平均带权周转时间{:.3f}".format(ans / n))

'''
5
A
0 9
B
1 6
C
2 4
D
3 5
E
4 1
'''


