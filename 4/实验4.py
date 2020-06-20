from tkinter import *
import tkinter.font as tf

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def GUI():
    start = 0
    disk_num = []
    direction = 0 # 0表示向数字减小的方向，1表示向数字增大的方向
    record = []
    ##整体窗口参数#################################################################
    root_window = Tk()
    root_window.title('磁盘移臂调度算法')
    root_window.resizable(width=True, height=True)
    ft = tf.Font(size=6)
    ##############################################################################

    ##第一层三个标签###############################################################
    disk_label_str = StringVar()
    disk_label_str.set('磁盘请求序列：')
    disk_label = Label(root_window, textvariable=disk_label_str, bg='yellow')
    disk_label.grid(row=0, column=0, columnspan=4, ipadx=100)
    start_label_str = StringVar()
    start_label_str.set('开始磁盘号：')
    start_label = Label(root_window, textvariable=start_label_str, bg='red')
    start_label.grid(row=0, column=4, ipadx=100)
    direction_label_str = StringVar()
    direction_label_str.set('磁头移动方向：')
    direction_label = Label(root_window, textvariable=direction_label_str, bg='green')
    direction_label.grid(row=0, column=5, ipadx=100, columnspan=2)
    ##############################################################################

    ##第二层三个输入框##############################################################
    disk_entry_str = StringVar()
    disk_entry_str.set('输入磁盘请求序列')
    Entry(root_window, textvariable=disk_entry_str).grid(row=1, column=0, columnspan=4, ipadx=75)
    start_entry_str = StringVar()
    start_entry_str.set('输入开始磁盘号')
    Entry(root_window, textvariable=start_entry_str).grid(row=1, column=4, ipadx=65)
    # direction_entry_str = StringVar()
    # direction_entry_str.set('输入磁头移动方向')
    # Entry(root_window, textvariable=direction_entry_str).grid(row=1, column=5, ipadx=70, columnspan=2)
    ###############################################################################

    ##第三层的四个按钮###############################################################
    def get_disk():
        nonlocal disk_num
        new_disk_num = disk_entry_str.get()
        if (is_number(new_disk_num)):
            disk_num.append(int(new_disk_num))
        elif (',' in new_disk_num):
            new_disk_nums = new_disk_num.split(',')
            for i in new_disk_nums:
                disk_num.append(int(i))
        string = ''
        for i in disk_num:
            string = string + ' ' + str(i)
        disk_label_str.set(string)
    def delete_disk():
        nonlocal disk_num
        if len(disk_num) == 0:
            return
        del disk_num[len(disk_num) - 1]
        if len(disk_num) >= 1:
            string = ''
            for i in disk_num:
                string = string + ' ' + str(i)
            disk_label_str.set(string)
        else:
            disk_label_str.set('输入磁盘请求序列')
    def get_start():
        nonlocal start
        new_start = start_entry_str.get()
        if (is_number(new_start)):
            start = int(new_start)
        string = '开始序号：' + str(start)
        start_label_str.set(string)
    # def get_direction():
    #     nonlocal direction
    #     new_direction = direction_entry_str.get()
    #     if(is_number(new_direction)):
    #         if(int(new_direction)==0 or int(new_direction)==1):
    #             direction = int(new_direction)
    #     if(int(direction) == 0):
    #         string = '数字变小方向'
    #     elif(int(direction) == 1):
    #         string = '数字变大方向'
    #     direction_label_str.set(string)
    Button(root_window, text='输入磁盘请求号', command=get_disk).grid(row=2, column=0, columnspan=2)
    Button(root_window, text='删除磁盘请求号', command=delete_disk).grid(row=2, column=2, columnspan=2)
    Button(root_window, text='输入开始磁盘号', command=get_start).grid(row=2, column=4)
    # Button(root_window, text='输入磁头移动方向', command=get_direction).grid(row=2, column=5)

    def set_direction_left():
        nonlocal direction
        direction = v.get()
        direction_label_str.set('数字变小方向')
    def set_direction_right():
        nonlocal direction
        direction = v.get()
        direction_label_str.set('数字变大方向')
    v = IntVar()
    Radiobutton(root_window, text="向左", variable=v, value=0, command=set_direction_left).grid(row=2, column=5)
    Radiobutton(root_window, text="向右", variable=v, value=1, command=set_direction_right).grid(row=2, column=6)

    ################################################################################

    ##第五层帆布显示算法##############################################################
    line_start = 100
    line_end = 900
    Height = 400 if len(disk_num) * 30 + 50 < 400 else len(disk_num) * 30 + 80
    canvas = Canvas(root_window, bg='white', confine=False)
    canvas.config(width=1000, height=Height)
    canvas.grid(row=4, column=0, columnspan=7, rowspan=2)

    def create_disk_num_line(y):
        nonlocal disk_num, line_start, line_end, start
        if len(disk_num) == 0:
            return
        sorted_disk_num = sorted(list(set(disk_num)))
        canvas.create_line(line_start, y, line_end, y)
        if start <= max(sorted_disk_num) + 20:
            start_x = (line_end-line_start) * (start / (max(sorted_disk_num) + 20)) + line_start
            canvas.create_oval(start_x-4, y-4, start_x+4, y+4)
            disk_num_x = []
            for i in range(len(sorted_disk_num)):
                disk_num_x.append((line_end-line_start) * (sorted_disk_num[i] / (max(sorted_disk_num) + 20)) + line_start)
            str_x = disk_num_x.copy()
            for i in range(len(str_x)):
                if i != len(str_x) - 1 and str_x[i + 1] - str_x[i] <= 15:
                    str_x[i] -= 5
                    str_x[i + 1] += 5
            for i in range(len(str_x)):
                canvas.create_line(disk_num_x[i], y - 10, disk_num_x[i], y)
                canvas.create_text(str_x[i], y + 10, text=str(sorted_disk_num[i]))
        else:
            start_x = (line_end - line_start) * (start / (start + 20)) + line_start
            canvas.create_oval(start_x - 4, y - 4, start_x + 4, y + 4)
            disk_num_x = []
            for i in range(len(sorted_disk_num)):
                disk_num_x.append(
                    (line_end - line_start) * (sorted_disk_num[i] / (start + 20)) + line_start)
            str_x = disk_num_x.copy()
            for i in range(len(str_x)):
                if i != len(str_x) - 1 and str_x[i + 1] - str_x[i] <= 15:
                    str_x[i] -= 5
                    str_x[i + 1] += 5
            for i in range(len(str_x)):
                canvas.create_line(disk_num_x[i], y - 10, disk_num_x[i], y)
                canvas.create_text(str_x[i], y + 10, text=str(sorted_disk_num[i]))
    def create_disk_move(y):
        nonlocal record, line_start, line_end, start
        if len(record)==0:
            return
        if start <= max(record) + 20:
            SSTF_record_x = [(line_end-line_start) * (start / (max(record) + 20)) + line_start]
            for i in range(len(record)):
                SSTF_record_x.append((line_end-line_start) * (record[i] / (max(record) + 20)) + line_start)
            SSTF_line = []
            for i in range(len(SSTF_record_x)):
                x = SSTF_record_x[i]
                SSTF_line.append([x, y])
                canvas.create_oval(x-2, y-2, x+2, y+2)
                y += 30
            for i in range(len(SSTF_line)-1):
                canvas.create_line(tuple(SSTF_line[i]), tuple(SSTF_line[i+1]))
        else:
            SSTF_record_x = [(line_end - line_start) * (start / (start + 20)) + line_start]
            for i in range(len(record)):
                SSTF_record_x.append((line_end - line_start) * (record[i] / (start + 20)) + line_start)
            SSTF_line = []
            for i in range(len(SSTF_record_x)):
                x = SSTF_record_x[i]
                SSTF_line.append([x, y])
                canvas.create_oval(x - 2, y - 2, x + 2, y + 2)
                y += 30
            for i in range(len(SSTF_line) - 1):
                canvas.create_line(tuple(SSTF_line[i]), tuple(SSTF_line[i + 1]))
    ################################################################################

    ##第四层两个算法按钮##############################################################
    record_label_var = StringVar()
    record_label_var.set('这里显示磁盘移动序列')
    Label(root_window, textvariable=record_label_var, bg='yellow').grid(row=3, column=4, ipadx=80)
    move_label_var = StringVar()
    move_label_var.set('这里显示移臂的总量')
    Label(root_window, textvariable=move_label_var, bg='blue').grid(row=3, column=5, columnspan=2, ipadx=80)

    def show_SSTF():
        nonlocal record, start, disk_num, line_start
        x = ALL
        canvas.delete(x)
        Height = 400 if len(disk_num) * 30 + 50 < 400 else len(disk_num) * 30 + 80
        canvas.config(width=1000, height=Height)
        canvas.create_text(50, 30, text='SSTF')
        record = SSTF(start, disk_num.copy())
        record_label_var.set(str(record))
        last_num = start
        sum_move = 0
        for i in range(len(record)):
            sum_move += abs(record[i] - last_num)
            last_num = record[i]
        move_label_var.set('移臂的总量:' + str(sum_move))
        create_disk_num_line(30)
        create_disk_move(50)
    def show_SCAN():
        nonlocal record, start, disk_num, direction
        x = ALL
        canvas.delete(x)
        Height = 400 if len(disk_num) * 30 + 50 < 400 else len(disk_num) * 30 + 80
        canvas.config(width=1000, height=Height)
        canvas.create_text(50, 30, text='SCAN')
        record = SCAN(start, disk_num.copy(), direction)
        record_label_var.set(str(record))
        last_num = start
        sum_move = 0
        for i in range(len(record)):
            sum_move += abs(record[i] - last_num)
            last_num = record[i]
        move_label_var.set('移臂的总量:' + str(sum_move))
        create_disk_num_line(30)
        create_disk_move(50)
    Button(root_window, text='SSTF', command=show_SSTF).grid(row=3, column=0, columnspan=2)
    Button(root_window, text='SCAN', command=show_SCAN).grid(row=3, column=2, columnspan=2)
    ################################################################################

    root_window.mainloop()
