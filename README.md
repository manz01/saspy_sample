# SASPy working in WSL

**Author:  Manzar Ahmed**
**Date: June 2025**

## ✨ Introduction

If you’re working in a Linux-native Python environment and need access to SAS — especially using the **free cloud-based SAS OnDemand for Academics (ODA)** — integrating it with **Windows Subsystem for Linux (WSL)** using **SASPy** is an incredibly powerful setup.

**SAS OnDemand for Academics** is a *free version of SAS* provided by SAS Institute for learning and teaching purposes. It allows you to run full-featured SAS in the cloud without requiring a paid license or local installation of the SAS system — making it ideal for students, educators, and even professionals experimenting with SAS in open-source environments.

This guide documents the **exact steps I followed** to get SASPy working inside WSL and connected to SAS OnDemand. Once integrated, you can use Python, Jupyter, and all your local Linux tools to interact with remote SAS sessions — giving you the best of both worlds: **open-source flexibility and enterprise-grade analytics**.

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


4. **Running SAS** in jupter Notebook

![Notebook SASPy Test](markdown_images/notebook-saspy-test.jpg)