from tools import cloudflare
from tools import finder
from tools import dnsloocup
from tools import ip_location
from tools import reverseIP
from tools import httpheader
from tools import port_scan
from tools import word_press
from colorama import Fore
import time
import sys

def information_gatering():
    print("\n")
    time.sleep(0.2)
    print(Fore.WHITE+"[*] Wellcome to Information Gatering")
    print("\n")
    time.sleep(0.1)
    print(Fore.WHITE+"[*] Select one option")
    print("\n")
    time.sleep(0.1)
    print(Fore.LIGHTRED_EX+"[1]"," : PAGE-FINDER\n")
    time.sleep(0.1)
    print(Fore.YELLOW+"[2]"," : CLOUDFLARE-BYPASSER\n")
    time.sleep(0.1)
    print(Fore.LIGHTBLUE_EX+"[3]"," : DNS-LOOKUP\n")
    time.sleep(0.1)
    print(Fore.CYAN+"[4]"," : IP-LOCATION\n")
    time.sleep(0.1)
    print(Fore.RED+"[5]"," : HTTP-HEADER\n")
    time.sleep(0.1)
    print(Fore.LIGHTBLUE_EX+"[6]"," : PORT-SCAN\n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+"[7]"," : REVERSE-IP\n")
    time.sleep(0.1)
    print(Fore.GREEN+"[8]"," : WORD-PRESS\n")
    time.sleep(0.1)
    print(Fore.LIGHTRED_EX+"[x]"," : Back To Menu\n")
    option = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    print("\n\n")
    if option == '1':
        finder.finder()
    elif option == '2':
        cloudflare.CloudFlare()
    elif option == '3':
        dnsloocup.dnslookup()
    elif option == '4':
        ip_location.ip_location()
    elif option == '5':
        httpheader.http_header()
    elif option == '6':
        port_scan.port_scan()
    elif option == '7':
        reverseIP.reverseIP()
    elif option == '8':
        word_press.wpplug()
    elif option == 'x':
        import webTik
    else:
        print(Fore.LIGHTRED_EX+"[-] Command Not Found")
        information_gatering()