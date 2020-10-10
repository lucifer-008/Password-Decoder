#!/usr/bin/python

import crypt
from termcolor import colored
from urllib.request import urlopen


passfile = input("[+] Please specify the path of user:password file: ")
dictionary = input("[+] Please specify the path of simple password file: ")



def crackPass(cryptWord):
	salt = cryptWord[0:2]
	try:
		list = open(dictionary, 'r')
		for word in list.readlines():
			word = word.strip('\n')
			cryptPass = crypt.crypt(word, salt)
			if cryptWord == cryptPass:
				print (colored("[+] Cogratulations, Password Found: " + word, 'yellow'))
				return
	except:
		Pass = open('PassWord.txt', 'r')
		for PassWord in Pass.readlines():
			PassWord = PassWord.strip('\n')
			Crypt = crypt.crypt(PassWord, salt)
			if cryptWord == Crypt:
				print (colored("[+] Congratulations, Password found: "+PassWord, 'yellow'))
				return


def main():
	try:
		password = open(passfile, 'r')
	except:
		print ("[!!] Please specify the Path....!!!!!!")
	for line in password.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print ("[*] Cracking Password For: "+ user)
			crackPass(cryptWord)

main()
