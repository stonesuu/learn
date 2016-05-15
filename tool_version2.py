# -*- coding: gbk -*-
'''脚本的目的：先选择时间，然后再选择该时间的目录下产生的文件名，然后从所有IP地址的目录内找到相应时间和相应
文件名的文件，再根据该文件名上指定的命令统计出需要的信息。'''
import os
date_set_dict = {} #这是日期选择字典，就是｛1：‘2016-05-12’｝
command_set_dict = {}#这是指令选择字典，就是｛1：‘10时0分0秒show version。txt’｝
addlist = []

def date_choose(main_dir):#第二部，日期选择函数
    time_set = set([])#用于去重，目的就是在addlist中选择10个IP地址，将每个IP下的日期listdir出来相互‘或’运算，得出可选则的时间。
    global date_set_dict
    #global addlist
    time_chosen_print = []#用于显示
    n = 1#字典的第一位
    #for tmp_dir in os.listdir(main_dir)[:10]:
    for tmp_dir in addlist[:10]:#只选择10个IP
        time_set = time_set | set(os.listdir(os.path.join(main_dir,tmp_dir)))#将其中的时间进行或运算
    for time in time_set:#组建date_set_dict
        date_set_dict[n] = time
        n += 1
        #print date_set_dict
    for num,time in date_set_dict.items():#组建显示的list，便于sorted排序，不然dict不好排序
        time_chosen_print.append(':'.join((str(num),time)))
    print '可选择的日期有:\n'
    for item in sorted(time_chosen_print):
        print item
    while True:#进行选择，用try特别好，随便输入什么都不报做。灵光一现
        get = raw_input('\n选择相应日期序号: ')
        try:
            int(get)
        except Exception:
            print '无效的选择，请重新输入，或输入0退出选择.\n'
        else:
            if int(get) == 0:
                return None
            elif int(get) not in date_set_dict:
                print '无效的数字，请重新输入，或输入0退出选择.\n'
            else:
                break
    return int(get)

def dir_choose():#第一步，指定文件的主目录
    global addlist #将主目录下的所有IP地址统计成一个list
    while True:
        main_dir_get = raw_input('''输入主目录(默认为'D:\ics-version') :''')
        if not main_dir_get:#如果直接回车，获得空值
            main_dir = 'D:\ics-version'#主目录为这个
        else:
            main_dir = main_dir_get#如果不是那就换成输入的值
        if str(main_dir_get) == '0':#如果主目录是‘0‘
            return None#因为输入0推出程序，看mian就知道了。
        elif os.path.exists(main_dir):#如果不是0，且存在，就用listdir将该目录下分割长度为4，前几位是10，172的东西存入addlist。因为这认为是IP地址。
            addlist = [x for x in os.listdir(main_dir) if (len(x.split('.')) == 4 and ( x[:3] == '10.' or x[:4] == '172.'))]
            if len(addlist) > 0:#如果有，则认为该目录是主目录
                return main_dir
            else:
                print '未在下一级目录发现IP地址的目录，请重新确认，或输入0退出程序。\n'
        else:
            print '该目录不存在，请重新确认，或输入0退出程序。\n'



def command_choose(main_dir,date):#第三部，选择指令，其实是文件名，因为批量产生的文件名中的时间是相同的。
    #global date_set_dict
    global command_set_dict
    #global addlist
    command_set = set([])#同样用于去重
    command_chosen_print = []#同样用于显示
    n = 1
    #path_list = [os.path.join(main_dir,x,date_set_dict[date]) for x in os.listdir(main_dir)]
    path_list = [os.path.join(main_dir,x,date_set_dict[date]) for x in addlist]#使用os.path.join在时间选择完成之后拼出目录list
    for path in path_list[:10]:#这里用的try，貌似可以不用，没有就是空值呗。
        try:
            os.listdir(path)
        except Exception:
            continue
        else:
        #command_set = command_set | set(os.listdir(path))
            command_set = command_set | set(os.listdir(path))#或运算
    for com in command_set:#组成dict
        command_set_dict[n] = com
        n += 1
    for num,com in command_set_dict.items():#组成显示用的list
        command_chosen_print.append(':'.join((str(num),com.split('.')[0])))
    print '\n\n可选择的指令有：\n'
    for item in sorted(command_chosen_print):
        print item.decode('gbk')#要注意汉字出来是编码，需要先译码
    while True:
        get = raw_input('\n选择相应指令序号: ')
        try:
            int(get)
        except Exception:
            print '无效的选择，请重新输入，或输入0退出选择.\n'
        else:
            if int(get) == 0:
                return None
            elif int(get) not in command_set_dict:
                print '无效的数字，请重新输入，或输入0退出选择.\n'
            else:
                break
    return int(get)





def sort_addlist(addlist):#NB的IP地址排序函数。先转换为（010.088.051.66，10.88.51.66）
    sortAddlist = []
    for add in addlist:
        tmplist = [x.rjust(3,'0') for x in add.split('.')]
        tmpStr = '.'.join(tmplist)
        tupItem = (tmpStr,add)
        sortAddlist.append(tupItem)
    list.sort(sortAddlist)
    return [x[1] for x in sortAddlist]
    

def show_version(main_dir,date,command):#
    #file_list = [os.path.join(main_dir,x,date_set_dict[date],command_set_dict[command]) for x in sort_addlist(addlist)]
    final_str = '%s\n\n' % date_set_dict[date]#拼接final_str
    for add in sort_addlist(addlist):
        final_str += ('%s:' % add).ljust(14)
        path = os.path.join(main_dir,add,date_set_dict[date],command_set_dict[command])#直接将目录拼接到文件名
        try:
            f = open(path)
        except Exception:
            final_str += 'file not found.'
        else:
            #tmparr = f.readlines()
            tmparr = f.read()#这里要说说，不同型号，不同版本，时间和module的行数不同。灵光一现，直接读成一个str，以需要找的名字为分界点，一分为二就ok
            f.close()
            try:
                tmparr_result01 = ('%s' % tmparr.split('Version ')[1].split(',')[0]).ljust(18)
                tmparr_result02 = ('  running time: %s' % tmparr.split('uptime is ')[1].split('\n')[0]).ljust(65)
                tmparr_result03 = ('  Module Number:%s' % tmparr.split('Model number                    :')[1].split('\n')[0])
            except:
                final_str += 'message fetch error'
            else:
                final_str += tmparr_result01+tmparr_result02+tmparr_result03

        final_str += '\n'
    t = open(r'D:\result\%s_%s'% (date_set_dict[date],command_set_dict[command]),'w') #这里要注意文件可以不存在，目录要存在。
    t.writelines(final_str) 
    t.close()
    print r"统计输出成功,文件名:'D:\result\%s_%s'" % (date_set_dict[date],command_set_dict[command])
    
            
    
                                    
                                    
    
    

        
        
        
            


if __name__ == '__main__':
    dir_choose_result = dir_choose()
    if dir_choose_result is not None:
        date_choose_result = date_choose(dir_choose_result)
        if date_choose_result is not None:
            command_choose_result = command_choose(dir_choose_result,date_choose_result)
            if command_choose_result is not None:
                if command_set_dict[command_choose_result].split(' ')[1] == 'version.txt':
                    show_version(dir_choose_result,date_choose_result,command_choose_result)
                else:
                    print '该指令尚未建立统计函数'
            else:
                pass
        else:
            pass
    else:pass
        



