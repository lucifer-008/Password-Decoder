#!/usr/bin/python

import hashlib
from termcolor import colored
import crypt

hashvalue = input("[*] Enter Your String: ")
type = input("[*] Enter Your Hash Type: ")

hash1 = 'md5'
hash2 = 'sha1'
hash3 = 'sha256'
hash4 = 'sha384'
hash5 = 'sha512'
hash6 = 'sha224'
hash7 = 'blake2c'
hash8 = 'blake2b'
hash9 = 'encode'



if type == hash1:
	hashobj = hashlib.md5()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash2:
	hashobj = hashlib.sha1()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash3:
	hashobj = hashlib.sha256()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash4:
	hashobj = hashlib.sha384()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash5:
	hashobj = hashlib.sha512()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash6:
	hashobj = hashlib.sha224()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash7:
	hashobj = hashlib.blake2s()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash8:
	hashobj = hashlib.blake2b()
	hashobj.update(hashvalue.encode())
	print ("Here is Your Hash " +hashobj.hexdigest())
	quit()
elif type == hash9:
	hashobj = crypt.crypt(hashvalue, 'LU')
	print ("Here is Your Hash " +hashobj)
	quit()



print ("[!!] Please Enter Valid Hash  Type....!!!!!!!!")
