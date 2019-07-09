#! /usr/bin/env python3

# loop statement

loopflag = 0b111
loopendpoint = 0b1111
loopstartpoint = 0b0

# print("loopflag = ",loopflag,", convert to binary = ",bin(loopflag))

# print("loopendpoint = ",loopendpoint,", convert to binary = ",bin(loopendpoint))
# print("loopstartpoint = ",loopstartpoint,", convert to binary = ",bin(loopstartpoint))

while bin(loopstartpoint) < bin(loopflag):
	print(loopstartpoint," : ",bin(loopstartpoint))
	loopstartpoint = loopstartpoint + 0b1