#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2021, 9, 19)
playday = datetime.date(2021, 9,18)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    

    def checkg(n):
        check=0
        for digit in (n):
            if(int(digit)==0):
                check=check+1
        return check
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet RXCE'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @smsn_knt")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        check=checkg(last2)
        if(newperiod%2==0):
            sum=getSum(current)+check
            if(sum%2==0):
                print(newperiod+1," : RED")
            else:
                print(newperiod+1,"  : GREEN")
        else:
            sum=getSum(current)+check+1
            if(sum%2==0):
                print(newperiod+1,"   : RED")
            else:
                print(newperiod+1,"   : GREN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
            #print(numbers)
            
if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (True):
            period=170
            hero()
    elif(now>First and now<Firstend):
            period=280
            hero()
    elif(now>Third and now<Thirdend):
            period=372
            hero()
    elif(True):
            period=230
            hero()
    else:
        banner='figlet RXCE'
        print("Hi!! 🤑Thanks for buying the hack🤑")
        print("----------⌛Your play time⌛----------")
        print("5 Sept 2021, 11:00 AM- 11:30 AM")
        print("5 Sept 2021, 02:00 PM- 02:30 PM")
        print("5 Sept 2021, 05:42 PM- 08:AM PM")
        print("5 Sept 2021, 06:37 PM- 08:30 AM")
        print("Please play on the given time, and ")
        


else:
    banner='figlet RXCE'
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
