from tkinter import *
from tkinter import ttk
class p: # 进程类
    def __init__(self, p_name, p_arrive, p_serve):
        self.p_name = p_name # 进程名
        self.p_arrive = p_arrive # 进程到达时间
        self.p_need_serve = p_serve # 进程剩余需要服务时间
        self.p_start = -1 # 进程开始时间
        self.p_end = -1 # 进程结束时间
        self.p_serve = p_serve # 进程需要服务时间
    def calculate_turnover(self):
        self.turnover = self.p_end - self.p_arrive  # 计算周转时间
        self.weighted_turnover = (self.p_end - self.p_arrive) / self.p_serve  # 计算带权周转时间
    def disp(self):
        # 计算周转时间，并输出相关统计信息
        self.calculate_turnover()
        print('{:^5}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{}'.format('name', 'arrive', 'serve', 'start', 'end', 'turnover', 'weighted-turnover'))
        print('{:^5}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{}'.format(self.p_name, self.p_arrive, self.p_serve, self.p_start, self.p_end,
                                                              self.turnover, self.weighted_turnover))


def GUI(process):
    root_window = Tk()
    root_window.resizable(width=True, height=True)
    
    #第一层,1个label，1个empty##########################################################################
    process_label_str = StringVar()
    process_str = ''
    for i in range(len(process)):
        if i != len(process_str) - 1:
            process_str = process_str + str(process[i]) + '\n'
        else:
            process_str = process_str + str(process[i])
    process_label_str.set(process_str)
    show_process_label = Label(root_window, textvariable=process_label_str, bg='yellow')
    show_process_label.grid(row=0, column=0, columnspan=2, rowspan=2, ipadx=25)

    new_process_entry_str = StringVar()
    new_process_entry_str.set('输入进程，形式为a,1,2')
    Entry(root_window, textvariable=new_process_entry_str).grid(row=0, column=4, columnspan=3)

    def get_process():
        nonlocal process
        new_process = new_process_entry_str.get()
        new_process_list = new_process.split(',')
        process.append([new_process_list[0], int(new_process_list[1]), int(new_process_list[2])])
        process_str = ''
        for i in range(len(process)):
            if i != len(process_str) - 1:
                process_str = process_str + str(process[i]) + '\n'
            else:
                process_str = process_str + str(process[i])
        process_label_str.set(process_str)
    def delete_process():
        del process[len(process) - 1]
        process_str = ''
        if len(process) == 0:
            process_str = '无进程'
        else:
            for i in range(len(process)):
                if i != len(process_str) - 1:
                    process_str = process_str + str(process[i]) + '\n'
                else:
                    process_str = process_str + str(process[i])
        process_label_str.set(process_str)


    Button(root_window, text='输入', command=get_process).grid(row=1, column=4, columnspan=2, sticky=N+E+W)
    Button(root_window, text='删除', command=delete_process).grid(row=1, column=6, columnspan=2, sticky=N+E+W)
    ##############################################################################################

    #第二层四个按钮################################################################################
    RR_time_str = StringVar()
    RR_time_str.set('1')
    Entry(root_window, textvariable=RR_time_str).grid(row=2, column=8)

    def show_FCFS():
        process_end = FCFS(process.copy())
        sub_window = Toplevel()
        sub_window.title('FCFS')

        tree = ttk.Treeview(sub_window)  # #创建表格对象
        tree["columns"] = ("完成时间", "周转时间", "带权周转时间")  # #定义列
        tree.column("完成时间", width=100)
        tree.column("周转时间", width=100)
        tree.column("带权周转时间", width=100)
        tree.heading("完成时间", text="完成时间")
        tree.heading("周转时间", text="周转时间")
        tree.heading("带权周转时间", text="带权周转时间")
        for i in range(len(process_end)):
            p = process_end[i]
            tuple_p = (p.p_end, p.turnover, p.weighted_turnover)
            tree.insert("", i, text=p.p_name, values=tuple_p)
        tree.pack()
    def show_HRN():
        process_end = HRN(process.copy())
        sub_window = Toplevel()
        sub_window.title('HRN')

        tree = ttk.Treeview(sub_window)  # #创建表格对象
        tree["columns"] = ("完成时间", "周转时间", "带权周转时间")  # #定义列
        tree.column("完成时间", width=100)
        tree.column("周转时间", width=100)
        tree.column("带权周转时间", width=100)
        tree.heading("完成时间", text="完成时间")
        tree.heading("周转时间", text="周转时间")
        tree.heading("带权周转时间", text="带权周转时间")
        for i in range(len(process_end)):
            p = process_end[i]
            tuple_p = (p.p_end, p.turnover, p.weighted_turnover)
            tree.insert("", i, text=p.p_name, values=tuple_p)
        tree.pack()
    def show_SJF():
        process_end = SJF(process.copy())
        sub_window = Toplevel()
        sub_window.title('SJF')

        tree = ttk.Treeview(sub_window)  # #创建表格对象
        tree["columns"] = ("完成时间", "周转时间", "带权周转时间")  # #定义列
        tree.column("完成时间", width=100)
        tree.column("周转时间", width=100)
        tree.column("带权周转时间", width=100)
        tree.heading("完成时间", text="完成时间")
        tree.heading("周转时间", text="周转时间")
        tree.heading("带权周转时间", text="带权周转时间")
        for i in range(len(process_end)):
            p = process_end[i]
            tuple_p = (p.p_end, p.turnover, p.weighted_turnover)
            tree.insert("", i, text=p.p_name, values=tuple_p)
        tree.pack()
    def show_RR():
        RR_time = int(RR_time_str.get())
        process_end = RR(process.copy(), RR_time)
        sub_window = Toplevel()
        sub_window.title('RR(' + str(RR_time) + ')')

        tree = ttk.Treeview(sub_window)  # #创建表格对象
        tree["columns"] = ("完成时间", "周转时间", "带权周转时间")  # #定义列
        tree.column("完成时间", width=100)
        tree.column("周转时间", width=100)
        tree.column("带权周转时间", width=100)
        tree.heading("完成时间", text="完成时间")
        tree.heading("周转时间", text="周转时间")
        tree.heading("带权周转时间", text="带权周转时间")
        for i in range(len(process_end)):
            p = process_end[i]
            tuple_p = (p.p_end, p.turnover, p.weighted_turnover)
            tree.insert("", i, text=p.p_name, values=tuple_p)
        tree.pack()
    Button(root_window, text='FCFS', command=show_FCFS).grid(row=2, column=0, columnspan=2, sticky=N+E+W)
    Button(root_window, text='HRN', command=show_HRN).grid(row=2, column=2, columnspan=2, sticky=N+E+W, ipadx=25)
    Button(root_window, text='SJF', command=show_SJF).grid(row=2, column=4, columnspan=2, sticky=N+E+W, ipadx=25)
    Button(root_window, text='RR', command=show_RR).grid(row=2, column=6, columnspan=2, sticky=N+E+W, ipadx=25)


    root_window.mainloop()


