#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def add():
    name = input("Название пункта?")
    no = input("Номер поезда")
    time_str = input("Время?\n")
    t = time.strptime(time_str, "%H:%M")
    return {
        "name": name,
        "no": no,
        "t": t,
    }
