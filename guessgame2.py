#!/bin/usr/env python 

import random 

def main():
	print "guess a number between one and ten"
	randomnumber = random.randint(1,10)
	catch = False 


	while not catch:
		userguess=input("guess your number here:")
		if userguess==randomnumber:
			print "congrats you won!"
			catch = True
		elif userguess>randomnumber:
			print "guess lower!"
		else:
			print "guess higher!"


	print "thanks for playing, come back again soon!"



if __name__=="__main__":
	main() 