def FCFS(process):
    # 输入为进程列表：[进程名，到达时间，服务时间]，例如：
    # process = [['A', 0, 3],
    #            ['B', 2, 6],
    #            ['C', 4, 4],
    #            ['D', 6, 5],
    #            ['E', 8, 2]]
    process = sorted(process, key=lambda x: x[1]) # 将进程按照到达时间排序
    process_stack = [] # 进程栈，栈底为正在运行的进程
    process_end = [] # 完成进程列表
    time = -1 # 时间
    while(1):
        time += 1

        if(len(process) != 0  and  time == process[0][1]): # 来进程就进入进程栈
            new_p = p(process[0][0], process[0][1], process[0][2]) # 新建进程类实例
            process_stack.append(new_p) # 加入进程栈
            del process[0] # 在输入进程列表中删除

        if(len(process_stack) != 0): # 进程栈不空就要运行进程栈栈底的程序
            now_p = process_stack[0] # 获取栈底进程
            if(now_p.p_need_serve == now_p.p_serve): # 如果需要服务时间等于服务时间，说明刚开始运行，记录开始时间
                now_p.p_start = time
            now_p.p_need_serve -= 1 # 运行，需要服务时间减1

            if(now_p.p_need_serve == 0): # 如果需要服务时间为0
                now_p.p_end = time # 记录结束时间
                now_p.calculate_turnover() # 计算周转时间
                del process_stack[0] # 从进程栈中删除
                process_end.append(now_p) # 加入完成栈
        else: # 进程栈空就退出
            break

    print('FCFS:')
    show_process_tima(process_end) # 格式化输出统计信息
    return process_end


