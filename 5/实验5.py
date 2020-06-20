import numpy as np
from tkinter import *
from pprint import pprint
# 参数
KB = 2048
size_of_disk_block = 2*KB
num_of_disk_block = 500
num_of_file = 50
# 结构
free_table = [[0, num_of_disk_block]]
bitmap = np.zeros(num_of_disk_block)
# 磁盘
disk = np.zeros((num_of_disk_block, size_of_disk_block))
#########################################################################################
def GUI(num_file_dict, delete_file_dict):
    global free_table, bitmap, KB, num_of_file, num_of_disk_block
    free_table_file_table = {}
    bitmap_file_table = {}
    add_file_dict = num_file_dict
    delete_file_dict = delete_file_dict

    input_scrollbar_row = 0
    button_row = 1
    show_scrollbar_row = 6

    root_window = Tk()
    #################################################################################
    # 第一层两个滑动窗口
    add_file_scrollbar = Scrollbar(root_window)
    add_file_scrollbar.grid(row=input_scrollbar_row, column=1, sticky=N + E + W, ipady=70, rowspan=5)
    add_file_listbox = Listbox(root_window, yscrollcommand=add_file_scrollbar.set)
    add_file_listbox.insert(END, '需要存入的文件：')
    for file_name, file_text in add_file_dict.items():
        file_size = np.round(len(file_text) / KB, 2)
        add_file_listbox.insert(END, file_name + '  ' + str(file_size) + 'KB')
    add_file_listbox.grid(row=input_scrollbar_row, column=0, rowspan=5)
    ###############
    delete_file_scrollbar = Scrollbar(root_window)
    delete_file_scrollbar.grid(row=input_scrollbar_row, column=5, sticky=N + E + W, ipady=70, rowspan=5)
    delete_file_listbox = Listbox(root_window, yscrollcommand=delete_file_scrollbar.set)
    delete_file_listbox.insert(END, '需要取出的文件')
    for file_name, file_text in delete_file_dict.items():
        file_size = np.round(len(file_text) / KB, 2)
        delete_file_listbox.insert(END, file_name + '  ' + str(file_size) + 'KB')
    delete_file_listbox.grid(row=input_scrollbar_row, column=4, rowspan=5)
    ###########################################################################################


    #########################################################################################################
    # 左边四个
    input_add_file_entry_str = StringVar()
    input_add_file_entry_str.set('输入')
    Entry(root_window, textvariable=input_add_file_entry_str).grid(row=0, column=2, columnspan=2)

    def get_add_file():
        nonlocal add_file_dict
        new_file = input_add_file_entry_str.get()
        file_name = new_file.split(',')[0]
        file_size = float(new_file.split(',')[1])
        file_text = np.random.randint(0, 2, size=int(file_size*KB))
        add_file_dict[file_name] = file_text
        add_file_listbox.insert(END, file_name + '  ' + str(round(file_size, 2)) + 'KB')
    def delete_add_file():
        all_key = list(add_file_dict.keys())
        # print(all_key[1])
        add_file_dict.pop(all_key[-1])
        add_file_listbox.delete(END)
    def clear_add_file():
        add_file_listbox.delete(0,END)
        add_file_dict.clear()
        add_file_listbox.insert(END, '需要存入的文件：')

    Button(root_window, text='添加', command=get_add_file).grid(row=button_row, column=2, sticky=N + E + W, columnspan=2)
    Button(root_window, text='删除', command=delete_add_file).grid(row=button_row+1, column=2, sticky=N + E + W, columnspan=2)
    Button(root_window, text='清空', command=clear_add_file).grid(row=button_row+2, column=2, sticky=N + E + W, columnspan=2)
    ################################################################################################################

    #########################################################################################################
    # 右边4个
    input_delete_file_entry_str = StringVar()
    input_delete_file_entry_str.set('输入')
    Entry(root_window, textvariable=input_delete_file_entry_str).grid(row=0, column=6, columnspan=2)

    def get_delete_file():
        nonlocal delete_file_dict
        new_file = input_add_file_entry_str.get()
        file_name = new_file.split(',')[0]
        file_size = float(new_file.split(',')[1])
        file_text = np.random.randint(0, 2, size=int(file_size * KB))
        delete_file_dict[file_name] = file_text
        delete_file_listbox.insert(END, file_name + '  ' + str(round(file_size, 2)) + 'KB')
    def delete_delete_file():
        all_key = list(delete_file_dict.keys())
        # print(all_key[1])
        delete_file_dict.pop(all_key[-1])
        delete_file_listbox.delete(END)
    def clear_delete_file():
        delete_file_listbox.delete(0,END)
        delete_file_dict.clear()
        delete_file_listbox.insert(END, '需要取出的文件：')

    Button(root_window, text='添加', command=get_delete_file).grid(row=button_row, column=6, sticky=N + E + W, columnspan=2)
    Button(root_window, text='删除', command=delete_delete_file).grid(row=button_row + 1, column=6, sticky=N + E + W,
                                                                 columnspan=2)
    Button(root_window, text='清空', command=clear_delete_file).grid(row=button_row + 2, column=6, sticky=N + E + W,
                                                                columnspan=2)
    ###############################################################################################################


    # free_table####################################################################
    # 空闲表

    free_table_scrollbar = Scrollbar(root_window)
    free_table_scrollbar.grid(row=show_scrollbar_row, column=1, sticky=N + E + W, ipady=70)
    free_table_listbox = Listbox(root_window, yscrollcommand=free_table_scrollbar.set)
    for i in range(len(free_table)):
        row = free_table[i]
        free_table_listbox.insert(END, str(row))
    free_table_listbox.grid(row=show_scrollbar_row, column=0)
    # file_table####################################################################
    free_table_file_table_scrollbar = Scrollbar(root_window)
    free_table_file_table_scrollbar.grid(row=show_scrollbar_row, column=3, sticky=N + E + W, ipady=70)
    free_table_file_table_listbox = Listbox(root_window, yscrollcommand=free_table_file_table_scrollbar.set)
    new_free_table_file_table = sorted(free_table_file_table.items(), key=lambda x:x[1][0])
    for row in new_free_table_file_table:
        free_table_file_table_listbox.insert(END, str(row))
    free_table_file_table_listbox.grid(row=show_scrollbar_row, column=2)
    free_table_file_table_scrollbar.config(command=free_table_file_table_listbox.yview)
    ############################################################################


    # bitmap####################################################################

    add_num_of_bitmap = 8 - (num_of_disk_block % 8)
    add_zeros = np.zeros(add_num_of_bitmap)
    new_bitmap = np.hstack((bitmap, add_zeros))
    new_bitmap = np.reshape(new_bitmap, (len(new_bitmap) // 8, 8))

    bitmap_scrollbar = Scrollbar(root_window)
    bitmap_scrollbar.grid(row=show_scrollbar_row, column=5, sticky=N + E + W, ipady=70)
    bitmap_listbox = Listbox(root_window, yscrollcommand=bitmap_scrollbar.set)
    for i in range(len(new_bitmap)):
        row = new_bitmap[i]
        bitmap_listbox.insert(END, str(i * 8) + ' ' + str(row))
    bitmap_listbox.grid(row=show_scrollbar_row, column=4)
    # file_table####################################################################
    bitmap_file_table_scrollbar = Scrollbar(root_window)
    bitmap_file_table_scrollbar.grid(row=show_scrollbar_row, column=7, sticky=N + E + W, ipady=70)
    bitmap_file_table_listbox = Listbox(root_window, yscrollcommand=bitmap_file_table_scrollbar.set)
    new_bitmap_file_table = sorted(bitmap_file_table.items(), key=lambda x: x[1][0])
    for row in new_bitmap_file_table:
        bitmap_file_table_listbox.insert(END, str(row) + ' ' + str())
    bitmap_file_table_listbox.grid(row=show_scrollbar_row, column=6)
    bitmap_file_table_scrollbar.config(command=bitmap_file_table_listbox.yview)
    ###################################################################################

    def free_table_add():
        for file_name, file_text in add_file_dict.items():
            AddFile2FreeTable(file_name, file_text, free_table_file_table)

        free_table_listbox.delete(0, END)
        for i in range(len(free_table)):
            row = free_table[i]
            free_table_listbox.insert(END, str(row))

        free_table_file_table_listbox.delete(0, END)
        new_free_table_file_table = sorted(free_table_file_table.items(), key=lambda x: x[1][0])
        for row in new_free_table_file_table:
            free_table_file_table_listbox.insert(END, str(row))

    def free_table_delete():
        for file_name, file_size in delete_file_dict.items():
            DeleteFileInFreeTable(file_name, free_table_file_table)

        free_table_listbox.delete(0, END)
        for i in range(len(free_table)):
            row = free_table[i]
            free_table_listbox.insert(END, str(row))

        free_table_file_table_listbox.delete(0, END)
        new_free_table_file_table = sorted(free_table_file_table.items(), key=lambda x: x[1][0])
        for row in new_free_table_file_table:
            free_table_file_table_listbox.insert(END, str(row))

    def bitmap_add():
        for file_name, file_text in add_file_dict.items():
            AddFile2BitMap(file_name, file_text, bitmap_file_table)

        add_num_of_bitmap = 8 - (num_of_disk_block % 8)
        add_zeros = np.zeros(add_num_of_bitmap)
        new_bitmap = np.hstack((bitmap, add_zeros))
        new_bitmap = np.reshape(new_bitmap, (len(new_bitmap) // 8, 8))
        bitmap_listbox.delete(0, END)
        for i in range(len(new_bitmap)):
            row = new_bitmap[i]
            bitmap_listbox.insert(END, str(i * 8) + ' ' + str(row))

        new_bitmap_file_table = sorted(bitmap_file_table.items(), key=lambda x: x[1][0])
        bitmap_file_table_listbox.delete(0, END)
        for row in new_bitmap_file_table:
            bitmap_file_table_listbox.insert(END, str(row) + ' ' + str())

    def bitmap_delete():
        for file_name, file_size in delete_file_dict.items():
            DeleteFileInBitMap(file_name, bitmap_file_table)

        add_num_of_bitmap = 8 - (num_of_disk_block % 8)
        add_zeros = np.zeros(add_num_of_bitmap)
        new_bitmap = np.hstack((bitmap, add_zeros))
        new_bitmap = np.reshape(new_bitmap, (len(new_bitmap) // 8, 8))
        bitmap_listbox.delete(0, END)
        for i in range(len(new_bitmap)):
            row = new_bitmap[i]
            bitmap_listbox.insert(END, str(i * 8) + ' ' + str(row))

        new_bitmap_file_table = sorted(bitmap_file_table.items(), key=lambda x: x[1][0])
        # print(len(bitmap_file_table))
        bitmap_file_table_listbox.delete(0, END)
        for row in new_bitmap_file_table:
            bitmap_file_table_listbox.insert(END, str(row) + ' ' + str())

    Button(root_window, text='空闲表/链存入', command=free_table_add).grid(row=5, column=0, sticky=N + E + W, columnspan=2)
    Button(root_window, text='空闲表/链取出', command=free_table_delete).grid(row=5, column=2, sticky=N + E + W,
                                                                        columnspan=2)
    Button(root_window, text='位示图存入', command=bitmap_add).grid(row=5, column=4, sticky=N + E + W, columnspan=2)
    Button(root_window, text='位示图取出', command=bitmap_delete).grid(row=5, column=6, sticky=N + E + W,
                                                                  columnspan=2)


    

    root_window.mainloop()
#########################################################################################
def AddFile2FreeTable(file_name, file_text, file_table):
    global KB, size_of_disk_block, num_of_disk_block, free_table, disk
    if len(file_text) % size_of_disk_block == 0:
        file_size = len(file_text) // size_of_disk_block
        new_file_text = file_text
    else:
        raw_file_size = len(file_text) // size_of_disk_block
        file_size = raw_file_size + 1
        add_text_size = file_size * size_of_disk_block - len(file_text)
        add_text = np.ones(add_text_size) * -1
        new_file_text = np.hstack((file_text, add_text))
    can_save = 0
    for i in range(len(free_table)):
        if free_table[i][1] >= file_size:
            can_save = 1
            disk_start_num = free_table[i][0]
            free_table[i][0] += file_size
            free_table[i][1] -= file_size

            file_table[file_name] = [disk_start_num, file_size]
            for j in range(disk_start_num, disk_start_num + file_size):
                disk[j] = new_file_text[(j - disk_start_num) * size_of_disk_block:((j - disk_start_num) + 1) * size_of_disk_block]
            break
    if can_save == 0:
        print(file_name, ' can not find enough block ', file_size)
        return
    new_free_table = []
    for node in free_table:
        if node[1] != 0:
            new_free_table.append(node)
    free_table = new_free_table


def DeleteFileInFreeTable(file_name, file_table):
    global KB, size_of_disk_block, num_of_disk_block, free_table, disk
    if file_name not in file_table.keys():
        print('can not find ', file_name)
        return
    free_table.append(file_table[file_name])
    free_table = sorted(free_table)
    new_free_table = []
    for i in range(len(free_table) - 1):
        if free_table[i][0] + free_table[i][1] == free_table[i + 1][0]:
            free_table[i][1] = free_table[i][1] + free_table[i + 1][1]
            free_table[i + 1][0] = -1

    for i in range(len(free_table)):
        if free_table[i][0] != -1:
            new_free_table.append(free_table[i])
    free_table = new_free_table
    del file_table[file_name]


def AddFile2BitMap(file_name, file_text, file_table):
    global KB, size_of_disk_block, num_of_disk_block, bitmap, disk
    if len(file_text) % size_of_disk_block == 0:
        file_size = len(file_text) // size_of_disk_block
        new_file_text = file_text
    else:
        raw_file_size = len(file_text) // size_of_disk_block
        file_size = raw_file_size + 1
        add_text_size = file_size * size_of_disk_block - len(file_text)
        add_text = np.ones(add_text_size) * -1
        new_file_text = np.hstack((file_text, add_text))
    can_save = 0
    num_of_zero = 0
    start_of_zero = 0
    for i in range(num_of_disk_block):
        if bitmap[i] == 0:
            num_of_zero += 1
        else:
            num_of_zero = 0
            start_of_zero = i + 1
        if num_of_zero >= file_size:
            can_save = 1
            bitmap[start_of_zero:start_of_zero + num_of_zero] = np.ones(num_of_zero)
            file_table[file_name] = [start_of_zero, num_of_zero]
            for j in range(start_of_zero, start_of_zero + num_of_zero):
                disk[j] = new_file_text[(j - start_of_zero) * size_of_disk_block:((j - start_of_zero) + 1) * size_of_disk_block]
            break
    if can_save == 0:
        print(file_name, ' can not find enough block ', file_size)
        return
    return


def DeleteFileInBitMap(file_name, file_table):
    global KB, size_of_disk_block, num_of_disk_block, bitmap, disk
    if file_name not in file_table.keys():
        # print(file_name)
        print('can not find ', file_name)
        return
    file_node = file_table[file_name]
    bitmap[file_node[0]:file_node[0] + file_node[1]] = np.zeros(file_node[1])
    del file_table[file_name]



if __name__ == '__main__':

    # 创建50个新文件
    file_table = {}
    num_file_dict = {}
    delete_file_dict = {}
    for i in range(num_of_file):
        file_size = np.random.randint(2*KB, 10*KB, size=1)
        file_text = np.random.randint(0, 2, size=file_size)
        num_file_dict[str(i) + '.txt'] = file_text
        if i % 2 != 0:
            delete_file_dict[str(i) + '.txt'] = file_text
    # 创建5个新文件
    alpha_file_dict = {}
    for file_name, file_size in zip(['A', 'B', 'C', 'D', 'E'], [7 * KB, 5 * KB, 2 * KB, 9 * KB, 3.5 * KB]):
        file_text = np.random.randint(0, 2, size=int(file_size))
        alpha_file_dict[file_name + '.txt'] = file_text

    # # 空闲表/空闲盘区链测试
    # for file_name, file_text in num_file_dict.items():
    #     AddFile2FreeTable(file_name, file_text, file_table)
    # # print('-'*30)
    # # pprint(free_table)
    # # pprint(sorted(file_table.items(), key=lambda x: x[1]))
    # for i in range(1, num_of_file, 2):
    #     DeleteFileInFreeTable(str(i) + '.txt', file_table)
    # # print('-' * 30)
    # # pprint(free_table)
    # # pprint(sorted(file_table.items(), key=lambda x: x[1]))
    # for file_name, file_text in alpha_file_dict.items():
    #     AddFile2FreeTable(file_name, file_text, file_table)
    # print('-' * 30)
    # pprint(free_table)
    # pprint(sorted(file_table.items(), key=lambda x:x[1]))
    #
    # # 位示图测试
    # file_table.clear()
    # for file_name, file_text in num_file_dict.items():
    #     AddFile2BitMap(file_name, file_text, file_table)
    # for i in range(1, num_of_file, 2):
    #     DeleteFileInBitMap(str(i) + '.txt', file_table)
    # for file_name, file_text in alpha_file_dict.items():
    #     AddFile2BitMap(file_name, file_text, file_table)
    # add_num_of_bitmap = 8 - (num_of_disk_block % 8)
    # add_zeros = np.zeros(add_num_of_bitmap)
    # new_bitmap = np.hstack((bitmap, add_zeros))
    # pprint(np.reshape(new_bitmap, (len(new_bitmap) // 8, 8)))
    # pprint(sorted(file_table.items(), key=lambda x:x[1]))


    # # 界面
    GUI(num_file_dict, delete_file_dict)







