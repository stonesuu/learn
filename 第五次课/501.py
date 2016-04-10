# -*- coding: utf-8 -*-
'''def sort_list(l):
    tmp = l[0]
    for x in range(1,len(l)):
#        print x,l.index(8)
        if l[x] < tmp:
            l.insert(0,l.pop(x))
    return l

#l = [8,1,2,3,4,5,6,7,9,10,2,4,5,6,11,23,24,1,3,5,3]

#print sort_list(l)'''



            
'''def sort_list01(L):
    if len(L) < 2:
        return L
    else:
        tmp = L[0]
        for x in range(1,len(L)):
            if L[x] < tmp:
                L.insert(0,L.pop(x))
        ind = L.index(tmp)
        lef_list = L[:ind]
        rig_list = L[ind+1:]
        return sort_list01(lef_list) + [tmp] + sort_list01(rig_list)

print sort_list01(l)

def quick(arr,key):
    if len(arr) < 1 :
        return arr
    left = []
    right = []
    env = arr[0]
    for i in range(1,len(arr)):
        if key(arr[i]) > key(env):
            right.append(arr[i])
        else:
            left.append(arr[i])
    return quick(left,key) +[env] + quick(right,key)


def key(x):
    return x['age']
def sorted1(arr,key):
    if len(arr) < 2:
        return arr
    else:
        tmp = arr[0]
        for x in range(1,len(arr)):
            if key(arr[x]) < key(tmp):
                arr.insert(0,arr.pop(x))
        ind = arr.index(tmp)
        left_list = arr[:ind]
        right_list = arr[ind+1:]
        return sorted1(left_list,key) + [tmp] + sorted1(right_list,key)'''

'''arr = [{'name':'aa','age':9},{'name':'bb','age':8},{'name':'cc','age':7}]

#print quick(arr,key)
def count(ret,n):
    if n[0] == '+':
        return ret+int(n[1])
    elif n[0] == '-':
        return ret-int(n[1])
    elif n[0] == '*':
        return ret*int(n[1])
    else:
        return ret/int(n[1])
#print count(5,'/2')

        
def prot(L):
    if len(L) == 1:
        return int(L[0])
    else:
        return count(prot(L[:len(L)-2]),L[len(L)-2:])

def last(L):
    tmp_L = L.replace('+',' + ')
    tmp_L = tmp_L.replace('-',' - ')
    tmp_L = tmp_L.replace('*',' * ')
    tmp_L = tmp_L.replace('/',' / ')
    return prot(tmp_L.split( ))'''

arr = '11+24*15/3*4-3+116+6669-37/5'

def cal(term01,term02,n):
    if n =='+':
        return term01+term02
    elif n == '-':
        return term01-term02
    elif n== '*':
        return term01*term02
    elif n == '/':
        return term01/term02

    
def change(L):
    tmp_L = L.replace('+',' + ')
    tmp_L = tmp_L.replace('-',' - ')
    tmp_L = tmp_L.replace('*',' * ')
    tmp_L = tmp_L.replace('/',' / ')
    return tmp_L.split( )

def advChange(arr):
#    arr = arr[:]
    while '*' in arr or '/' in arr:
        for i in range(len(arr)):
            if arr[i] == '*' or arr[i] == '/':
                tmparr = [arr[i-1],arr[i],arr[i+1]]
                arr[i-1] = tmparr
                del arr[i]
                del arr[i]
                break
    return arr

'''def advChange(arr):
    arr = arr[:]
    while '*' in arr or '/' in arr:
        tmparr = []
        markindex = []
        for i in range(len(arr)):
            if arr[i] == '*' or arr[i] == '/':
                if i < len(arr)-2 and (arr[i+2] == '*' or arr[i+2] == '/') :
                    tmparr.append(arr[i-1])
                    tmparr.append(arr[i])
                    markindex.append(i-1)
                    markindex.append(i)
                else:
                    tmparr.append(arr[i-1])
                    tmparr.append(arr[i])
                    tmparr.append(arr[i+1])
                    markindex.append(i-1)
                    markindex.append(i)
                    markindex.append(i+1)
                    break
        arr[markindex[0]] = tmparr
        count = len(markindex)-1
        while count > 0:
            del arr[markindex[1]]
            count -= 1
    return arr'''
                    
                    
                
                
             

'''def langCal(arr):
    if len(arr) == 1:
        return int(arr[0])
    else:
        return cal(langCal(arr[:len(arr)-2]),int(arr[-1]),arr[-2])'''

def langCal(arr):
    if len(arr) == 1:
        if not isinstance(arr[0],list):
            return int(arr[0])
        else:
            return langCal(arr[0])
    else:
        return cal(langCal(arr[:len(arr)-2]),langCal([arr[-1]]),arr[-2])

def fina(L):
    tmp_arr = change(L)
    tmp_arr = advChange(tmp_arr)
    return langCal(tmp_arr)

ret = fina(arr)
print ret








    

        
    




        
       
