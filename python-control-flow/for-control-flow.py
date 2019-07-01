#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" This module file be about python's for control flow statement """
""" define a binary variable """
loopflag = 0b000
loopflagshift = loopflag ^ 1
loopendpoint = 0b100
#loopflag = loopflag ^ 1


while loopendpoint > loopflag:
	# print(int(loopflag)+1," position is ",bin(loopflag))
	loopflag = loopflag ^ 1
	
# print("loopflag : ",bin(loopflag),", loopflag convert to decimal : ",int(loopflag))
# print("loopflagshift : ",bin(loopflagshift),", loopflagshift convert to decimal : ",int(loopflagshift))
# print("loopendpoint : ",bin(loopendpoint),", loopendpoint convert to decimal : ",int(loopendpoint))

# if loopflag < loopflagshift:
# 	print("loopflag < loopflagshift ",bin(loopflag),' ',bin(loopflagshift))
# elif loopflag == loopflagshift:
# 	print("loopflag = loopflagshift ",bin(loopflag),' ',bin(loopflagshift))
# else:
# 	print("loopflag > loopflagshift ",bin(loopflag),' ',bin(loopflagshift))




# while loopflag > loopflagshift:
# 	#print("loopflag = loopflagshift ",bin(loopflag),' ',bin(loopflagshift))
# 	print(int(loopflag),": loopposition ",bin(loopflag))
# 	loopflagshift = loopflagshift ^ 1
# print("loopflag's type is ",type(loopflag))
# print("loopflagshift's type is ",type(loopflagshift))
# print("loopendpoint's type is ",type(loopendpoint))
# while int(loopendpoint).equals(int(loopflag)):
# 	print(int(loopflag),": loopposition ",bin(loopflag))
# 	loopflag = loopflag ^ 1
# 	print(int(loopflag),": loopposition ",bin(loopflag))

# print(bin(loopflag))
# print("loopflag bit left shift 1 is ",bin(loopflag) ^ 1)
# loopflag = bin(loopflag) ^ 1
# print("loopflag bit left shift 1 is ",bin(loopflag) ^ 1)
# loopflag = bin(loopflag) ^ 1
# print("loopflag bit left shift 1 is ",bin(loopflag) ^ 1)

