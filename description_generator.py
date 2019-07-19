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
             "u7_Excel_functions_curves.txt"]

path_vba_txt = 'modules_txt/'
path_listings_out = 'try_doc2/'

file_name_for_report_str = "report"
file_name_for_all_stuff = "all_stuff"

"""
string for specific VBA format of description
"""
start_string = "    Application.MacroOptions _\n"
almost_end_string =", _\n"
connect_to_next_string = " & _\n"
macro_string = "        Macro:="
description_string = "      Description:="
category_string = "     Category:=\"u7\",_\n"
argument_descriptions_string ="     ArgumentDescriptions:=Array("
connect_to_next_string_in_array = ",  _\n"



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
        """
        create .txt files with one functions descriptions and all_stuff.txt with all functions descriptions
        :param path:
        :return: None
        """
        fname = path + '/' + self.func_name + ".txt"
        fname2 = path + '/' + file_name_for_all_stuff + ".txt"
        print(fname)
        f = open(fname, "w", encoding='UTF-8')
        result_lines = self.lines

        """
        start addition in report file
        """
        report = "Отчет по функции " + self.func_name + " \n "
        """
        addition of start string - 1 line
        """
        result_lines.insert(0,start_string)

        """
        addition of 2th string - 2 line - with function name
        """
        result_lines.insert(1, macro_string + "\""  + self.func_name + "\"" + almost_end_string)

        """
        preparing and editing of short function description above declaration of function
        """
        string_contain_function = False
        string_number = 2
        description_string_lines = description_string
        while string_contain_function == False:
            math_object = re.search(r'Function',result_lines[string_number])
            if math_object != None:
                string_contain_function = True
            if not string_contain_function:
                current_addition = result_lines[string_number]
                current_addition = "\"" + current_addition
                current_addition = current_addition.replace("\n", "\"" + connect_to_next_string)

                description_string_lines += current_addition

                string_number += 1
            else:
                last_addition_with_end = current_addition
                last_addition_with_end = last_addition_with_end.replace(connect_to_next_string, almost_end_string)
                description_string_lines = description_string_lines.replace(current_addition,last_addition_with_end)

        """
        addition of function description in 3th line
        """
        result_lines.insert(2, description_string_lines)

        """
        deleting of unedited short description
        """
        string_to_del = string_number - 2
        for i in range(string_to_del):
            result_lines.pop(3)

        """
        addition of category string in 4th line
        """
        result_lines.insert(3, category_string)


        """
        beginning of work with description of argument for 5th line
        """

        """
        creating of string, contained parametrs devided by decimal (,) delimetr
        """
        string_contain_end_of_parametrs = False
        string_number = 4
        sting_with_parametrs_and_delimetr = ""

        """
        list of pattern, that will be deleted in sting
        """
        not_nedeed_in_string = [self.func_name, "ByVal","-1", "const", "Optional", "Double", "Integer",
                                "String", "Public", " As ", "Function", " _ ", " ", "=",  "\n", "\' ", "(_",
                                "PVT_DEFAULT", "H_CORRELATION "]
        last_step = 0
        while string_contain_end_of_parametrs == False:
            math_object = re.search(r'\)', result_lines[string_number])
            if math_object != None:
                string_contain_end_of_parametrs = True
                last_step += 1
            if not string_contain_end_of_parametrs or last_step == 1:
                if last_step == 1:
                    last_step += 1
                current_addition = result_lines[string_number]
                all_const_deleted = False
                while not all_const_deleted:
                    this_const_deleted = False
                    position_equal = current_addition.find("=")
                    if position_equal == (-1):
                        all_const_deleted = True
                    else:
                        position_next = position_equal + 1
                        while not this_const_deleted:
                            if current_addition[position_next] == "," or current_addition[position_next] == ")" or current_addition[position_next] == "\n":
                                slice_to_delete = current_addition[position_equal:position_next]
                                current_addition = current_addition.replace(slice_to_delete,"")
                                this_const_deleted = True
                            else:
                                this_symbol = current_addition[position_next]

                                position_next +=1



                for i in not_nedeed_in_string:

                    current_addition = current_addition.replace(i, "")
                sting_with_parametrs_and_delimetr += current_addition

                string_number += 1

        sting_with_parametrs_and_delimetr = sting_with_parametrs_and_delimetr.replace(",_",",")
        sting_with_parametrs_and_delimetr = sting_with_parametrs_and_delimetr.replace("(","")
        sting_with_parametrs_and_delimetr = sting_with_parametrs_and_delimetr.replace(")", "")

        """
        extract names of parametrs from string to list
        """
        list_of_names_parametr = sting_with_parametrs_and_delimetr.split(",")

        """
        write number of parametrs in report
        """
        report += "Количество параметров в функции = " + str(len(list_of_names_parametr)) + " \n "
        parametrs_in_report = sting_with_parametrs_and_delimetr.replace(",", ", ")
        report += "Строка параметров:" + parametrs_in_report + " \n "

        """
        preparing and editing description of parametrs for 5th lines
        """
        argument_descriptions_string_with_stuff = argument_descriptions_string
        for i in list_of_names_parametr:
            parametr_writed = False
            start_string_number = string_number
            current_string_number = start_string_number
            last_number =  (len(result_lines) - 1)
            while not parametr_writed and current_string_number <= last_number:
                current_string = result_lines[current_string_number]
                lower_name = i.lower()
                lower_current_string = current_string.lower()
                position_equal = lower_current_string.find(lower_name)
                if current_string_number == last_number:
                    current_addition = "\"" + lower_name +"\"" + connect_to_next_string_in_array
                    argument_descriptions_string_with_stuff += current_addition
                    parametr_writed = True
                if position_equal != (-1):
                    current_addition = "\"" + lower_current_string
                    current_addition = current_addition.replace("\n", "\"" + connect_to_next_string_in_array)
                    argument_descriptions_string_with_stuff += current_addition
                    parametr_writed = True
                current_string_number += 1

        last_addition_with_end = current_addition
        last_addition_with_end = last_addition_with_end.replace(connect_to_next_string_in_array, ") \n")

        argument_descriptions_string_with_stuff = argument_descriptions_string_with_stuff.replace(current_addition, last_addition_with_end +"\n")

        """
        insert finished 5th line 
        """
        result_lines.insert(4, argument_descriptions_string_with_stuff)


        """
        deleting of last lines
        """
        for i in range(5,last_number+2):
            result_lines.pop(5)

        """
        deleting last symbols, that are not needed 
        """
        k = 0
        for i in result_lines:
            result_lines[k] = i.replace("\' ","")
            k +=1

        """
        addition function in needed format in overall file by append
        """
        f2 = open(fname2, "a", encoding='UTF-8')
        f2.writelines(result_lines)
        f2.close()

        """
        addition in report file
        """
        report += " \n "
        fname_report = path_listings_out + '/' + file_name_for_report_str + ".txt"
        f3_report = open(fname_report, "a", encoding='UTF-8')
        f3_report.writelines([report])
        f3_report.close()


        """
        create file with one function in needed format
        """
        f.writelines(result_lines)
        f.close()


