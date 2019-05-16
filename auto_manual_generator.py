# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:34:07 2019

@author: Rinat Khabibullin
"""
import glob
import os

path_func_files = "docs/u7_vba/listings/"
files = glob.glob(path_func_files+"*.lst")
print(files)

ls = []

for file in files:
    f = open(file,"r", encoding='UTF-8')
    l = f.readlines()
    f.close()
    fname_ext = os.path.basename(file)
    fname = os.path.splitext(fname_ext)[0]
    ls.append(r"\section{"+fname.replace('_','\_')+"}"+'\n')
    ls.append(r"\putlisting{listings/"+fname_ext+"}"+'\n')
    
print(ls)

f = open("docs/u7_vba/text/auto.tex","w", encoding='UTF-8')
f.writelines(ls)
f.close()