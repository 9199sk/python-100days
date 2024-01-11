#exception handling in python
#kisi bhi number ka table
a=int(input("enter a number:"))
print(f"multiplication table of {a} is:")

for i in range(1,11):
    print(f"{a}X{i}={a*i}")
   



# a=int(input("enter a number:"))
# print(f"multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#      print(f"{a}X{i}={a*i}")
# except :
#   print("invalid input")
# print("some of lines of code")


#alg alg trh ke error check krene ke liye
try:
    n=int(input("entere an interger:"))
    a=[3,6]
    print (a[n])
except ValueError:
    print("no inter number is no. integer")

except IndexError:
    print("indexerror")


