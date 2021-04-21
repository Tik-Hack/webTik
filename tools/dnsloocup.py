import sys
import requests
from colorama import Fore


def dnslookup():
    print(Fore.RED+"[!] Plase Enter Domain")
    url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Dns-Lookup"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.RED+"https://")
    result = requests.get("http://api.hackertarget.com/dnslookup?q=" + url).text
    print(Fore.LIGHTBLUE_EX+result)
    
    input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
    import webTik
