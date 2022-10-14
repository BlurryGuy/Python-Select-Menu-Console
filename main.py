from pick import pick
import sys
import time
import os
from colorama import Fore,init,Back,Style

init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def first_function():
    print("You picked the first option")
    input()

def second_function():
    print("You picked the second option")
    input()

def print01(chat):
    for i in chat:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
        
print01(Fore.GREEN + "> " + Fore.RESET + "Press Enter to continue")

input()

cls()

title = 'Please choose a option: '

os.system("color a")

options = ['Cool Option 1', 'Another Cool Option 2']

option, index = pick(options, title, indicator='->', default_index=0)

if index == 0:

   first_function()
   
elif index == 1:

     second_function()
