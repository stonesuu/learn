# -*- coding: gbk -*-
import os
def tongji(timechosen,addlist,destFile = 'D:\destfile.txt'):
    lastStr = '%s\n\n' % timechosen
    for add in addlist:
        lastStr += '''%s:\n''' % (add,)
        filePath = 'D:\�ļ�\%s\%s' % (add,timechosen)
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
timechosen = raw_input('�������ڣ���2016-04-10���� ').strip( )
destFile = raw_input('����ͳ���ļ�����·����Ĭ��ΪD:\destfile.txt)�� ').strip( )
if not destFile == '':
    destDir = os.path.split(destFile)[0]
    if not os.path.exists(destDir):
        os.system('mkdir %s' % destDir)
    tongji(timechosen,addlist,destFile)
    print 'ͳ���ļ��Ѿ�������·��Ϊ%s' % destFile
else:
    tongji(timechosen,addlist)
    print 'ͳ���ļ��Ѿ�������·��ΪD:\destfile.txt'


    

