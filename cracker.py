#!/usr/bin/python

from urllib.request import urlopen
from termcolor import colored
import hashlib



print ("Follow Me On The Github:-- https://github.com/lucifer-008")

hash = input("Enter Hash Value: ")
Hash = input("Enter Hash Name: ")
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
hash1 = 'sha1'
hash2 = 'sha256'
hash3 = 'sha512'
hash4 = 'md5'
hash5 = 'sha384'

hash6 = 'sha224'


hash7 = 'blake2c'
hash8 = 'blake2b'





for password in passlist.split('\n'):
	if Hash == hash1:
		hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password......", 'red'))
	elif Hash == hash2:
		hashguess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))
	elif Hash == hash3:
		hashguess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password......", 'red'))
	elif Hash == hash4:
		hashguess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))
	elif Hash == hash5:
		hashguess = hashlib.sha384(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))
	elif Hash == hash6:
		hashguess = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))


	elif Hash == hash7:
		hashguess = hashlib.blake2s(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))
	elif Hash == hash8:
		hashguess = hashlib.blake2b(bytes(password, 'utf-8')).hexdigest()
		if hashguess == hash:
			print (colored("[*] Password is "+str(password), 'green'))
			quit()
		else:
			print (colored(str(password)+" not matched. Trying another password.......",'red'))





print ("Password not  found :( :( :( :(")
 