def RR(process, RR_time):
    # 输入为进程列表：[进程名，到达时间，服务时间]和时间片大小，例如：
    # process = [['A', 0, 3],
    #            ['B', 2, 6],
    #            ['C', 4, 4],
    #            ['D', 6, 5],
    #            ['E', 8, 2]]
    # 1. 前一个进程剩下的时间片可以给下一个进程用
    # 2. 对于时间片到了，前一个进程完成了，同时新来了一个进程的情况
    # 处理过程是，（1）将前一个进程移除 （2）将新来的进程加入进程栈 （3）不将交换栈底换到栈顶，直接运行栈底进程
    process = sorted(process, key=lambda x: x[1]) # 将进程按照到达时间排序

    process_stack = [] # 进程栈，栈底为正在运行的进程
    process_end = [] # 完成进程列表
    time = -1 # 时间
    Pass = 0 # 如果等于1，意为跳过时间片，即上一个时间片进程完成了，剩下的时间留给下个进程
    while(1):
        time += 1

        if(len(process) != 0  and  time == process[0][1]): # 来进程就进入进程栈
            new_p = p(process[0][0], process[0][1], process[0][2]) # 新建进程
            process_stack.append(new_p) # 加入进程栈
            del process[0] # 在输入进程中删除


        if(len(process_stack) != 0): # 进程栈不空就要运行进程栈栈底的程序

            if (time != 0 and time % RR_time == 0 and Pass==0):  # 到了新的时间片
                temp_p = process_stack[0]
                del process_stack[0]
                process_stack.append(temp_p)

            if(time % RR_time == 0): # Pass修改为0
                Pass = 0

            now_p = process_stack[0] # 获取栈底进程
            if(now_p.p_need_serve == now_p.p_serve): # 如果需要服务时间等于服务时间，说明刚开始运行，记录开始时间
                now_p.p_start = time
            now_p.p_need_serve -= 1 # 运行，需要服务时间减1

            if(now_p.p_need_serve == 0): # 如果需要服务时间为0
                now_p.p_end = time # 记录结束时间
                now_p.calculate_turnover() # 计算周转时间
                del process_stack[0] # 从进程栈中删除
                process_end.append(now_p) # 加入完成栈
                Pass = 1 # 意为跳过时间片，原因是上一个时间片完成进程完成了，剩下的时间留给下个进程
        else: # 进程栈空就退出
            break

    print('RR:')
    show_process_tima(process_end) # 格式化输出统计信息
    return process_end


