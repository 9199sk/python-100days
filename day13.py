#string are immutable
a="sameer!!! sameer !!!"
b="khan"
#latter ko capital and small krne ka rule
print(len(a))
print(a.upper())
print(b.lower())

#use are strip
print(a.rstrip("!"))
print(a.replace("sameer","lucky"))
#use split
print(a.split(" "))


#first latter ko big krne ke liye
mywebsite="my New webpage"
print(mywebsite.capitalize())

#senence ko center me lane ke liye
str1="welcome to mannu college"
print(str1.center(50))
print(len(str1))

#kon sa word string me kitni bar aa rha hai
print(a.count("sameer"))

#line ending check
str1="welcome to mannu college"
print(str1.endswith("college"))
print(str1.endswith("to",5,10))

#find string
h="my name is sameer khan"
print(h.find("is"))

#alphanumric check
h1="ibelongtodarbhangadistric"
print(h1.isalnum())
#chekck is alpha
h1="Darbhanga"
print(h1.isalpha())

#cheklower case
h2="Khanbhai"
print(h2.islower())

#check printable
h3="we wish youhappy birthday \n"
print(h3.isprintable())

#check space
h4="      "
print(h4.isspace())

#chek title
h5="Mathama Gandhi"
print(h5.istitle())

h6="we wish youhappy birthday \n"
print(h6.startswith("we"))

#small to capital latter convert
h2="we wish youhappy birthday \n"
print(h2.swapcase())

#convert title
h3="we wish youhappy birthday brother "
print(h3.title())


