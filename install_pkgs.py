import subprocess
import sys


# try: 
#     import pandas as pd
# except ImportError: 
#     subprocess.check_call([sys.executable,"-m", "pip", "install", "pandas"])
#     import pandas as pd



# try: 
#     import openpxyl
# except ImportError: 
#     subprocess.check_call([sys.executable,"-m", "pip", "install", "openpyxl"])
#     import openpyxl


# try: 
#     import pdfplumber
# except ImportError: 
#     subprocess.check_call([sys.executable,"-m", "pip", "install", "pdfplumber"])
#     import pdfplumber

try: 
    import black
except ImportError: 
    subprocess.check_call([sys.executable,"-m", "pip", "install", "black"])
    import black
