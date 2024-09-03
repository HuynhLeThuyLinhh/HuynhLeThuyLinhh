# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:09:29 2024

@author: DELL
"""

import datetime
s = int(input("Nhập năm sinh: "))
x = datetime.date.today().year
print("Bạn sinh năm: ",s, "Vậy bạn ",x-s,"tuổi")