# -*- coding:utf-8 -*-


def hanluo(n, A, B, C, count=0):
    count += 1
    if n == 1:
        print '从%s到%s移动%s' % (A, C, n)
    else:
        hanluo(n-1, A, C, B, count)
        print n
        print '从%s到%s移动%s' % (A, C, n)
        hanluo(n-1, B, A, C, count)
    print count
n = input('请输入方块数：')
hanluo(n, 'A', 'B', 'C')