#!/usr/bin/python
import requests, sys, re, os, time, random
from colorama import Fore, Back, Style


r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                $$$$$$$$\                                      $$\   $$\ 
                \____$$  |    DEEP WEB MOROCCO +18             $$ |  $$ |
                    $$  / $$$$$$\  $$$$$$$\   $$$$$$\          $$ |  $$ |
                   $$  / $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$\ $$$$$$$$ |
                  $$  /  $$ /  $$ |$$ |  $$ |$$$$$$$$ |\______|$$  __$$ |
                 $$  /   $$ |  $$ |$$ |  $$ |$$   ____|        $$ |  $$ |
                $$$$$$$$\|$$$$$$  |$$ |  $$ |\$$$$$$$\         $$ |  $$ |
                \________|\______/ \__|  \__| \_______|        \__|  \__|                                                                                                                                                                                                                                            
                        S. MARGUS - Zone-H Url Hunter                                       
                               1337   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()

try:
    __Defacer = sys.argv[1]
    __ZH = sys.argv[2]
    __PHPSESSID = sys.argv[3]
    __ZHE = sys.argv[4]
except IndexError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'zone.py ' + Fore.WHITE + 'Name_of_defacer ' + y + 'ZH PHPSESSID ZHE'
    print(Style.RESET_ALL)
    sys.exit()

page = 1
print r + '    [' + w + '+' + r + '] ' + w + 'Notifier is : ' + r + __Defacer
while True:
    url = 'http://www.zone-h.org/archive/special=' + __Defacer + '/page=' + str(page)
    page = page + 1
    sess = requests.session()

    my_cookie = {
        'ZHE': __ZHE,
        'ZH': __ZH,
        'PHPSESSID': __PHPSESSID
    }

    Open = sess.get(url, cookies=my_cookie, timeout=10)
    print Open.text
    Hunt_urls = re.findall('<td>(.*)\n							</td>', Open.content)
    for xx in Hunt_urls:
        print r + '    [' + w + '*' + r + '] ' + y + xx.split('/')[0]
        with open('hunted_urls.txt', 'a') as rr:
            rr.write(xx.split('/')[0] + '\n')

    if page > 50:
        sys.exit()
    else:
        continue
