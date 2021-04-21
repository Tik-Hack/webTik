from colorama import Fore
import requests


def http_header():
    
        print(Fore.LIGHTRED_EX+"[!] Enter Domain")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Http-Header"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "+Fore.RED+"https://")
        result = requests.get("http://api.hackertarget.com/httpheaders?q=" + url).text
        print(Fore.LIGHTBLUE_EX+result)
        
        input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
        import webTik

