# SASPy working in WSL

**Author:  Manzar Ahmed**</br>
**Date: June 2025**

## ✨ Introduction

Hey Everyone!

I've worked as a SAS engineer for several years, but more recently, many of the projects I'm involved in have been migrating away from SAS to modern tools like **Python**, **dbt**, **Snowflake**, and **Databricks**.

In a recent project, we migrated SAS code to **DuckDB**, and later into **Snowflake**. During this process, I discovered the **SASPy** Python library, which lets you run SAS code directly from Python and integrates nicely with **Visual Studio Code (VS Code)**.

I enjoy building code samples in my personal sandbox, which runs on **Ubuntu via Windows Subsystem for Linux (WSL)**. In this setup, I managed to configure SASPy to work with the **free cloud-based SAS OnDemand for Academics (ODA)**.

**SAS OnDemand for Academics (ODA)** is a free, cloud-based version of SAS offered by the SAS Institute for learning and teaching. It provides full-featured SAS capabilities in the cloud without requiring a local installation or paid license—making it ideal for students, educators, and professionals exploring SAS in open-source environments.

This guide documents the exact steps I followed to set up SASPy inside WSL and connect it to SAS OnDemand. Once integrated, you can leverage Python, Jupyter, and your local Linux tools to interact with remote SAS sessions—offering the best of both worlds: open-source flexibility and enterprise-grade analytics.

For official documentation and additional guidance, refer to the SAS support page:  
🔗 [SASPy with SAS OnDemand for Academics – Official Guide](https://support.sas.com/ondemand/saspy.html)


## ✅ Prerequisites
Ensure the following are installed inside WSL:
* Python 3.3+
* Java 1.8.0_162+
* SASPy 3.3.4+
* A SAS OnDemand for Academics account

## 🛠️ Step-by-Step Setup in WSL
1. **Install Dependencies**

In WSL terminal:
```bash
sudo apt update
sudo apt install -y python3 python3-pip openjdk-11-jdk
pip3 install saspy
```

Terminal output:
```terminal
(venv) u001@DELL-XPS13:~$ pip3 install saspy
Collecting saspy
  Downloading saspy-5.103.0-py3-none-any.whl (10.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.0/10.0 MB 19.5 MB/s eta 0:00:00
Installing collected packages: saspy
Successfully installed saspy-5.103.0
```

Ensure Java is installed correctly:

```bash
java -version
```
Terminal output:
```terminal
(venv) u001@DELL-XPS13:~$ java -version
openjdk version "17.0.15" 2025-04-15
OpenJDK Runtime Environment (build 17.0.15+6-Ubuntu-0ubuntu122.04)
OpenJDK 64-Bit Server VM (build 17.0.15+6-Ubuntu-0ubuntu122.04, mixed mode, sharing)
```

2. **Create** sascfg_personal.py

Find the SASPy config directory:

```py
python3 -c "import saspy; print(saspy.__file__.replace('__init__.py', 'sascfg_personal.py'))"
```

Create the file at that path (adjust if needed):

```bash
nano /home/u001/.local/lib/python3.*/site-packages/saspy/sascfg_personal.py
```

Paste this content (edit java path and uncomment your region):
```python
SAS_config_names = ['oda']

oda = {
    'java' : '/usr/bin/java',  # Confirm with `which java`
    #European Home Region 1
    'iomhost' : ['odaws01-euw1.oda.sas.com','odaws02-euw1.oda.sas.com'],
    'iomport' : 8591,
    'authkey' : 'oda',
    'encoding' : 'utf-8'
}
```

3. **Create** .authinfo File

This file stores your ODA credentials securely.
```bash
nano ~/.authinfo
```

Paste this (replace with your ODA email/username and password):
```bash
oda user ODA_USERNAME password ODA_PASSWORD
```

Then set permissions:
```bash
chmod 600 ~/.authinfo
```


## **Add Environment Variable to** `.bashrc`
Open your shell config file (depending on the shell you use):
```bash
nano ~/.bashrc
```
Add the following line at the end (edit path accordingly):
```bash
export SASPY_CFG=/home/u001/.local/lib/python3.10/site-packages/saspy/sascfg_personal.py
```
Then **reload** the profile:
```bash
source ~/.bashrc
```


**Common Problems**

```terminal
Using SAS Config named: oda
Pandas module not available. Setting results to HTML
Did not find key oda in authinfo file:/home/u001/.authinfo

Please enter the OMR user id: 
```


after entering user id (email) and password:

```bash
SAS Connection established. Subprocess id is 12109

SAS Connection terminated. Subprocess id was 12109
```

🧪 Optional: Jupyter Notebook in WSL

```bash
pip3 install notebook
jupyter notebook --no-browser --ip=0.0.0.0


```

Access from browser via http://localhost:8888 on Windows side.


## **Running SAS** in jupter Notebook
You can now run SAS code directly in Jupyter notebooks using SASPy’s magic commands. Below are two key code blocks that complete the integration.

### 🧱 **Block 1** : Initialize SASPy and Load Magic Extension
```python
import os
import saspy

# Get the path to your personal SASPy configuration
cfg_path = os.environ.get("SASPY_CFG")

# Establish a connection to SAS using the ODA profile
sas = saspy.SASsession(cfgfile=cfg_path)

# Load SAS magic commands into the notebook environment
from saspy.sas_magic import SASMagic
SASMagic.saslib = sas
%load_ext saspy.sas_magic
```

#### 💡 Explanation:
* Retrieves the SASPY_CFG environment variable set in .bashrc.
* Starts a SAS session using the oda configuration.
* Loads the %SAS magic command so you can run native SAS code directly in notebook cells.

### 🧾 **Block 2**: Run Native SAS Code Using %SAS Magic
#### 💡 Explanation:
* The %%SAS cell magic tells Jupyter to treat the entire cell as SAS code.
* This example runs a simple PROC PRINT on the sashelp.cars dataset, showing the first 6 rows.

#### 📸 Output Preview
* Here’s an example screenshot of SAS output rendered directly in the notebook
![Notebook SASPy Test](markdown_images/notebook-saspy-test.jpg)

