#python dictionaries:

dic= {
    344:"apple juice",
    547: "mango juice",
    665:"banana juice",
    548:"kaju 1 kg pak:"
}
dic2=int(input("enter your code:"))

if 344 in dic:
    print("apple juice")
if 547 in dic:
    print("mango juice")
if 665 in dic:
    print("banana juice")
if 548 in dic:
    print("kaju 1kg pak:") 
else:
    print("this item code is not provide")               

#accessing dictionary items
info={'name':"samir","age":18,"eligble":True}
print(info)
print(info['name'])
print(info.get("eligble"))


for key in info.keys():
    print(info[key])

