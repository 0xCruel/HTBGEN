import base64
import subprocess
from colorama import Fore, Back, Style


def banner():

    g = Fore.GREEN
    w = Fore.WHITE

    print(f"""
   
   
                                        {g}     __  ________ ____  _____________   __
                                        {w}    / / / /_  __/ __ )/ ____/ ____/ | / /
                                        {g}   / /_/ / / / / __  / / __/ __/ /  |/ / 
                                        {w}  / __  / / / / /_/ / /_/ / /___/ /|  /  
                                        {g} /_/ /_/ /_/ /_____/\____/_____/_/ |_/   
                                                     
                                        {w}             | MADE BY CRUEL|
   
   
   
   
   """)

banner()


subprocess.call("curl -XPOST https://www.hackthebox.eu/api/invite/generate", shell=True) 
print('\n')
api = str(input(Fore.RED + "copy the line and past it here:\n==> ")) 
print('\n')
dec = str(base64.standard_b64decode(api))
print("[#]==> " + dec.replace('b', '')) 
print('\n')
print("Enjoy!") 
print('\n')
