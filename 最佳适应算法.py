Free = 0
Busy = 1


class Item:
    def __init__(self, address, name, size, state):
        self.address = address
        self.name = name
        self.size = size
        self.state = state  # 0表示空闲


def add(name, size):
    list = []
    for i in range(len(freetable)):
        if freetable[i].state == Free:
            list.append([freetable[i].size, freetable[i].address])
    list.sort()
    for j in range(len(list)):
        if list[j][0] >= size:
            for i in range(len(freetable)):
                if freetable[i].address == list[j][1]:
                    if freetable[i].size != size:
                        new_item = Item(freetable[i].address + size, None, freetable[i].size - size, Free)
                        freetable[i].size = size
                        freetable[i].state = Busy
                        freetable[i].name = name
                        freetable.insert(i + 1, new_item)
                    else:
                        freetable[i].name = name
                        freetable[i].state = Busy
                    return True
    return False


def release(name):
    length = len(freetable)
    for i in range(length):
        if freetable[i].state == Busy and freetable[i].name == name:
            freetable[i].state = Free
            if i != 0 and freetable[i - 1].state == Free:
                freetable[i - 1].size += freetable[i].size
                freetable.pop(i)
                if i != length - 1 and freetable[i].state == Free:
                    freetable[i - 1].size += freetable[i].size
                    freetable.pop(i)
                return True
            if i == 0 and freetable[i + 1].state == Free:
                freetable[i + 1].address = freetable[i].address
                freetable[i + 1].size += freetable[i].size
                freetable.pop(i)
                return True
            return True
    return False


def output():
    print()
    list = []
    for i in range(len(freetable)):
        if freetable[i].state == Free:
            list.append([freetable[i].size, freetable[i].address])
    list.sort()
    cnt = 0
    for j in range(len(list)):
        for i in range(len(freetable)):
            if freetable[i].address == list[j][1]:
                print('分区号', cnt, '分区首址', freetable[i].address, '分区大小', freetable[i].size, '状态', freetable[i].state)
                cnt += 1
    print()


def output_all():
    print()
    for i in range(len(freetable)):
        print('分区号', i, '分区首址', freetable[i].address, '分区大小', freetable[i].size, '状态', freetable[i].state)
    print()


size = int(input())
freetable = [Item(0, None, size, Free)]
opt = 1
while opt == 1 or opt == 2:
    print("申请空间(1) / 释放空间(2) / 结束操作(9)")
    opt = int(input())
    if opt == 1:
        print("进程名称:", end=' ')
        name = input()
        print("申请空间大小:", end=' ')
        size = int(input())
        if add(name, size) is not True:
            print('内存不足，分配失败!')
    if opt == 2:
        print("进程名称:", end=' ')
        name = input()
        if release(name) is not True:
            print('进程不存在!')
    output_all()

'''
640
1
1
100
1
2
150
1
3
300
2
2
1
4
80
2
3
'''