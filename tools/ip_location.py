import os
import sys
from colorama import Fore
import ipapi
import requests
import socket
import time



def ip_location():
    print(Fore.LIGHTRED_EX+"[!] Enter WebSite Domain  ! ! ! \n")
    url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐"+Fore.LIGHTRED_EX+" https://")
    ip = socket.gethostbyname(str(url))
    source = ipapi.location(ip=ip)
    try:
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+"[$] Ip "+Fore.LIGHTRED_EX+"Info")
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Ip: "+Fore.LIGHTRED_EX+source['ip'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Country: "+Fore.LIGHTRED_EX+source['country_name'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] City: "+Fore.LIGHTRED_EX+source['city'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Region: "+Fore.LIGHTRED_EX+source['region'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Id Country: "+Fore.LIGHTRED_EX+source['country'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Calling Code: "+Fore.LIGHTRED_EX+source['country_calling_code'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Languages: "+Fore.LIGHTRED_EX+source['languages'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] Org: "+Fore.LIGHTRED_EX+source['org'])
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX+"[+] zip: "+Fore.LIGHTRED_EX+source['zip'])
        
    except:
        input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
        import webTik
        
       

