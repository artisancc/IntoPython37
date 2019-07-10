#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Break out of the innermost enclosing for or while loop

loopendpoint = 0b111
loopbreakpoint = 0b11
loopinit = 0b0

while loopinit < loopendpoint:
	if loopinit == loopbreakpoint:
		print("the while loop was break, occur in the ",bin(loopbreakpoint))
		break
	print(loopinit," : ",bin(loopinit))
	loopinit = loopinit + 0b1