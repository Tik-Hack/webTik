from colorama import Fore
import requests


def port_scan():
        print(Fore.LIGHTRED_EX+"[!] Enter Domain")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Port-Scan"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.RED+"https://")
        result = requests.get("http://api.hackertarget.com/nmap?q=" + url).text
        print(Fore.LIGHTBLUE_EX+result)
        
        input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
        import webTik
    