def process_code_file(code_file_name):
    """
    code_file_name - file with vba functions to parse

    generate functions list with its headers 
    and saves it to separate files
    """
    func_list = []

    f = open(code_file_name, "r")

    l = f.readlines()
    f.close()
    num_line = 0
    is_declaration = False
    # iterate through all file lines 
    for num_line in range(len(l)):
        # get new line 
        s = l[num_line].lstrip()
        # check if description start mark in place 
        start_description = re.search(r'description_to_manual', s)
        if start_description:
            print('new description start found')
            func = VBA_Func_Header("unknown")
            func_list.append(func)
            is_declaration = True
        # check if description end mark in place 
        end_description = re.search(r'description_end', s)
        if end_description:
            is_declaration = False
        # check if there is function name in string
        search = re.search(r'(?<=Function)\s+\w+', s)
        if search and is_declaration:
            func.func_name = search[0].lstrip()
            print("Function " + func.func_name)

        if is_declaration:
            if not start_description:
                func.lines.append(l[num_line])

    for func in func_list:
        func.save_lines_to_file(path_listings_out)


"""
create file for future edited text and clear it
"""
fname2 = path_listings_out + '/' + file_name_for_all_stuff + ".txt"
f2 = open(fname2, "w", encoding='UTF-8')
f2.writelines([""])
f2.close()

"""
crealte file for reports and clear it
"""
fname_report = path_listings_out + '/' + file_name_for_report_str + ".txt"
f3_report = open(fname_report, "w", encoding='UTF-8')
f3_report.writelines([""])
f3_report.close()

"""
listing generation start
extract function with description markers
and edited it by format
"""
for code_file in file_name:
    process_code_file(path_vba_txt + code_file)