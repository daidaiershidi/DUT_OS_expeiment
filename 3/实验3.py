from tkinter import *

def GUI():
    pages = []
    memory_size = 0
    ##整体窗口参数#################################################################
    root_window = Tk()
    root_window.title('页面置换算法')
    # root_window.geometry('200x100')
    root_window.resizable(width=True, height=True)
    ##############################################################################

    ##子窗口1#####################################################################
    # 页号输入框
    page_num_entry = StringVar()
    page_num_entry.set('请输入页号')
    Entry(root_window, textvariable=page_num_entry).grid(row=0, column=0, columnspan=2)
    # 内存大小输入框
    memory_size_entry = StringVar()
    memory_size_entry.set('请输入内存大小')
    Entry(root_window, textvariable=memory_size_entry).grid(row=2, column=0, columnspan=2)
    # 显示页号
    show_pages_label_text = StringVar()
    show_pages_label_text.set('在这里显示页号')
    show_pages_label = Label(root_window, textvariable=show_pages_label_text)
    show_memory_size_label_text = StringVar()
    show_memory_size_label_text.set('在这里显示内存大小')
    show_memory_size_label = Label(root_window, textvariable=show_memory_size_label_text)
    def get_page():
        nonlocal pages
        page_num = page_num_entry.get()
        if(is_number(page_num)):
            pages.append(int(page_num))
        elif(',' in page_num):
            page_nums = page_num.split(',')
            for i in page_nums:
                pages.append(int(i))
        string = '页号：'
        for i in pages:
            string = string + ' ' + str(i)
        show_pages_label_text.set(string)
    def delete_page():
        nonlocal pages
        if len(pages) == 0:
            return
        del pages[len(pages) - 1]
        if len(pages) >= 1:
            string = '页号：'
            for i in pages:
                string = string + ' ' + str(i)
            show_pages_label_text.set(string)
        else:
            show_pages_label_text.set('在这里显示页号')
    def get_memory_size():
        nonlocal memory_size
        memory_size_num = memory_size_entry.get()
        if (is_number(memory_size_num)):
            memory_size = int(memory_size_num)
        string = '内存：' + str(memory_size)
        show_memory_size_label_text.set(string)
        # print(memory_size)
    Button(root_window, text='输入页号', command=get_page).grid(row=1, column=0, ipadx=10)
    Button(root_window, text='删除页号', command=delete_page).grid(row=1, column=1, ipadx=10)
    Button(root_window, text='输入内存大小', command=get_memory_size).grid(row=3, column=0)
    show_pages_label.grid(row=0, column=4)
    show_memory_size_label.grid(row=2, column=4)
    ###################################################################################

    ##子窗口2###########################################################################
    def show_FIFO():
        FIFO_text.delete(1.0, END)
        FIFO_delete, FIFO_page, error_num, rate = FIFO(pages, memory_size)
        for i in range(len(FIFO_page)):
            text = FIFO_page[i]
            if FIFO_delete[i] == 0:
                FIFO_text.insert(END, str(text) + '\n')
            else:
                FIFO_text.insert(END, str(text) + '--淘汰' + str(FIFO_delete[i]) + '页\n')
        FIFO_text.insert(END, '页面缺页中断次数为：' + str(error_num) + '\n')
        FIFO_text.insert(END, '此算法页面中断率为：' + str(rate))
    def show_LRU():
        LRU_text.delete(1.0, END)
        LRU_delete, LRU_page, error_num, rate = LRU(pages, memory_size)
        for i in range(len(LRU_page)):
            text = LRU_page[i]
            if LRU_delete[i] == 0:
                LRU_text.insert(END, str(text) + '\n')
            else:
                LRU_text.insert(END, str(text) + '--淘汰' + str(LRU_delete[i]) + '页\n')
        LRU_text.insert(END, '页面缺页中断次数为：' + str(error_num) + '\n')
        LRU_text.insert(END, '此算法页面中断率为：' + str(rate))
    # 子窗口配置（包含FIFO子窗口和LRU子窗口）
    frame2 = Frame(root_window)
    FIFO_frame = Frame(frame2)
    FIFO_text = Text(root_window, width=30, height=20)
    FIFO_text.grid(row=4, column=0, rowspan=3, columnspan=6, ipadx=110)
    Button(root_window, text='FIFO', command=show_FIFO).grid(row=10, column=0)
    LRU_frame = Frame(frame2)
    LRU_text = Text(root_window, width=30, height=20)
    LRU_text.grid(row=4, column=4, rowspan=3, columnspan=6)
    Button(root_window, text='LRU', command=show_LRU).grid(row=10, column=4)
    FIFO_frame.grid(row=4, column=0, rowspan=3, columnspan=7)
    LRU_frame.grid(row=4, column=4, rowspan=2, columnspan=7)
    frame2.grid(row=4, column=0, rowspan=6, columnspan=7)
    ###################################################################################
    root_window.mainloop()


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

def FIFO(pages, memory_size):
    # 输入举例：
    # pages =  [1,22,3,4,23,32,33]，页号
    # memory_size = 4，内存大小
    FIFO_page = [] # 记录每次内存里的页号情况，如[[1],[1,2],[1,2,3]]
    FIFO_delete = [] # 记录每次换掉的页号
    memory = [] # 内存
    error_num = 0 # 统计缺页率
    pages_length = len(pages) # 总页号数量
    for page in pages: # 遍历每个页号
        if page not in memory: # 如果不在内存里
            error_num += 1 # 缺页次数加一
            if len(memory) < memory_size: # 如果没超出内存大小，调入内存
                memory.append(page)
                FIFO_delete.append(0)
            else: # 如果超出内存大小，换掉最先的页
                memory.append(page)
                FIFO_delete.append(memory[0])
                del memory[0]
        else: # 如果在内存里
            FIFO_delete.append(0) # 无换页，用0表示
        FIFO_page.append(memory.copy()) # 记录内存状态
    return FIFO_delete, FIFO_page, error_num, error_num/pages_length
def LRU(pages, memory_size):
    # 输入举例：
    # pages =  [1,22,3,4,23,32,33]，页号
    # memory_size = 4，内存大小

    LRU_page = [] # 记录每次内存里的页号情况，如[[1],[1,2],[1,2,3]]
    LRU_delete = [] # 记录每次换掉的页号
    memory = [] # 内存
    error_num = 0 # 统计缺页率
    pages_length = len(pages) # 总页号数量
    for page in pages: # 遍历每个页号
        if page not in memory: # 如果不在内存里
            error_num += 1 # 缺页次数加一
            if len(memory) < memory_size: # 如果没超出内存大小，调入内存
                memory.append(page)
                LRU_delete.append(0)
            else: # 如果超出内存大小
                memory.append(page)
                LRU_delete.append(memory[0])
                del memory[0]
        else: # 如果在内存里，放到列表最后（因为每次换列表最前面的页号），表示使用过
            k = memory.index(page)
            temp = memory[k]
            LRU_delete.append(temp)
            del memory[k]
            memory.append(temp)
        LRU_page.append(memory.copy()) # 记录内存状态
    return LRU_delete, LRU_page, error_num, error_num/pages_length





if __name__ == '__main__':
    pages = [1,22,3,4,23,32,33]
    GUI()
    # print(FIFO(pages, 4))