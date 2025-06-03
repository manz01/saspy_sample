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
        raise EnvironmentError("SASPY_CFG environment variable is not set.")

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
    print("-" * 62, "SAS LOG", "-" * 63)
    print(submit_result.get('LOG', '[No LOG found in result]'))
    print("-" * 133)



def sas_output(output_dir, filename, html_content):
    """
    Write the given HTML content to a file in the specified directory and print the file path.

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