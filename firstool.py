# -*- coding: gbk -*-
import os
def tongji(timechosen,destFile,addlist):
    lastStr = '%s\n\n' % timechosen
    for add in addlist:
        lastStr += '''%s:\n''' % (add,)
        filePath = 'D:\文件\%s\%s' % (add,timechosen)
        for fil in os.listdir(filePath):
            if ('%s' % fil).split( )[1] == 'version.txt':
                f = open('%s' % os.path.join(filePath,fil))
                tmparr = f.readlines()
                f.close()
                lastStr += '%s\n' % tmparr[1].split(', ')[2]
                lastStr += '%s\n\n' % tmparr[8].split('is ')[1]
    t = open(destFile,'w')
    t.write(lastStr)
    t.close()
    print '统计文件已经产生，路径为%s' % destFile

timechosen = raw_input('输入日期（如2016-04-10）： ')
destFile = raw_input('输入统计文件生成路径（如D:\destfile.txt)： ')
print '这个版本地址是固定的。'
addlist = ['10.66.1.%s' % x for x in range(3,11)]
tongji(timechosen,destFile,addlist)



    

