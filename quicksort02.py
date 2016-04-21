arr = [10,9,112,21,23,24,32,12,45,22,2123,45,32,445,32,44,553,222,434,7,3,2,6,5,8,5,23,4,6,8,3,1,4,65,8,9,6,4,32,3,4,56,8,6,3,2,1,5,6,12,23,34,21]
count = 0
def quicksort(l,begin,end):
    global count
    if end-begin <= 1:
        if l[begin] > l[end]:
            count += 1
            l[begin],l[end] = l[end],l[begin]
    else:
        compare = l[begin]
        i = begin +1
        j = end
        while True:
            while l[i] <= compare and i< end:
                i += 1
            while l[j] > compare and j > begin+1:
                j -= 1
            if i < j:
                count += 1
                l[i],l[j] = l[j],l[i]
            elif i > j:
                count += 1
                l[begin],l[i-1] = l[i-1],l[begin]
                quicksort(l,begin,i-2)
                quicksort(l,i,end)
                break
            elif i ==begin+1:
                quicksort(l,i,end)
                break
            elif j == end:
                count += 1
                l[begin],l[end] = l[end],l[begin]
                quicksort(l,begin,j-1)
                break
quicksort(arr,0,len(arr)-1)

print arr
print count


            
                
            
            
        
