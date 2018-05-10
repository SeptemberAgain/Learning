import time
from numpy import random


# 冒泡排序
def bubble(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
        # print('Then:', a)
    return a


# 选择排序
def select(a):
    for i in range(0, len(a) - 1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        # print('Then:', a)
    return a

# 插入排序
def insert(a):
    for i in range(0, len(a)-1):
        for j in range(i+1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        # print('Then:', a)
    return a


# 希尔排序
def shell(a):
    gap = round(len(a)/2)
    while gap > 0:
        for i in range(gap, len(a)):
            j = i
            temp = a[i]
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = temp
        # print('Then:', a)
        gap = round(gap/2)
    return a


# 归并排序(细分)
def merge(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    list1 = merge(a[:mid])
    list2 = merge(a[mid:])
    return unite(list1, list2)

# 归并排序(重组)
def unite(list1, list2):
    i = 0
    j = 0
    result = []
    while i<len(list1) and j<len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1
    result += list1[i:] + list2[j:]
    return result

# 快速排序
def quick(a, start, end):
    if start < end:
        i = start
        j = end
        while j > i:
            while j > i and a[j] >= a[start]:
                j -= 1
            while j > i and a[i] <= a[start]:
                i += 1
            a[i], a[j] = a[j], a[i]
        a[start], a[i] = a[i], a[start]
        quick(a, start, i-1)
        quick(a, j+1, end)
    return a


# 堆排序(总)
def heap(a):
    size = len(a)
    createheap(a, size)
    for i in range(size-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        handleheap(a, 0, i)
    return a


# 堆排序(创建堆)
def createheap(a, size):
    for i in range(int(size/2)-1, -1, -1):
        handleheap(a, i, size)


# 堆排序(处理堆)
def handleheap(a, i, size):
    left = 2*i + 1
    right = 2*i + 2
    peak = i
    if i <= int(size/2)-1:
        if left < size and a[left] > a[peak]:
            peak = left
        if right < size and a[right] > a[peak]:
            peak = right
        if peak != i:
            a[i], a[peak] = a[peak], a[i]
            handleheap(a, peak, size)


# 计数排序
def counting(a):
    max = min = a[0]
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
        elif min > a[i]:
            min = a[i]
    b = [0]*(max-min+1)
    c = []
    for i in range(0, len(a)):
        b[a[i]-min] += 1
    for i in range(max-min+1):
        while b[i] > 0:
            b[i] -= 1
            c.append(i+min)
    return c


# 桶排序
def bucket(a):
    n = 10
    b = [[] for _ in range(0, n)]
    result = []
    for i in range(0, n):
        b[int(a[i]*n)].append(a[i])
    for i in range(0, n):
        quick(b[i], 0, len(b[i])-1)
        for j in range(0, len(b[i])):
            result.append(b[i][j])
    return result


# 基数排序
def base(a):
    for k in range(4):  # 4轮排序
        s = [[] for _ in range(10)]
        for i in a:
            s[i // (10 ** k) - (i // (10 ** (k+1)))*10].append(i)
        a = [a for b in s for a in b]
    return a


# 主函数
def main():
    a = [7, 12, 454, 23, 3, 6, 11, 17, 76, 22, 34, 100, 1, 7, 9]
    x = random.rand(15)
    A = [random.randint(1, 9999) for i in range(15)]
    print('Brfore:', a)
    end = time.clock()
    print('Now:', bubble(a),'time used for bubble: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', select(a), 'time used for select: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', insert(a), 'time used for insert: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', shell(a), 'time used for shell: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', merge(a), 'time used for merge: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', quick(a, 0, len(a)-1), 'time used for quick: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', heap(a), 'time used for heap: %.2es' %(time.clock() - end))
    end = time.clock()
    print('Now:', counting(a), 'time used for counting: %.2es' %(time.clock() - end))
    end = time.clock()
    print()
    print('Brfore:', x)
    print('Now:', bucket(x),'time used for bucket: %.2es' %(time.clock() - end))
    end = time.clock()
    print()
    print('Brfore:', A)
    print('Now:', base(A),'time used for base: %.2es' %(time.clock() - end))

if __name__ == '__main__':
    main()