def SSTF(start, disk_num):
    # 输入示例：
    # start = 100，磁头所在磁盘号
    # disk_num = [55, 58, 39, 18, 90, 160, 150, 38, 184]，需要访问磁盘号，list结构

    disk_record = [] # 依次记录访问的磁盘号
    for i in range(len(disk_num)):
        next_disk = sorted(disk_num, key=lambda x:abs(x-start))[0] # 排序找离磁头最近的磁盘号
        disk_record.append(next_disk)
        disk_num.remove(next_disk)
        start = next_disk # 修改磁头所在磁盘号
    return disk_record
def SCAN(start, disk_num, direction):
    # 输入示例：
    # start = 100，磁头所在磁盘号
    # disk_num = [55, 58, 39, 18, 90, 160, 150, 38, 184]，需要访问磁盘号，list结构
    # direction = 0，表示向左移动，direction = 1，表示向右移动

    disk_record = [] # 依次记录访问的磁盘号
    left_num = [] # 存储磁头左边的磁盘号
    right_num = [] # 存储磁头右边的磁盘号
    for i in disk_num:
        if i <= start:
            left_num.append(i)
        else:
            right_num.append(i)
    if direction == 0: # 初始磁头向左
        disk_record = disk_record + sorted(left_num, reverse=True)
        disk_record = disk_record + sorted(right_num)
    elif direction == 1: # 初始磁头向右
        disk_record = disk_record + sorted(right_num)
        disk_record = disk_record + sorted(left_num, reverse=True)
    return disk_record





if __name__ == '__main__':
    # start = 100
    # disk_num = [55, 58, 39, 18, 90, 160, 150, 38, 184]
    # direction = 0  # 0表示向数字减小的方向，1表示向数字增大的方向
    # print(SSTF(start, disk_num.copy()))
    # print(SCAN(start, disk_num.copy(), 0))
    # print(SCAN(start, disk_num.copy(), 1))

    GUI()