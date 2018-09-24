def bubbleSort(l):
    for i in range(1,len(l)):
        flag = True
        for j in range(len(l)-i):
            if l[j] > l[j+1]:
                flag = False
                x, y = l[j], l[j+1]
                l[j+1], l[j] = x, y
        if flag:
            return l

def insertionSort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j = i - 1
        while(j>=0 and l[j] > temp):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = temp

def merge(x, y):
    z = []
    i = 0
    j = 0
    while(len(z) <= (len(x) + len(y))):
        if i < len(x) and x[i] <= y[j]:
            z.append(x[i])
            i += 1
        elif j < len(y):
            z.append(y[j])
            j += 1
    return z
    
def mergeSort(l, left, right):
    if left != right:
        mid = int((left+right) / 2)
        x = mergeSort(l, left, mid)
        y = mergeSort(l, mid+1, right)
        return merge(x, y)
    else:
        temp = []
        temp.append(l[left])
        return temp

# def quickSort(l, left, right):
#     if left >= right:
#         return
#     i = j = pivot = left
#     k = left + 1
#     while(k <= right):
#         if l[k] > l[pivot]:
#             j += 1
#         else:
#             x, y = l[i+1], l[k]
#             l[i+1], l[k] = y, x
#             i += 1
#             j += 1
#         k += 1
#     x, y = l[pivot], l[i]
#     l[pivot], l[i] = y, x
#     
#     quickSort(l, left, i-1)
#     quickSort(l, i+1, right)

def decrement(x):
    x -= 1
    return x

def partition(a, left, right):
    pivot = a[left]
    i = left
    j = right
    while(i < j):
        while(i < j):
            j -= 1
            if a[j] > pivot:
                pass
            else:
                break
        if i < j:
            a[i] = a[j]
        while(i < j):
            if a[i] < pivot:
                i += 1
                pass
            else:
                break
        if i < j:
            a[j] = a[i]
    a[i] = pivot
    return i

def quickSort(a, left, right):
    if right-left < 2:
        return
    m = partition(a, left, right)
    quickSort(a, left, m)
    quickSort(a, m+1, right)
    
l = [5,2,7,4,9,5]
quickSort(l, 0, len(l))
print(l)
            
            
    
        
    
    
    
    
    
    
    
    
    
            
            
            
                