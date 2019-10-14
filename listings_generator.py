# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:57:40 2019

@author: Khabibullin Rinat

Unifloc 7 manual 
Listings generator 

Read automitically saved VBA code file and prepares code listings for manual
"""

import re
import glob
import os

file_name = ["u7_Excel_functions.txt",
             "u7_Excel_functions_ESP.txt",
             "u7_Excel_functions_GL.txt",
             "u7_Excel_functions_service.txt",
             "u7_Excel_functions_well.txt",
			 "u7_Excel_functions_curves.txt",
             "u7_Excel_functions_transient.txt"]

path_vba_txt = 'modules_txt/'
path_listings_out = 'docs/u7_vba/listings/'

class VBA_Func_Header:
    """
    class representing vba function header
    """
    def __init__(self, func_name):
        self.func_name = func_name.lstrip()
        self.str_desc = ''
        self.num_line = 0
        self.lines = []
        
    def save_lines_to_file(self, path):
        fname = path+'/'+self.func_name+".lst"
        print(fname)
        f = open(fname,"w", encoding='UTF-8')
        f.writelines(self.lines)
        f.close()
        

def process_code_file(code_file_name):
    """
    code_file_name - file with vba functions to parse
    
    generate functions list with its headers 
    and saves it to separate files
    """
    func_list = []
    
    f = open(code_file_name,"r")
    
    l = f.readlines()
    f.close()
    num_line = 0
    is_declaration = False
    # iterate through all file lines 
    for num_line in range(len(l)):
        # get new line 
        s = l[num_line].lstrip()
        # check if description start mark in place 
        start_description = re.search(r'description_to_manual',s)
        if start_description:
            print('new description start found')
            func = VBA_Func_Header("unknown")
            func_list.append(func)
            is_declaration = True
        # check if description end mark in place 
        end_description = re.search(r'description_end',s)        
        if end_description:
            is_declaration = False
        # check if there is function name in string
        search = re.search(r'(?<=Function)\s+\w+',s)
        if search and is_declaration:
            func.func_name = search[0].lstrip()
            print("Function " + func.func_name)
            

        if is_declaration:
            if not start_description:
                func.lines.append(l[num_line])
        
    
                    
    for func in func_list:
        func.save_lines_to_file(path_listings_out)
   
"""
listing generation start
extract function with description markers
"""    
for code_file in file_name:
    process_code_file(path_vba_txt + code_file)

"""
tex chapter generation start
"""
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