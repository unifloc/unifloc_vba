# -*- coding: utf-8 -*-
"""
простой тест на вызов функций unifloc VBA из python
Created on Thu Oct 10 09:59:29 2019

@author: Rinat Khabibullin
"""
import sys
sys.path.insert(0,'..')

import unifloc_vba_python_api.python_api as python_api 

UniflocVBA = python_api.API("../UniflocVBA_7.xlam")


print("done")

t = UniflocVBA.PVT_rs_m3m3(2,2)
print(t)