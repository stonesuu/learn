# -*- coding: gbk -*- 
import os
def addSort(addlist):
    sortAddlist = []
    for add in addlist:
        tmplist = [x.rjust(3,'0') for x in add.split('.')]
        tmpStr = '.'.join(tmplist)
        tupItem = (tmpStr,add)
        sortAddlist.append(tupItem)
    list.sort(sortAddlist)
    return [x[1] for x in sortAddlist]

def static(timechosen,addlist,destFile = 'D:\destfile.txt'):
    lastStr = '%s\n\n' % timechosen  
    for add in addlist: 
        lastStr += ('''%s:''' % (add,)).ljust(14) 
        filePath = 'D:\ZOneSoftware\SGICS_V4.0\SystemFileStorage\exeResultPath\%s\%s' % (add,timechosen)
        filexist = os.path.exists(filePath)
        if filexist == True:
            for fil in os.listdir(filePath): 
                if ('%s' % fil).split( )[1] == 'version.txt': 
                    f = open('%s' % os.path.join(filePath,fil)) 
                    tmparr = f.readlines() 
                    f.close() 
                    lastStr += ('%s' % tmparr[1].split(', ')[2]).ljust(21) 
                    lastStr += ('  running time: %s' % tmparr[8].split('is ')[1]).strip('\n')
        else:
            lastStr += 'the file is not exist'
        lastStr += '\n'
    #staList = lastStr.split('\n')[2:]
    #print staList[:10]
    t = open(destFile,'w') 
    t.writelines(lastStr) 
    t.close() 
 
 
#addlist = ['10.66.1.%s' % x for x in range(1,23)]
addlist = [x for x in os.listdir('D:\ZOneSoftware\SGICS_V4.0\SystemFileStorage\exeResultPath') if (x[:3] == '10.' or x[:4] == '172.')]
timechosen = raw_input('输入日期（如2016-04-10）： ').strip( ) 
destFile = raw_input('输入统计文件生成路径（默认为D:\destfile.txt)： ').strip( ) 
if not destFile == '': 
    destDir = os.path.split(destFile)[0] 
    if not os.path.exists(destDir): 
        os.system('mkdir %s' % destDir) 
    static(timechosen,addSort(addlist),destFile) 
    print '统计文件已经产生，路径为%s' % destFile 
else: 
    static(timechosen,addSort(addlist)) 
    print '统计文件已经产生，路径为D:\destfile.txt'


