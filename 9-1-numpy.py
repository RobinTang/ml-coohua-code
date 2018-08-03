# -*- coding: utf-8 -*-
"""
 @desc:
 @author: tyh
 @contact: yhtang10@gmail.com
 @software: PyCharm   
 @time: 2018/08/03
"""

import numpy as np

arr = np.arange(1e7)
larr = arr.tolist()

def list_time(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar

    return alist


from scipy.interpolate import interp1d
x = np.linspace(0, 10*np.pi, 20),
y = np.cos(x)
fl = interp1d(x, y, kind='linear')

xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
