#!/usr/bin/python
# New little programs make 3 changes in this file
import string
from eledef import *

# New little programs listed here
import addnum
import tinyrpg

# Main part preparation
welcomeinfo = '''NOW YOU HAVE ENTERED
THE ELEPHANTVS SYSTEM
USERS INTERFACE
ENTER 'HELP' FOR ALL COMMANDS AVAILABLE'''
# New little programs APPENDED here
cmdlst=['HELP', 'EXIT', 'ADDNUM', 'TINYRPG']
def help():
    print 'HERE ARE THE COMMANDS AVAILABLE:'
    for cmd in cmdlst:
        print cmd+'\t',
    print '\n',

# The main part of the system
print welcomeinfo
print 'LATEST COMMAND UPDATED:',cmdlst[-1]
cmdinput = ''
while cmdinput != 'EXIT':
    print 'ENTER A COMMAND:'
    cmdinput = eleinput()
    if cmdinput == 'HELP':
        help()
# New little programs added here
    elif cmdinput == 'ADDNUM':
        addnum.run()
    elif cmdinput == 'TINYRPG':
        tinyrpg.run()
    else:
        if not cmdinput in cmdlst:
            print 'COMMAND NOT FOUND'
else:
    print 'EXITING ELEPHANTVS'
