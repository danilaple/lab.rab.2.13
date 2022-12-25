#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def fun1(type):
        def fun2(spisok):
            if type == list:
                return list(map(int, spisok.split()))
            return tuple(map(int, spisok.split()))
        return fun2 
