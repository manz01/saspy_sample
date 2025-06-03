"""
Author:       Manzar Ahmed
Create Date:  2025-05-18
Project:      sas samples
Description:  generate a sample report
----------------------------------------------------------------------------
Version Control
----------------------------------------------------------------------------
#    Date      Name          Description
1.0  20250518  Manzar Ahmed  Initial
----------------------------------------------------------------------------
"""
import os
from utils.sas_setup import start_sas_session, print_sas_log, sas_output

output_path = '~/reports'
output_path = os.path.expanduser(output_path)

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
