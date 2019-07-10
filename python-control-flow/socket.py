#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# continue statement will skip the after statement and go on

loopinit = 0b0
loopend = 0b1111
loopcontinue = 0b110

while loopinit < loopend:
	if loopinit == loopcontinue:
		loopinit = loopinit + 0b1
		print("continue the next loop, occur in ",bin(loopcontinue))
		continue
	print(loopinit," : ",bin(loopinit))
	loopinit = loopinit + 0b1

def f():
	pass