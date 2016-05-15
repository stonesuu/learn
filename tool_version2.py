# -*- coding: gbk -*-
'''�ű���Ŀ�ģ���ѡ��ʱ�䣬Ȼ����ѡ���ʱ���Ŀ¼�²������ļ�����Ȼ�������IP��ַ��Ŀ¼���ҵ���Ӧʱ�����Ӧ
�ļ������ļ����ٸ��ݸ��ļ�����ָ��������ͳ�Ƴ���Ҫ����Ϣ��'''
import os
date_set_dict = {} #��������ѡ���ֵ䣬���ǣ�1����2016-05-12����
command_set_dict = {}#����ָ��ѡ���ֵ䣬���ǣ�1����10ʱ0��0��show version��txt����
addlist = []

def date_choose(main_dir):#�ڶ���������ѡ����
    time_set = set([])#����ȥ�أ�Ŀ�ľ�����addlist��ѡ��10��IP��ַ����ÿ��IP�µ�����listdir�����໥�������㣬�ó���ѡ���ʱ�䡣
    global date_set_dict
    #global addlist
    time_chosen_print = []#������ʾ
    n = 1#�ֵ�ĵ�һλ
    #for tmp_dir in os.listdir(main_dir)[:10]:
    for tmp_dir in addlist[:10]:#ֻѡ��10��IP
        time_set = time_set | set(os.listdir(os.path.join(main_dir,tmp_dir)))#�����е�ʱ����л�����
    for time in time_set:#�齨date_set_dict
        date_set_dict[n] = time
        n += 1
        #print date_set_dict
    for num,time in date_set_dict.items():#�齨��ʾ��list������sorted���򣬲�Ȼdict��������
        time_chosen_print.append(':'.join((str(num),time)))
    print '��ѡ���������:\n'
    for item in sorted(time_chosen_print):
        print item
    while True:#����ѡ����try�ر�ã��������ʲô�������������һ��
        get = raw_input('\nѡ����Ӧ�������: ')
        try:
            int(get)
        except Exception:
            print '��Ч��ѡ�����������룬������0�˳�ѡ��.\n'
        else:
            if int(get) == 0:
                return None
            elif int(get) not in date_set_dict:
                print '��Ч�����֣����������룬������0�˳�ѡ��.\n'
            else:
                break
    return int(get)

def dir_choose():#��һ����ָ���ļ�����Ŀ¼
    global addlist #����Ŀ¼�µ�����IP��ַͳ�Ƴ�һ��list
    while True:
        main_dir_get = raw_input('''������Ŀ¼(Ĭ��Ϊ'D:\ics-version') :''')
        if not main_dir_get:#���ֱ�ӻس�����ÿ�ֵ
            main_dir = 'D:\ics-version'#��Ŀ¼Ϊ���
        else:
            main_dir = main_dir_get#��������Ǿͻ��������ֵ
        if str(main_dir_get) == '0':#�����Ŀ¼�ǡ�0��
            return None#��Ϊ����0�Ƴ����򣬿�mian��֪���ˡ�
        elif os.path.exists(main_dir):#�������0���Ҵ��ڣ�����listdir����Ŀ¼�·ָ��Ϊ4��ǰ��λ��10��172�Ķ�������addlist����Ϊ����Ϊ��IP��ַ��
            addlist = [x for x in os.listdir(main_dir) if (len(x.split('.')) == 4 and ( x[:3] == '10.' or x[:4] == '172.'))]
            if len(addlist) > 0:#����У�����Ϊ��Ŀ¼����Ŀ¼
                return main_dir
            else:
                print 'δ����һ��Ŀ¼����IP��ַ��Ŀ¼��������ȷ�ϣ�������0�˳�����\n'
        else:
            print '��Ŀ¼�����ڣ�������ȷ�ϣ�������0�˳�����\n'



def command_choose(main_dir,date):#��������ѡ��ָ���ʵ���ļ�������Ϊ�����������ļ����е�ʱ������ͬ�ġ�
    #global date_set_dict
    global command_set_dict
    #global addlist
    command_set = set([])#ͬ������ȥ��
    command_chosen_print = []#ͬ��������ʾ
    n = 1
    #path_list = [os.path.join(main_dir,x,date_set_dict[date]) for x in os.listdir(main_dir)]
    path_list = [os.path.join(main_dir,x,date_set_dict[date]) for x in addlist]#ʹ��os.path.join��ʱ��ѡ�����֮��ƴ��Ŀ¼list
    for path in path_list[:10]:#�����õ�try��ò�ƿ��Բ��ã�û�о��ǿ�ֵ�¡�
        try:
            os.listdir(path)
        except Exception:
            continue
        else:
        #command_set = command_set | set(os.listdir(path))
            command_set = command_set | set(os.listdir(path))#������
    for com in command_set:#���dict
        command_set_dict[n] = com
        n += 1
    for num,com in command_set_dict.items():#�����ʾ�õ�list
        command_chosen_print.append(':'.join((str(num),com.split('.')[0])))
    print '\n\n��ѡ���ָ���У�\n'
    for item in sorted(command_chosen_print):
        print item.decode('gbk')#Ҫע�⺺�ֳ����Ǳ��룬��Ҫ������
    while True:
        get = raw_input('\nѡ����Ӧָ�����: ')
        try:
            int(get)
        except Exception:
            print '��Ч��ѡ�����������룬������0�˳�ѡ��.\n'
        else:
            if int(get) == 0:
                return None
            elif int(get) not in command_set_dict:
                print '��Ч�����֣����������룬������0�˳�ѡ��.\n'
            else:
                break
    return int(get)





def sort_addlist(addlist):#NB��IP��ַ����������ת��Ϊ��010.088.051.66��10.88.51.66��
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
    final_str = '%s\n\n' % date_set_dict[date]#ƴ��final_str
    for add in sort_addlist(addlist):
        final_str += ('%s:' % add).ljust(14)
        path = os.path.join(main_dir,add,date_set_dict[date],command_set_dict[command])#ֱ�ӽ�Ŀ¼ƴ�ӵ��ļ���
        try:
            f = open(path)
        except Exception:
            final_str += 'file not found.'
        else:
            #tmparr = f.readlines()
            tmparr = f.read()#����Ҫ˵˵����ͬ�ͺţ���ͬ�汾��ʱ���module��������ͬ�����һ�֣�ֱ�Ӷ���һ��str������Ҫ�ҵ�����Ϊ�ֽ�㣬һ��Ϊ����ok
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
    t = open(r'D:\result\%s_%s'% (date_set_dict[date],command_set_dict[command]),'w') #����Ҫע���ļ����Բ����ڣ�Ŀ¼Ҫ���ڡ�
    t.writelines(final_str) 
    t.close()
    print r"ͳ������ɹ�,�ļ���:'D:\result\%s_%s'" % (date_set_dict[date],command_set_dict[command])
    
            
    
                                    
                                    
    
    

        
        
        
            


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
                    print '��ָ����δ����ͳ�ƺ���'
            else:
                pass
        else:
            pass
    else:pass
        



