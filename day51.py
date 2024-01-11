# seek()and tell()function
with open ('file.txt','r')as f:
    print(type(f))
#move to the 10 bytes in the file
f.seek(10)
#read the seek next 5 bytes

data=f.read(5)
print(data)
















