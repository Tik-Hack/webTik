import socket
import sys
import time
from colorama import Fore

def CloudFlare():
    print("""
 [!] Please Enter The Target Website Address\n""")
    
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webTik"+Fore.BLUE+" ~ "+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐")
    if site == "":
        try:
            print(Fore.RED+"[!]"+Fore.GREEN+"Please Enter Address : \n")
            time.sleep(5)
            sys.exit()
        except:
            return
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            time.sleep(0.1)
            print(Fore.GREEN+"[+]"+Fore.WHITE+" CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            pass
    
    input(Fore.GREEN+"[*] Back To Menu (Press Enter...) ")
    import webTik


