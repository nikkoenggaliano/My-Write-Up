#!/usr/bin/env python

from random import choice 
import string
s = string.printable

while True:
	j = 0
	final = ""
	key1 = "%c%c%c%c"%(choice(s), choice(s), choice(s) ,choice(s))
	padd = "-"
	final += key1 + padd + key1 + padd + key1 + padd + key1
	
	for i in final:
		j += ord(i)
	if j == 1655:
		print(final)
		


