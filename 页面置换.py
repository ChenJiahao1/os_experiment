import random
import queue


def optimial(ins_address, index):
    global count
    page_num = ins_address // 10
    for i in range(3):
        if Block[i] == -1:
            Block[i] = page_num
            count += 1
            print('调入第{:d}条指令'.format(index))
            print('指令的逻辑地址为:', ins_address)
            print('内存中该指令不存在！')
            print('页面置换完成, 该指令的物理地址为第{:d}块,第{:d}条'.format(i, ins_address % 10))
            return
        if Block[i] == page_num:
            print('调入第{:d}条指令'.format(index))
            print('指令的逻辑地址为:', ins_address)
            print('内存中该指令已存在！')
            print('该指令的物理地址为第{:d}块,第{:d}条'.format(i, ins_address % 10))
            return
    count += 1
    f = 0
    tmp = page_address[index + 1::]
    flag = [0] * 3
    end_index = -1
    for j in range(3):
        if Block[j] in tmp:
            flag[j] = tmp.index(Block[j])
        else:
            Block[j] = page_num
            end_index = j
            f = 1
            break
    if f == 0:
        end_index = flag.index(max(flag))
        Block[end_index] = page_num
    print('调入第{:d}条指令'.format(index))
    print('指令的逻辑地址为:', ins_address)
    print('内存中该指令不存在,且内存块已满！')
    print('最佳置换算法运行完毕！')
    print('该指令的物理地址为第{:d}块,第{:d}条'.format(end_index, ins_address % 10))


def LRU(ins_address, index):
    global count
    page_num = ins_address // 10
    for i in range(3):
        if Block[i] == -1:
            Block[i] = page_num
            count += 1
            print('调入第{:d}条指令'.format(index))
            print('指令的逻辑地址为:', ins_address)
            print('内存中该指令不存在！')
            print('页面置换完成, 该指令的物理地址为第{:d}块,第{:d}条'.format(i, ins_address % 10))
            return
        if Block[i] == page_num:
            print('调入第{:d}条指令'.format(index))
            print('指令的逻辑地址为:', ins_address)
            print('内存中该指令已存在！')
            print('该指令的物理地址为第{:d}块,第{:d}条'.format(i, ins_address % 10))
            return
    count += 1
    tmp = list(reversed(page_address[0:index]))
    flag = [0] * 3
    for j in range(3):
        flag[j] = tmp.index(Block[j])
    end_index = flag.index(max(flag))
    Block[end_index] = page_num
    print('调入第{:d}条指令'.format(index))
    print('指令的逻辑地址为:', ins_address)
    print('内存中该指令不存在,且内存块已满！')
    print('LRU算法运行完毕！')
    print('该指令的物理地址为第{:d}块,第{:d}条'.format(end_index, ins_address % 10))


if __name__ == '__main__':
    L = 0
    R = 319
    n = R - L + 1
    instruct_list = [0] * n
    page_address = [0] * n
    Block = [-1] * 3
    m = random.randint(L, R)
    count = 0  # 记录缺页次数
    i = 0
    random.seed(0)
    while i < n:
        m0 = random.randint(L, R)
        assert m0 != L and m0 != R, 'm0 == L or m0 == R, 后续无法继续执行, 请重试！'
        instruct_list[i] = m0 + 1
        page_address[i] = instruct_list[i] // 10
        i += 1

        m1 = random.randint(L, m0 - 1)
        instruct_list[i] = m1
        page_address[i] = instruct_list[i] // 10
        i += 1

        instruct_list[i] = m1 + 1
        page_address[i] = instruct_list[i] // 10
        i += 1

        m2 = random.randint(m1 + 2, R)
        instruct_list[i] = m2
        page_address[i] = instruct_list[i] // 10
        i += 1

        instruct_list[i] = m2 + 1
        page_address[i] = instruct_list[i] // 10
        i += 1

    print(*instruct_list)
    for i in range(len(instruct_list)):
        optimial(instruct_list[i], i)
        print()
    print('缺页次数', count)
    print('缺页率', count / 320)
    pre_count = count

    count = 0
    Block = [-1] * 3
    for i in range(len(instruct_list)):
        LRU(instruct_list[i], i)
        print()

    print('OPT:')
    print('缺页次数', pre_count)
    print('缺页率', pre_count / 320)

    print()

    print('LRU:')
    print('缺页次数', count)
    print('缺页率', count / 320)
