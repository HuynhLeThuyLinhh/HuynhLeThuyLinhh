# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:55:44 2024

@author: DELL
"""

a = input("Nhập 1 chữ cái: ")
x = a.upper()
y = a.lower()
if a==x:
    print("Chữ cái đã nhập: ",y)
elif a==y:
    print("Chữ cái đã nhập: ",x)
else:
    print("Chữ cái đã nhập không hợp lệ.")
