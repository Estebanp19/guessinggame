#!/bin/usr/env python 

import random 

def main():
	print "guess a number between one and ten"
	randomnumber = random.randint(1,10)
	DECISIVE = False 


	while not DECISIVE:
		userguess=input("guess your number here:")
		if userguess==randomnumber:
			print "congrats you won!"
			DECISIVE = True
		elif userguess>randomnumber:
			print "guess lower!"
		else:
			print "guess higher!!!!!"


	print "thanks for playing, come back again soon!"


if __name__=="__main__":
	main() 