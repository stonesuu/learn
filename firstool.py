# -*- coding: gbk -*-
import os
def tongji(timechosen,addlist,destFile = 'D:\destfile.txt'):
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

addlist = ['10.66.1.%s' % x for x in range(3,11)]
timechosen = raw_input('输入日期（如2016-04-10）： ').strip( )
destFile = raw_input('输入统计文件生成路径（默认为D:\destfile.txt)： ').strip( )
if not destFile == '':
    destDir = os.path.split(destFile)[0]
    if not os.path.exists(destDir):
        os.system('mkdir %s' % destDir)
    tongji(timechosen,addlist,destFile)
    print '统计文件已经产生，路径为%s' % destFile
else:
    tongji(timechosen,addlist)
    print '统计文件已经产生，路径为D:\destfile.txt'


    

