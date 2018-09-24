ip = [int(x) for x in input().split()] 

def createFenwickTree(ip):
    ft = [0] * (len(ip)+1)
    ft[0] = 0
    t = 0
    for x in ip:
        p = t + 1
        while(1):
            ft[p] += x
            p += p & (-p)
            if p > (len(ft)-1):
                break
        t += 1
    return ft

def updateFenwickTree(ft, val, index, ip):
    diff = val - ip[index]
    ip[index] = val
    start = index + 1
    while(1):
        ft[start] += diff
        start += start & (-start)
        if start > (len(ft)-1):
            break
    return ft

def getRangeSumQuery(left, right, ft):
    p = right + 1
    upper = 0
    lower = 0
    while(p > 0):
        upper += ft[p]
        p -= p & (-p)
    p = left
    while(p > 0):
        lower += ft[p]
        p -= p & (-p)
    return upper - lower

ft = createFenwickTree(ip)
print(getRangeSumQuery(2, 3, ft))
ft = updateFenwickTree(ft, 8, 3, ip)
print(getRangeSumQuery(2, 3, ft))
print(ip)