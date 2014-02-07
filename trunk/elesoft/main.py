#!/usr/bin/python
import string
welcomeinfo = '''NOW YOU HAVE ENTERED
THE ELEPHANTVS SYSTEM
USERS INTERFACE
ENTER 'HELP' FOR HELP'''
cmdlst=['HELP','EXIT']
def help():
	print 'HERE ARE THE COMMANDS AVAILABLE:'
	for cmd in cmdlst:
		print cmd+'\t',
	print '\n',
def eleinput():
	tmp = raw_input().upper()
	return tmp
	
# The main part of the system
print welcomeinfo
cmdinput = ''
while cmdinput != 'EXIT':
	print 'ENTER A COMMAND:'
	cmdinput = eleinput()
	if cmdinput == 'HELP':
		help()
	else:
		if not cmdinput in cmdlst:
			print 'COMMAND NOT FOUND'
else:
	print 'EXITING ELEPHANTVS'
