# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:57:40 2019

@author: Khabibullin Rinat

Unifloc 7 manual 
Listings generator 

Read automitically saved VBA code file and prepares code code descriptions
used in VBA as promt helpers
generate /description_generated/u7_descriptions.txt which is read by VBA
also generate python_api.py file 
"""

# TODO где " имя параметра" используется для "имя параметра2" возникает неправильное определение нескольких строк
# TODO перевод в нижний регистр позволяет все прочитать без ошибок, но если заккомитить .lower() можно будет переименовать переменные
import re



file_name = ["u7_Excel_functions.txt",
             "u7_Excel_functions_well.txt",
             "u7_Excel_functions_Jet.txt",
             "u7_Excel_functions_service.txt",
             "u7_Excel_functions_crv.txt",
             "u7_Excel_functions_transient.txt"]

path_vba_txt = 'modules_txt/'
path_listings_out = 'description_generated/'
path_python_api_out = 'unifloc_vba_python_api/'
start_string_for_module = "' автоматически сгенерированное описание функций unifloc VBA \n" \
                          "' description_generator.py использован для генерации. \n " \
                          "Option Explicit \n Sub Set_Descriptions() \n On Error Resume Next \n"
end_string_for_module = "End Sub"

file_name_for_report_str = "report"
file_name_for_all_stuff = "all_stuff"
file_name_for_description_module = "u7_descriptions"
file_name_for_python_api = "python_api.py"

"""
string for specific VBA format of description
"""
start_string = "    Application.MacroOptions _\n"
almost_end_string = ", _\n"
macro_string                 = "        Macro:="
description_string           = "        Description:="
category_string              = "        Category:=\"u7\", _\n"
argument_descriptions_string = "        ArgumentDescriptions:=Array("
connect_to_next_string_in_array = ", _\n"
"""
strings for python API
"""
tab_str = "    "
start_classes_str = "import xlwings as xw\n" \
                    "addin_name_str = \"UniflocVBA_7.xlam\"\n" \
                    "class API():\n" \
                    "" + tab_str + "def __init__(self, addin_name_str):\n" \
                    "" + 2 * tab_str + "self.book = xw.Book(addin_name_str)\n"
                    
create_class_str = "#UniflocVBA = API(addin_name_str)\n"

api_const_string = "H_CORRELATION = 0 # 0 - BeggsBrill, 1 - Ansari and so on \n" \
                   "PVT_CORRELATION = 0 # 0 -Standing, 1 -McCain, 2 - linear \n" \
                   "PVT_DEFAULT = \"gamma_gas:0,900;gamma_oil:0,750;gamma_wat:1,000;rsb_m3m3:100,000;rp_m3m3:-1,000;pb_atma:-1,000;tres_C:90,000;bob_m3m3:-1,000;muob_cP:-1,000;PVTcorr:0;ksep_fr:0,000;pksep_atma:-1,000;tksep_C:-1,000; \" \n" \
                   "ESP_DEFAULT = \"ESP_ID:1006.00000;HeadNom_m:2000.00000;ESPfreq_Hz:50.00000;ESP_U_V:1000.00000;MotorPowerNom_kW:30.00000;Tintake_C:85.00000;t_dis_C:25.00000;KsepGS_fr:0.00000;ESP_energy_fact_Whday:0.00000;ESP_cable_type:0;ESP_Hmes_m:0.00000;ESP_gas_degradation_type:0;c_calibr_head:0.00000;PKV_work_min:-1,00000;PKV_stop_min:-1,00000;\"\n" \
                   "WELL_DEFAULT = \"hperf_m:2000,00000;hpump_m:1800,00000;udl_m:0,00000;d_cas_mm:150,00000;dtub_mm:72,00000;dchoke_mm:15,00000;roughness_m:0,00010;tbh_C:85,00000;twh_C:25,00000;\"\n" \
                   "WELL_GL_DEFAULT = \"hperf_m:2500,00000;htub_m:2000,00000;udl_m:0,00000;d_cas_mm:125,00000;dtub_mm:62,00000;dchoke_mm:15,00000;roughness_m:0,00010;tbh_C:100,00000;twh_C:50,00000;GLV:1;H_glv_m:1500,000;d_glv_mm:5,000;p_glv_atma:50,000;\"\n" \
                   "const_gg_ = 0.6 \n" \
                   "const_gw_ = 1 \n" \
                   "const_go_ = 0.86 \n" \
                   "const_sigma_wat_gas_Nm = 0.01 \n" \
                   "const_sigma_oil_Nm = 0.025 \n" \
                   "const_mu_w = 0.36\n" \
                   "const_mu_g = 0.0122 \n" \
                   "const_mu_o = 0.7 \n" \
                   "const_rsb_default = 100 \n" \
                   "const_Bob_default = 1.2 \n" \
                   "const_tres_default = 90 \n" \
                   "const_Roughness_default = 0.0001 \n" \
                   "StartEndTemp = 0 \n" \
                   "Standing_based = 0 \n" \
                   "const_rho_air = 1.2217 \n" \
                   " \n"    




API_func_str = ""

def create_func_in_API(parameters_str, atributs_in_signature_str, func_name_str, func_from_book, func_description, description_string_lines):
    start_string_in_func = tab_str + "def " + func_name_str + "(self, " + atributs_in_signature_str + "):\n"
    func_description = func_description.replace("\")","")
    func_description = func_description.replace("\"","   ")
    func_description = func_description.replace(", _", "")
    func_description = func_description.replace("\'", "")
    func_description = func_description.replace("        ArgumentDescriptions:=Array(", "")
    func_description = " ==========  arguments  ============== \n" + func_description + "        \"\"\"\n"
    func_description = func_description.replace("\n", "\n\n")
    func_description = func_description.replace("\n\n\n\n", "")

    description_string_lines = description_string_lines.replace(description_string, " ========== description ============== \n")
    description_string_lines = description_string_lines.replace(", _", "")
    description_string_lines = description_string_lines.replace("\"", "")
    description_string_lines = "        \"\"\"\n" + description_string_lines + "        \n"
    description_string_lines = description_string_lines.replace(" \"\n", "\n")
    description_string_lines = description_string_lines.replace("\'", "")

    middle_string_in_func = func_from_book
    end_string_in_func = 2 * tab_str + "return " + "self.f_" + func_name_str + "(" + parameters_str + ")\n"
    return start_string_in_func + description_string_lines + func_description + middle_string_in_func + end_string_in_func

def append_func_in_API_func_str(filled_str, VBA_func_name):
    str_to_append = 2 * tab_str +"self.f_" + VBA_func_name + " = self.book.macro(\"" + VBA_func_name + "\")\n"
    new_str = filled_str + str_to_append
    return new_str

class VBA_Func_Header:
    """
    class representing vba function header
    """

    def __init__(self, func_name, file_name_for_python_api = file_name_for_python_api):
        self.func_name = func_name.lstrip()
        self.str_desc = ''
        self.num_line = 0
        self.lines = []
        self.API_func_str = ""
        self.file_name_for_python_api = file_name_for_python_api

    def edit_string(self, string):
        """
        Editing of original state of string, deleting of some not needed symbols

        :param string: original string
        :return: edited string with clear syntax
        """
        string = string.replace("\"","")
        string = string.replace("\n", " ")
        string = string.replace(" _", " ")
        string = string.replace("     ", " ")
        string = string.replace("   ", " ")
        string = string.replace("  ", " ")
        string = string.replace("  ", " ")
        string = string.replace("  ", " ")
        string = string.replace("https://", "www.")
        string = string.replace("http://", "www.")
        return string

    def replace_long_edited_string(self, string):
        if len(string) > 182:
            string = string[:182]
            string += "..см.мануал"
        return string


    def save_lines_to_file(self, path):
        """
        create .txt files with one functions descriptions and all_stuff.txt with all functions descriptions
        :param path:
        :return: None
        """
        fname_api = path + '/' + self.file_name_for_python_api
        fname = path + '/' + self.func_name + ".txt"
        fname2 = path + '/' + file_name_for_all_stuff + ".txt"
        print(fname)
        result_lines = self.lines

        """
        start addition in report file
        """
        report = "Отчет по функции " + self.func_name + " \n "
        """
        addition of start string - 1 line
        """
        result_lines.insert(0, start_string)

        """
        addition of 2th string - 2 line - with function name
        """
        result_lines.insert(1, macro_string + "\"" + self.func_name + "\"" + connect_to_next_string_in_array)

        """
        addition of function name in python API 
        """
        self.API_func_str = append_func_in_API_func_str(self.API_func_str, self.func_name)
        """
        preparing and editing of short function description above declaration of function
        """
        string_contain_function = False
        string_number = 2
        description_string_lines = description_string + "\""
        while string_contain_function == False:
            math_object = re.search(r'Function', result_lines[string_number])
            if math_object != None:
                string_contain_function = True
            if not string_contain_function:
                current_addition = result_lines[string_number]
                current_addition = self.edit_string(current_addition)

                description_string_lines += current_addition

                string_number += 1
            else:
                description_string_lines += "\"" + connect_to_next_string_in_array

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
        string_with_parameters_for_api = ""
        """
        list of pattern, that will be deleted in sting
        """
        not_nedeed_in_api = [self.func_name, "ByVal",  "Optional", "Double", "Integer", "Boolean", "Long" , "Variant",
                                "String", "Public", " As ", "Function", " _ ", " ",  "\n", "\' ", "(_", 'TEMP_CALC_METHOD']

        not_nedeed_in_string = [self.func_name, "ByVal","-1",  "Optional", "Double", "Integer", "Boolean", "Long" , "Variant",
                                "String", "Public", " As ", "Function", " _ ", " ", "=",  "\n", "\' ", "(_",
                                "PVT_DEFAULT", "H_CORRELATION", "TEMP_CALC_METHOD", 'TEMP_CALC_METHOD']
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
                string_with_parameters_for_api += current_addition
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

                for i in not_nedeed_in_api:
                    string_with_parameters_for_api = string_with_parameters_for_api.replace(i, "")
                string_with_parameters_for_api = string_with_parameters_for_api.replace(",_", ",")
                string_with_parameters_for_api = string_with_parameters_for_api.replace("_)", "")
                string_with_parameters_for_api = string_with_parameters_for_api.replace(")", "")
                string_with_parameters_for_api = string_with_parameters_for_api.replace("(", "")
                string_with_parameters_for_api = string_with_parameters_for_api.replace("hydr_corrH_CORRELATION=0",
                                                                                        "hydr_corr=H_CORRELATION")
                #string_with_parameters_for_api = string_with_parameters_for_api.lower()
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
        number_of_parametrs = len(list_of_names_parametr)
        report += "Количество параметров в функции = " + str(number_of_parametrs) + " \n "
        parametrs_in_report = sting_with_parametrs_and_delimetr.replace(",", ", ")
        report += "Строка параметров:" + parametrs_in_report + " \n "

        """
        preparing and editing description of parametrs for 5th lines
        """
        argument_descriptions_string_with_stuff = argument_descriptions_string
        number_of_writed_parametrs_in_description = 0
        string_of_not_writed_parametrs = ""
        k_iter_for_search_plus = 0
        for i in list_of_names_parametr:
            parametr_writed = False
            start_string_number = string_number
            current_string_number = start_string_number
            last_number =  (len(result_lines) - 1)
            while not parametr_writed and current_string_number <= last_number + 1:

                lower_name = i.lower()

                if current_string_number == last_number + 1:
                    current_addition = "\"" + lower_name +"\"" + connect_to_next_string_in_array
                    argument_descriptions_string_with_stuff += current_addition
                    parametr_writed = True
                    string_of_not_writed_parametrs += lower_name + '  '
                else:
                    current_string = result_lines[current_string_number]

                    """this symbol T_C is not understandable, change it"""
                    if current_string.find("Т_C") != -1:
                        current_string = current_string.replace("Т_C", "t_c")
                    # this super puper method especially for bubble pressure
                    if current_string.find("tres_C,") != -1:
                        current_string = current_string.replace("tres_C,", "пласта,")
                    lower_current_string = current_string.lower()
                    position_equal = lower_current_string.find(lower_name)
                    if position_equal != (-1):
                        """
                        in this place parametr are found and description will be search in next lines before new parametr
                        """
                        current_addition = " \"" + self.edit_string(lower_current_string)

                        if current_string_number != last_number:
                            current_string_number_plus = current_string_number + 1
                            current_string_plus = result_lines[current_string_number_plus]

                            """this symbol T_C is not understandable, change it"""
                            if current_string_plus.find("Т_C") != -1:
                                current_string_plus = current_string_plus.replace("Т_C", "t_c")
                            #this super puper method especially for bubble pressure
                            if current_string_plus.find("tres_C,") != -1:
                                current_string_plus = current_string_plus.replace("tres_C,", "пласта.")
                            current_string_plus_lower = current_string_plus.lower()
                            string_not_contain_new_parametr = True
                            is_not_empty_string = True
                            is_not_included_result = True  # TODO check, can result be used in description?
                            """
                            searching additional lines
                            """
                            while string_not_contain_new_parametr and current_string_number_plus <= last_number:

                                current_string_plus = result_lines[current_string_number_plus]

                                #this symbol T_C is not understandable, change it
                                if current_string_plus.find("Т_C") != -1:
                                    current_string_plus = current_string_plus.replace("Т_C", "t_c")

                                #this super puper methon especially for bubble pressure
                                if current_string_plus.find("tres_c,") != -1:
                                    current_string_plus = current_string_plus.replace("tres_c,", "пласта,")
                                current_string_plus_lower = current_string_plus.lower()

                                """
                                cheking line on new parametr name
                                """
                                for k in range(k_iter_for_search_plus + 1, number_of_parametrs):
                                    name_of_next_parametr = list_of_names_parametr[k]
                                    name_of_next_parametr_lower = name_of_next_parametr.lower()
                                    if current_string_plus_lower.find(name_of_next_parametr_lower) != -1:
                                        string_not_contain_new_parametr = False

                                if current_string_plus_lower.find("\'\n") != -1:
                                    is_not_empty_string = False

                                if current_string_plus_lower.find("езультат") != -1:
                                    is_not_included_result = False
                                if string_not_contain_new_parametr and is_not_empty_string and is_not_included_result:
                                    current_string_plus_lower = self.edit_string(current_string_plus_lower)
                                    current_addition += current_string_plus_lower
                                current_string_number_plus += 1
                        current_addition = self.replace_long_edited_string(current_addition)
                        current_addition += "\""
                        current_addition += connect_to_next_string_in_array
                        argument_descriptions_string_with_stuff += current_addition
                        parametr_writed = True
                        number_of_writed_parametrs_in_description += 1
                current_string_number += 1
            k_iter_for_search_plus += 1

        """
        creating report about parametrs description
        """
        report += "Параметров найдено и записано = " + str(number_of_writed_parametrs_in_description) + " \n "
        if number_of_writed_parametrs_in_description != number_of_parametrs:
            number_of_not_writed_parametrs = number_of_parametrs - number_of_writed_parametrs_in_description
            report += "Ошибка! " + "Не найдены параметры! Количество: " + str(number_of_not_writed_parametrs) + " \n "
            report += "Список параметров: " + string_of_not_writed_parametrs + " \n "
        """
        replace end in last addition - from & to )
        """
        last_addition_with_end = current_addition
        last_addition_with_end = last_addition_with_end.replace(connect_to_next_string_in_array, ") \n")

        """
        create finished 5th line 
        """
        argument_descriptions_string_with_stuff = argument_descriptions_string_with_stuff.replace(current_addition, last_addition_with_end +"\n \n")

        """
        insert finished 5th line 
        """
        result_lines.insert(4, argument_descriptions_string_with_stuff)


        """
        deleting of last lines
        """
        for i in range(5, last_number + 2):
            result_lines.pop(5)

        """
        deleting last symbols, that are not needed 
        """
        k = 0
        for i in result_lines:

            result_lines[k] = i.replace("\'", "")
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
        create python api file 
        """
        finished_API_func_str = create_func_in_API(sting_with_parametrs_and_delimetr, string_with_parameters_for_api,
                                                   self.func_name, self.API_func_str,
                                                   argument_descriptions_string_with_stuff, description_string_lines)
        py_result = finished_API_func_str +"\n"
        file_name_for_python_api = path_python_api_out + '/' + self.file_name_for_python_api
        f4_api = open(file_name_for_python_api, "a", encoding='UTF-8')
        f4_api.writelines([py_result])
        f4_api.close()
        """
        create file with one function in needed format
        """
        
        # f = open(fname, "w", encoding='UTF-8')
        # f.writelines(result_lines)
        # f.close()


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
create file for python API and clear it
"""
file_name_for_python_api_woth_path = path_python_api_out + '/' + file_name_for_python_api
python_api = open(file_name_for_python_api_woth_path, "w", encoding='UTF-8')
python_api.writelines([""])
python_api.close()
"""
description generation start
extract function with description markers
and edited it by format
"""
for code_file in file_name:
    process_code_file(path_vba_txt + code_file)

"""
create file .txt for generated description module and fill it
"""
f3_module_txt = path_listings_out + '/' + file_name_for_description_module + ".txt"
f3_module_txt = open(f3_module_txt, "w", encoding='cp1251')
f3_module_txt.writelines([""])

f2 = open(fname2, "r", encoding='UTF-8')
generated_lines = f2.read()
f3_module_txt.writelines([start_string_for_module])
f3_module_txt.writelines(generated_lines)
f3_module_txt.writelines([end_string_for_module])

f3_module_txt.close()
f2.close()
print("description module generated in " + f3_module_txt.name)

"""
create python api file with required format
"""

file_name_for_python_api_woth_path = path_python_api_out + '/' + file_name_for_python_api
python_api = open(file_name_for_python_api_woth_path, "r", encoding='UTF-8')
generated_api_lines = python_api.read()
python_api.close()

python_api = open(file_name_for_python_api_woth_path, "w", encoding='UTF-8')
python_api.writelines([api_const_string + start_classes_str])
python_api.writelines(generated_api_lines)
python_api.writelines([create_class_str])
python_api.close()