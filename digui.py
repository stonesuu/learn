def find(beg,end):
    print 'begin is (%s) end is (%s)' % (beg,end)
    if (end-beg) == 1:
        print 'a',end
        return end
    else:
        tmp = (beg+end)/2
        if x == L[tmp]:
            print 'b',tmp
            return tmp
        elif x > L[tmp]:
            beg =  tmp
            find(beg,end)
        else:
            end = tmp
            find(beg,end)
    
L = [1,3,4,6,7,9,11,14,16,17,19,23,25,27,29,30,34,36,38,46,48,57,59,68,78,89,90]
x = 79

m = find(0,len(L)-1)
print m
    
