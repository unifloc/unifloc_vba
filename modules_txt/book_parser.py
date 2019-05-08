# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:57:40 2019

@author: khabi

book parser 
read automitically saved code file VBA and prepares code listings for manual
"""

import re

file_name = ["u7_Excel_functions.txt",
             "u7_Excel_functions_ESP.txt",
             "u7_Excel_functions_GL.txt",
             "u7_Excel_functions_service.txt",
             "u7_Excel_functions_well.txt"]

class VBA_Func_Header:
    """
    class representing vba fynction header
    """
    def __init__(self, func_name):
        self.func_name = func_name.lstrip()
        self.str_desc = ''
        self.num_line = 0
        self.lines = []
        
    def save_lines_to_file(self, path):
        fname = path+'/'+self.func_name+".lst"
        print(fname)
        f = open(fname,"w")
        f.writelines(self.lines)
        f.close()
        
def process_code_file(code_file_name):
    """
    functions list
    """
    func_list = []
    
    f = open(code_file_name,"r")
    
    l = f.readlines()
    f.close()
    num_line = 0
    found_func = False
    is_declaration = False
    
    for num_line in range(len(l)):
        s = l[num_line].lstrip()
        search = re.search(r'(?<=Function)\s+\w+',s)
        if search:
            func = VBA_Func_Header(search[0])
            func_list.append(func)
            str_desc = l[num_line-1].lstrip()
            func.str_desc = (str_desc if str_desc[0]=='\'' else ' ')
            func.num_line = num_line
            func.lines.append(func.str_desc)
            func.lines.append(s)
            found_func = True
            is_declaration = True
        else:
            if found_func:
                if is_declaration:
                    func.lines.append(l[num_line])
                    is_declaration = False if (len(s) > 0 and s[0] == '\'') else True             
                else:
                    found_func = False if (len(s) > 0 and not s[0] == '\'') else True
                    if found_func: 
                        func.lines.append(l[num_line])
    
                    
    for func in func_list:
        func.save_lines_to_file('out')
    
for code_file in file_name:
    process_code_file(code_file)
