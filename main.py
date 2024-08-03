import random
import string
from colorama import *
import requests
import fade
import threading
init()
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLUE
C = Fore.CYAN
M = Fore.MAGENTA
Y = Fore.YELLOW
W = Fore.WHITE
B = Fore.BLACK
LR = Fore.LIGHTRED_EX
LG = Fore.LIGHTGREEN_EX
LBL = Fore.LIGHTBLUE_EX
LC = Fore.LIGHTCYAN_EX
LM = Fore.LIGHTMAGENTA_EX
LY = Fore.LIGHTYELLOW_EX
LW = Fore.LIGHTWHITE_EX
LB = Fore.LIGHTBLACK_EX

bad_counter = 0

stop_codes = [401]
i_codes = [202, 404, 204, 302, 304, 307, 403]
v_codes = [200]

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chars_list = list(chars)

banner = ("""██╗   ██╗      ██████╗ ██╗   ██╗ ██████╗██╗  ██╗███████╗
██║   ██║      ██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝
██║   ██║█████╗██████╔╝██║   ██║██║     █████╔╝ ███████╗
╚██╗ ██╔╝╚════╝██╔══██╗██║   ██║██║     ██╔═██╗ ╚════██║
 ╚████╔╝       ██████╔╝╚██████╔╝╚██████╗██║  ██╗███████║
  ╚═══╝        ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝""")

faded_banner = fade.purpleblue(banner)

print(faded_banner)

global data

global codeas
codeas = input(f"{LM}[{M}input{LM}] {LC}How Many Fortnite Codes should i generate(it would be 50x your int()): {C}")
codeas = int(codeas)

def gen():
    #print(f"Gen Trhead started")
    global codeas
    codes = codeas
    try:
        for i in range(codes):
            code = "".join(random.sample(chars, 16))
            data = {
            "code": code
            }
            #print(f"Generated Code: {code}")
            response = requests.post(url = "https://www.fortnite.com/de/api/posa/code/status", data=data)
            response_text = response.text
            #print(response_text)
            #print(response.status_code)

            if response.status_code in i_codes:
                print(f"{W}[{LY}info{W}] {LR}Invalid V-Bucks Code: {R}|{code}|{LR}, response code: {LC}{response.status_code}{W}")
            elif response.status_code in stop_codes:
                if bad_counter > 60:
                    print(f"{W}[{LY}info{W}] Not Autorized response code, try to go on https://www.epicgames.com/fortnite/de/vbuckscard and restart")
                    input()
                    exit()
                print(f"{W}[{LY}info{W}] Invalid Response code {Y}401{W}")
                bad_counter+=1
            elif response.status_code in v_codes or response.status_code < 200:
                with open('codes.txt', 'a') as file:
                    file.write(f"Valid: {code}\n")
                print(f"{W}[{LY}info{W}] Valid V-Bucks Code: {G}|{code}|{W}, wrote to file: {LG}codes.txt{W}, response code: {LC}{response.status_code}{W}")
    except Exception as e:
        print(f"{R}Error: {LR}{e}")

threads = []



for i in range(50):
    t = threading.Thread(target=gen)
    threads.append(t)
    #print(f"Generated Thread: x{i+1}/{50*codeas}")

for i in range(50):
    threads[i].start()
    #print(f"Started Thread: x{i+1}/{50*codeas}")

for i in range(50):
    threads[i].join()
    #print(f"Joined Thread: x{i+1}/{50*codeas}")
