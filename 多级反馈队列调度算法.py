import queue as Q

run = 'r'
wait = 'w'
finish = 'f'


class Pcb:
    def __init__(self, name, atime, ntime):
        self.name = name
        self.atime = atime
        self.ntime = ntime
        self.rtime = 0  # 已经运行的时间
        self.state = wait


def into_queue():
    global tmp, tmp_index
    t = tmp_index
    for i in range(t, len(tmp)):
        if tmp[i].atime <= h:
            queue_list[0].put(tmp[i])
            tmp_index = i + 1
        else:
            return


if __name__ == '__main__':
    print('进程数量:')
    n = int(input())
    print('设置队列数量:')
    q_num = int(input())
    queue_list = [Q.Queue() for _ in range(q_num)]
    tmp = []
    for _ in range(n):
        name = input()
        atime = int(input())
        ntime = int(input())
        pcb = Pcb(name, atime, ntime)
        tmp.append(pcb)
    tmp.sort(key=lambda x: x.atime)
    tmp_index = 0
    h = 0  # 此时运行时间

    into_queue()

    ans = 0

    flag = 1
    while flag:
        flag = 0
        for i in range(q_num):
            queue = queue_list[i]
            if not queue.empty():
                time = pow(2, i)
                if i != q_num - 1:
                    next_queue = queue_list[i + 1]
                pcb = queue.get()
                print('\n当前cpu时间', h)
                print('当前运行进程', pcb.name, '该进程已运行时间', pcb.rtime)
                if pcb.ntime - pcb.rtime > time:  # 如果该时间片无法运行完该进程
                    pcb.rtime += time
                    print('此次运行时间:', time)
                    h += time
                    if i != q_num - 1:
                        next_queue.put(pcb)
                    else:
                        queue.put(pcb)
                else:
                    h += pcb.ntime - pcb.rtime
                    print('此次运行时间:', pcb.ntime - pcb.rtime)
                    pcb.rtime = pcb.ntime
                    print('\n进程', pcb.name, '已完成')
                    print('其周转时间为', h - pcb.atime, '\t', '带权周转时间:{:.3f}'.format((h - pcb.atime) / pcb.ntime))
                    ans += (h - pcb.atime) / pcb.ntime
                if tmp_index != n:
                    into_queue()
                break
        for queue in queue_list:
            if not queue.empty():
                flag = 1
                break
    print('所有进程已完成,平均带权周转时间为:{:.3f}'.format(ans / n))

'''
5
3
A
0
60
B
1
6
C
2
20
D
6
5
E
8
1
'''
