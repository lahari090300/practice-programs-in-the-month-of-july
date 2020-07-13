def partition(list1,first,last):
    pivot=list1[first]
    left=first+1 
    right=last
    while True:
        while((left<=right) and (list1[left]<=pivot)):
            left=left+1 
        while((left<=right) and (list1[right]>=pivot)):
            right=right-1
        if right<left:
            break 
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def qsort(list1,first,last):
    if len(list1)==1:
        return list1
    if len(list1)==0:
        return []
    if first<last:
        pivot_index_place=partition(list1,first,last)
        qsort(list1,first,pivot_index_place-1)
        qsort(list1,pivot_index_place+1,last)
        
list1=[56,34,8,7,3,45]
qsort(list1,0,len(list1)-1)
print(list1)
