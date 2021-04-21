from tools import cms
import information_gatering
from colorama import Fore
import time
import sys
from tools import Developoer
from tools import banner
def start():
    print("\n")
    time.sleep(0.2)
    print(Fore.WHITE+"[\//\/] Wellcome to webTik")
    print("\n")
    time.sleep(0.1)
    print(Fore.WHITE+"[*] Select one option")
    print("\n")
    time.sleep(0.1)
    print(Fore.RED+"[1]"," : Information-Gatering\n")
    time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX+"[2]"," : CMS-Detection\n")
    time.sleep(0.1)
    print(Fore.LIGHTBLUE_EX+"[3]"," : Developer :)\n")
    time.sleep(0.1)
    print(Fore.LIGHTCYAN_EX+"[4]"," : Exit \n")
    option = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    print("\n")
    if option == '1':
       information_gatering.information_gatering()
    elif option == '2':
        cms.cms()
    elif option == '3':
        Developoer.Developer()
        print(Fore.WHITE+"\n")
    elif option == '4':
        print(Fore.LIGHTBLUE_EX+"[\//\/]Good By\n")
        sys.exit()
    else:
        print(Fore.LIGHTRED_EX+"[-] Command Not Found")
        start()

start()