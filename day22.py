#list argunment
#hm list ke sath boolean string print kr skte hai
#isme list of no 4 hai agr print 5 krge to error aayega
marks=[3,5,6,"samir",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# agr no check krna hai list me hai ki nshi
if "samir" in marks:
    print("yes")
else:
    print("no")    #output yes

#same chj apply string ke liye bhi hoti hai
if "mi" in "samir":
    print("yes")

else:
    print("no")   #output yes
#this is jump index
print(marks[1:2:3])    
