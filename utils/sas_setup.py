"""
sas_setup.py

Utility functions for initializing SASPy sessions and handling SAS outputs.

Author: Manzar Ahmed
Created: 05-Jun-2025
License: MIT (See LICENSE file for full text)
"""
__version__ = '0.0.1'
__updated__ = '2025-06-05'
__author__ = 'Manzar Ahmed'
__maintainer__ = ['Manzar Ahmed']
__email__ = 'manzar@example.com'
__license__ = 'MIT'
__docformat__ = 'google'
__license_text__ = """
MIT License

Copyright (c) 2025 Manzar Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
"""
# -*- coding: utf-8 -*-
import os
import saspy


def start_sas_session():
    """
    Starts a SASPy session using the SASPY_CFG environment variable and
    submits an optional autoexec file if found.

    Returns:
        saspy.SASsession object
    """
    cfg_path = os.environ.get("SASPY_CFG")
    if not cfg_path:
        raise EnvironmentError(
            "SASPY_CFG environment variable is not set."
        )

    sas = saspy.SASsession(cfgfile=cfg_path)

    autoexec_path = os.path.expanduser('/home/u001/autos.sas')
    if os.path.exists(autoexec_path):
        with open(autoexec_path, 'r') as f:
            sas.submit(f.read())

    return sas


def print_sas_log(submit_result):
    """
    Prints the SAS log from a saspy.submit() result dictionary.

    Args:
        submit_result (dict): The dictionary returned by sas.submit(...)
    """
    print("-" * 25, "SAS LOG", "-" * 25)
    print(submit_result.get('LOG', '[No LOG found in result]'))
    print("-" * 61)


def sas_output(output_dir, filename, html_content):
    """
    Write the given HTML content to a file in the specified directory
    and print the file path.

    Args:
        output_dir (str): Path to the output directory.
        filename (str): Desired filename (e.g., "report.html").
        html_content (str): HTML content to be written.

    Returns:
        str: Full path of the written file.
    """
    os.makedirs(output_dir, exist_ok=True)
    html_output_path = os.path.join(output_dir, filename)

    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ HTML report saved to: {html_output_path}")
    return html_output_path
