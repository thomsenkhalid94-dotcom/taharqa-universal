import os
import sys, time
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse 
import zipfile, hashlib
LOGO = r"""
  _______ _ _ _ ____ ___ _
 |__ __| / \ | | | | | _ \ / _ \ / \
    | | / _ \ | |__| | | |_) || | | | / _ \
    |  / ___ \| __ | | _ < | |_| | / ___ \
    |_| /_/ \_\_| |_| |_| \_\ \__\_\ /_/ \_\
        LAB by khwajja.Sec® | Gezira,state medani,SDN
"""

def menu():
    os.system('clear' if os.name!='nt' else 'cls')
    print(LOGO)
    print(" [1] Run Server (8080)")
    print(" [2] Run Scanner")
    print(" [3] Run SOC Analyzer")
    print(" [4] View Logs")
    print(" [5] Run Zipfile crak")
    print(" [0] Exit")

while True:
    menu()
    c = input("\n taharqa®> ")
    if c=="1": os.system("python3 app/app.py" if os.name!='nt' else "python app/app.py")
    elif c=="2": os.system("python3 app/scanner.py" if os.name!='nt' else "python app/scanner.py")
    elif c=="3": os.system("python3 app/analyze.py" if os.name!='nt' else "python app/analyze.py")
    elif c=="4": os.system("cat app/waf.log" if os.name!='nt' else "type app\\waf.log")
    elif c=="5": os.system("python3 app/zf-crack.py" if os.name!='nt' else "python app/zf-crack.py")
    elif c=="0": break
print("   -bye well see ya    حمد ع السلامه")
print("                                                                                     ")
print("==============================================================*auth.khwajja.Sec®*====")
