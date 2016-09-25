# -*- coding:utf-8 -*-


def maopao(a):

    for i in range(len(a) - 1, 1, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print a

a = [2, 1, 9, 4, 3, 5, 7, 6]
maopao(a)


def charu(a):

    pass