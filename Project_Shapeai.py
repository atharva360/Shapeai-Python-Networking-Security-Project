# WAP in Python to generate hashes of string data using 3 algorithms from hashlib.
int_val = int(input("Enter any integer value:"))
flt_val = float(input("Enter any float value:"))
str_val = input("Enter any string:")
print ("Hash value of" ,int_val, "is: " + str(hash(int_val)))
print ("Hash value of",flt_val, "is: " + str(hash(flt_val)))
print ("Hash value of",str_val, "is: " + str(hash(str_val)))


# WAP in Python to generate MD5 of string data
import hashlib
go = hashlib.md5(b'Atharva')
print("The byte of hash is : ", end = " ")
print (go.digest())


