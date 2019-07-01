#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" This module file be about python's control flow """

""" define a 16 bit hexadecimal variable """
hexadecimalnumber = 0x0000000000000005
""" degine a 8 bit binary variable """
binarynumber = 0b00000010
""" define a 8 bit octal variable """
octalnumber = 0o00000007
""" define a 2 bit decimal variable """
decimalnumber = 10

if decimalnumber == 10:
	print("bingo! the decimalnumber is ",decimalnumber)
elif octalnumber == 0o00000007:
	print("bingo! the octalnumber is ",octalnumber)	
else : #hexadecimalnumber == 0x0000000000000005
	print("bingo! the hexadecimalnumber is ",hexadecimalnumber)

print("The hexadecimalnumber is ",hexadecimalnumber)
print(hexadecimalnumber,"convert to decimal ",int(hexadecimalnumber))
print("The octalnumber is ",octalnumber)
print("The octalnumber ",octalnumber,"convert to binary ",bin(octalnumber))
print("The decimalnumber is ",decimalnumber)
print("The binarynumber is ",binarynumber)