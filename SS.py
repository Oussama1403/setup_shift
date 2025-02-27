#! /usr/bin/python3 

import os
import yaml
from colorama import Fore
art = """ 
 ___  ____  ____  __  __  ____    ___  _   _  ____  ____  ____ 
/ __)( ___)(_  _)(  )(  )(  _ \  / __)( )_( )(_  _)( ___)(_  _)
\__ \ )__)   )(   )(__)(  )___/  \__ \ ) _ (  _)(_  )__)   )(  
(___/(____) (__) (______)(__)    (___/(_) (_)(____)(__)   (__) 
"""
def installer(packages):
    print(Fore.YELLOW + "\nType 'all' to install all packages or choose a single package\n")
    i = 1
    for p in packages:
        print(Fore.RED + '[',i,']',p[0],'\n')
        i = i+1
    option = input(":$ ")
    if not option == "all":
        option = int(option)
        if (option in range(0,len(packages)+1) ):
            os.system(packages[option-1][1])
    else:
        for i in range(len(packages)):
            cmd = packages[i][1]
            os.system(cmd)    
    
def add():
    print(Fore.YELLOW + "What's the name of the automated command: ")
    pack_name = str(input(':$ '))
    print(Fore.YELLOW + "What's the command to run the command: ")
    pack_com = str(input(':$ '))
    pack = [pack_name,pack_com]
    return pack


def main():
    print(art)
    print(Fore.CYAN + "[!] The idea by: @elfalehdev and shoutout to @cryptolake for the update.\n")
    print(Fore.RED + "[1] Install packages \n[2] Add a package to the config\n") 
    option = int(input(":$ "))
    with open('config.yaml','r') as file:
        config = yaml.safe_load(file)
        packages = config['packages']
    if (option == 1):
            installer(packages)
    elif (option == 2):
        with open('config.yaml','w') as file:
            config['packages'].append(add())
            yaml.dump(config,file)
            
if __name__=='__main__':main()
