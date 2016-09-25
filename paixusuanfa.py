# -*- coding:utf-8 -*-
import time


def maopao(a):
    start_time = time.time()*1000
    x = len(a)
    for i in range(len(a)-1):
        for j in range(x-2, i-1, -1):
            if a[j+1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    use_time = time.time()*1000 - start_time
    print '1 冒泡排序: ',a,'\n', '使用时间: ', '%s ms' % use_time


def charu(a):
    start_time = time.time()*1000
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j-1] > a[i]:
            j -= 1
        a.insert(j, a[i])
        a.pop(i+1)
    use_time = time.time()*1000 - start_time
    print '2 插入排序: ',a, '\n', '使用时间: ', '%s ms' % use_time


def kuaisu(a):
    star_time = time.time()*1000

    def quick(a):
        if len(a) <= 1:
            return a
        x = len(a)
        i = 0
        flag = a[i]
        for j in range(1, x):
            if a[j] < flag:
                flag = a[j]
                a.insert(0, flag)
                a.pop(j+1)
                i += 1
        a1 = a[:i]
        a2 = a[i+1:]
        a = quick(a1)
        a.append(flag)
        a.extend(quick(a2))
        return a
    use_time = time.time()*1000 - star_time
    print '3 快速排序: ',quick(a), '\n', '使用时间: ', '%s ms' % use_time

if __name__ == '__main__':
    x = [5,4,3,2,1]
    kuaisu(x)