def SJF(process):
    # 输入为进程列表：[进程名，到达时间，服务时间]，例如：
    # process = [['A', 0, 3],
    #            ['B', 2, 6],
    #            ['C', 4, 4],
    #            ['D', 6, 5],
    #            ['E', 8, 2]]
    from operator import attrgetter
    process = sorted(process, key=lambda x: x[1]) # 将进程按照到达时间排序
    process_stack = [] # 进程栈，栈底为正在运行的进程
    process_end = [] # 完成进程列表
    time = -1 # 时间
    while(1):
        time += 1

        if(len(process) != 0  and  time == process[0][1]): # 来进程就进入进程栈
            new_p = p(process[0][0], process[0][1], process[0][2]) # 新建进程
            process_stack.append(new_p) # 加入进程栈
            del process[0] # 在输入进程中删除
            process_stack = sorted(process_stack, key=attrgetter('p_need_serve', 'p_arrive')) # 每次运行需要服务时间最短的进程


        if(len(process_stack) != 0): # 进程栈不空就要运行进程栈栈底的程序
            now_p = process_stack[0] # 获取栈底进程
            # print(time, ' ', now_p.p_name)
            if(now_p.p_need_serve == now_p.p_serve): # 如果需要服务时间等于服务时间，说明刚开始运行，记录开始时间
                now_p.p_start = time
            now_p.p_need_serve -= 1 # 运行，需要服务时间减1

            if(now_p.p_need_serve == 0): # 如果需要服务时间为0
                now_p.p_end = time # 记录结束时间
                now_p.calculate_turnover() # 计算周转时间
                del process_stack[0] # 从进程栈中删除
                process_end.append(now_p) # 加入完成栈
        else: # 进程栈空就退出
            break

    print('SJF:')
    show_process_tima(process_end) # 格式化输出统计信息
    return process_end


def HRN(process):
    # 输入为进程列表：[进程名，到达时间，服务时间]，例如：
    # process = [['A', 0, 3],
    #            ['B', 2, 6],
    #            ['C', 4, 4],
    #            ['D', 6, 5],
    #            ['E', 8, 2]]
    process = sorted(process, key=lambda x: x[1]) # 将进程按照到达时间排序
    process_stack = [] # 进程栈，栈底为正在运行的进程
    process_end = [] # 完成进程列表
    time = -1 # 时间
    while(1):
        time += 1

        if(len(process) != 0  and  time == process[0][1]): # 来进程就进入进程栈
            new_p = p(process[0][0], process[0][1], process[0][2]) # 新建进程
            process_stack.append(new_p) # 加入进程栈
            del process[0] # 在输入进程中删除

        if(len(process_stack) != 0): # 进程栈不空就要运行进程栈栈底的程序
            process_stack = sorted(process_stack, key=lambda x:(1 + (time - x.p_arrive)/x.p_need_serve), reverse=True)
            now_p = process_stack[0] # 获取栈底进程

            if(now_p.p_need_serve == now_p.p_serve): # 如果需要服务时间等于服务时间，说明刚开始运行，记录开始时间
                now_p.p_start = time
            now_p.p_need_serve -= 1 # 运行，需要服务时间减1

            if(now_p.p_need_serve == 0): # 如果需要服务时间为0
                now_p.p_end = time # 记录结束时间
                now_p.calculate_turnover() # 计算周转时间
                del process_stack[0] # 从进程栈中删除
                process_end.append(now_p) # 加入完成栈
        else:
            break

    print('HRN:')
    show_process_tima(process_end)# 格式化输出统计信息
    return process_end


def show_process_tima(process_end):
    # print('{:^5}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{}'.format('name', 'arrive', 'serve', 'start', 'end', 'turnover',
    #                                                       'weighted-turnover'))
    # for i in range(len(process_end)):
    #     p = process_end[i]
    #     print('{:^5}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{}'.format(p.p_name, p.p_arrive, p.p_serve, p.p_start,
    #                                                           p.p_end,
    #                                                           p.turnover, p.weighted_turnover))
    print('{:^8}|{:^6}|{:^8}|{}'.format('进程名', '完成时间', '周转时间',
                                                          '带权周转时间'))
    for i in range(len(process_end)):
        p = process_end[i]
        print('{:^10}|{:^10}|{:^10}|{}'.format(p.p_name, p.p_end,
                                                              p.turnover, p.weighted_turnover))


if __name__ == '__main__':
    # 进程
    process=[['A', 0, 3],
             ['B', 2, 6],
             ['C', 4, 4],
             ['D', 6, 5],
             ['E', 8, 2]]



    # 测试进程类
    # new_p = p(process[0][0], process[0][1], process[0][2])
    # new_p.disp()

    # 测试算法
    FCFS_end = FCFS(process.copy())
    RR_end = RR(process.copy(), 1)
    SJF_end = SJF(process.copy())
    HRN_end = HRN(process.copy())

    # 界面
    GUI(process)

