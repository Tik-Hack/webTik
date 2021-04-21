import os
from colorama import Fore
import requests
import sys
import json
import time


def reverseIP():
    print(Fore.LIGHTRED_EX+"[!] Enter Domain")
    url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Reverse-Ip"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.RED+"https://")
    site = {"remoteAddress":url}
    link = requests.post("https://domains.yougetsignal.com/domains.php" , site)

    source = json.loads(link.content)

    for data in source['domainArray']:
        time.sleep(0.1)
        print(" "+data[0]+"\n")

    input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
    import webTik

