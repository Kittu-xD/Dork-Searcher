import re
import requests
import sys
import time
import random

colors = [36, 32, 34, 35, 31, 37]
clear = '\x1b[0m'

logo = '''
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-

██╗ ██╗  ██████╗░ ░█████╗░ ██████╗░ ██╗░░██╗ ██╗  ██╗ ██╗
╚═╝ ╚═╝  ██╔══██╗ ██╔══██╗ ██╔══██╗ ██║░██╔╝ ██║  ╚═╝ ╚═╝
░░░ ░░░  ██║░░██║ ██║░░██║ ██████╔╝ █████═╝░ ██║  ░░░ ░░░
░░░ ░░░  ██║░░██║ ██║░░██║ ██╔══██╗ ██╔═██╗░ ██║  ░░░ ░░░
██╗ ██╗  ██████╔╝ ╚█████╔╝ ██║░░██║ ██║░╚██╗ ██║  ██╗ ██╗
╚═╝ ╚═╝  ╚═════╝░ ░╚════╝░ ╚═╝░░╚═╝ ╚═╝░░╚═╝ ╚═╝  ╚═╝ ╚═╝

-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
'''

for N, line in enumerate(logo.split('\n')):
    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
    time.sleep(0.06)

def getURL(dorki):

    baseURL = "https://search.earthlink.net/search-api/?q=inurl:"+dorki+"&num=50&start=0&lr=lang_en&oe=utf-8"
    rsp = requests.get(baseURL)
    test = re.findall('"U":"(.+?)"', rsp.text)
    print("Found", len(test), "results!!")
    input("Press enter to start printing...")
    for a in range(len(test)):
        print("[+]", test[a])
    # strt = int(strt)
    # print("New starting :", strt)

try:
    query = input("[*] Enter query to search : ")
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    getURL(query)
    getMore = input("[+] Process finished!!\n[+] Enter 1 for next page Results || Enter 2 to finish searching: ")
    start = 50
    while getMore == '1':
        baseURL = "https://search.earthlink.net/search-api/?q=inurl:"+query+"&num=50&start="+str(start)+"&lr=lang_en&oe=utf-8"
        rsp = requests.get(baseURL)
        test = re.findall('"U":"(.+?)"', rsp.text)
        print("Found", len(test), "results!!")
        input("Press enter to start printing...")
        for a in range(len(test)):
            print("[+]", test[a])
        start += 50
        print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
        getMore = input("[+] Enter 1 for next page Results || Enter 2 to finish searching: ")
    input("[*] Process finished!!! Press any key to exit...")

except Exception as exc:
    print("Pst!!! Error due to reason :", exc)

