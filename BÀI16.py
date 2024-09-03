# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:45:35 2024

@author: DELL
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
d = a*3600+b*60+c
print("Thời gian",f"{a}h{b}p{c}s","=",d,"giây")