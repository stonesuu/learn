# -*- coding: utf-8 -*-
arr = [9,112,21,23,24,32,12,45,22,2123,45,32,445,32,44,553,222,434,7,3,2,6,5,8,5,23,4,6,8,3,1,4,65,8,9,6,4,32,3,4,56,8,6,3,2,1,5,6,12,23,34,21]
def quickSort(L,begin,end):
    if end - begin == 1:
        if L[begin] > L[end]:
            L[begin],L[end] = L[end],L[begin]
            return L
        else:
            return L
    else:
        tmp = L[begin]
        i = begin + 1
        j = end
        divi = 0
        while True:
            while L[i] <= tmp and i < end:
                i += 1
            while L[j] > tmp and j > begin +1:
                j -= 1
            if j < i:
                L[begin],L[i-1] = L[i-1],L[begin]
                divi = i-1
                break
            elif i == end and j==end:
                L[begin],L[end] = L[end],L[begin]
                divi = end
                break
            elif i == begin+1 and j == begin+1:
                divi = begin
                break
            else:
                L[i],L[j] = L[j],L[i]
        if end-begin == 2:
            return L
        elif divi == end:
            quickSort(L,begin,end-1)
            return L
        elif divi == begin:
            quickSort(L,divi+1,end)
            return L
        else:
            quickSort(L,begin,divi-1)
            quickSort(L,divi+1,end)
            return L
    
quickSort(arr,0,len(arr)-1)
print arr

        
    
    
