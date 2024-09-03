# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:38:55 2024

@author: DELL
"""

N = int(input("Nhập biển số xe (gồm 4 chữ số): "))
a = N // 1000
b = (N-a*1000)//100
c = (N-a*1000-b*100)//10
d = N-a*1000- b*100- c*10
print("Số nút của xe bạn: ",a + b + c + d)