"""
-------------------------------------------------------------------------------------------------
Program:        generate_report.py
Project:        saspy_sample
Description:    generate a sample report
Input(s):       sashelp.class
Output(s):      html report in ~/reports/class_report.html
Author:         Manzar Ahmed
First Created:  05-Jun-2025
-------------------------------------------------------------------------------------------------
Program history:
-------------------------------------------------------------------------------------------------
Date        Programmer                Description
----------  ------------------------  -----------------------------------------------------------
2025-06-05  Manzar Ahmed              v0.01/Initial version
-------------------------------------------------------------------------------------------------
"""
import os
from utils.sas_setup import start_sas_session, print_sas_log, sas_output

output_path = os.path.expanduser('~/reports')

sas = start_sas_session()

sas_code = """
proc report data=sashelp.class nowd;
    column name sex age height weight;
    define name / display;
    define sex / display;
    define age / analysis;
    define height / analysis;
    define weight / analysis;
run;
"""

result = sas.submit(sas_code, results='html')

print_sas_log(result)

sas_output(output_path, "class_report.html", result['LST'])
