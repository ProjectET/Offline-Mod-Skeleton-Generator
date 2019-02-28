#!/usr/bin/python2.7
import os
import sys
from shutil import copyfile

try:
    os.mkdir("Output")
except OSError:
    pass

def coderun():
    z = 0
    x = 0
    c = 0
    v = 0
    erz = None
    erx = None
    erc = None
    erv = None

    cred()
    try:
        Mn = raw_input("Enter Mod name (No spaces or special characters): ")
        Mn = Mn.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not Mn:
            raise ValueError
        else:
            z = 1
    except ValueError:
        erz = "Mod name"
    
    try:
        Md = raw_input("Enter Mod display name: ")
        if not Md:
            raise ValueError
        else:
            x = 1
    except ValueError:
        erx = "Mod display name"

    try:
        It = raw_input("Enter 1st Item's name (No spaces or special characters): ")
        It = It.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not It:
            raise ValueError
        else:
            c = 1
    except ValueError:
        erc = "1st Item's name"
    
    try:
        MA = raw_input("Enter your username: ")
        if not MA:
            raise ValueError
        else:
            v = 1
    except ValueError:
        erv = "Username"
    b = z + x + c + v
    if b == 4:
        try:
            os.makedirs(os.path.join("Output", Mn, "Items"))
        except OSError:
            print "Dir exists - skipping."

        copyfile("Templates/Items/itemname.png", os.path.join("Output", Mn, "Items", It + ".png"))
        copyfile("Templates/modname.csproj.user", os.path.join("Output", Mn, Mn + ".csproj.user"))
        
        bldr = open(os.path.join("Templates", "build.txt")).read()
        bldr = bldr.replace('{username}', MA).replace('{displayname}', Md)
        build = open(os.path.join("Output", Mn, "build.txt"), "w")
        build.write(bldr)
        
        dscr = open(os.path.join("Templates", "description.txt")).read()
        dscr = dscr.replace('{displayname}', Md)
        desc = open(os.path.join("Output", Mn, "description.txt"), "w")
        desc.write(dscr)

        Itcr = open(os.path.join("Templates", "Items", "itemname.cs")).read()
        Itcr = Itcr.replace("{modname}", Mn).replace("{itemname}", It)
        Itcs = open(os.path.join("Output", Mn, "Items", It + ".cs"), "w")
        Itcs.write(Itcr)

        mncr = open(os.path.join("Templates", "modname.cs")).read()
        mncr = mncr.replace('{modname}', Mn)
        mncs = open(os.path.join("Output", Mn, Mn + ".cs"), "w")
        mncs.write(mncr)

        mnpr = open(os.path.join("Templates", "modname.csproj")).read()
        mnpr = mnpr.replace('{modname}', Mn)
        mnpj = open(os.path.join("Output", Mn, Mn + ".csproj"), "w")
        mnpj.write(mnpr)
    else:
        cred()
        print "ERROR | Following field(s) are empty.\n-----------------------------------"
        if z != 1:
            print erz
        if x != 1:
            print erx
        if c != 1:
            print erc
        if v != 1:
            print erv
        print ""

def cred():
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    print "TModloader Mod Skeleton Generator\n\nCreated by ProjectET.\nOriginal mod skeleton generator by jopojelly."
    print "--------------------------------------------------------------------------\n"

while True:
    coderun()
    while True:
        lsg = raw_input("Would you like to generate another skeleton? Enter 'y', otherwise 'n' to close. ")
        if lsg.lower() == 'y':
            break
        elif lsg.lower() == 'n':
            sys.exit(0)
        else:
            print "Invalid command. To generate another skeleton, enter 'y' otherwise 'n' to close.\n"
