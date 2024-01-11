#list many types of method

n=[2,4,3,6,5,1]
print(n)
 #end me koi number add krne ke liye
n.append(112)
print(n)
#output[2,3,6,5,1,112]


n.sort()#accending order me short
print(n)
#output[1,2,3,4,5,6]

n.sort(reverse=True)#decending order rule
print(n)
#output[112,6,5,4,3,2,1]

n.reverse() #last to first show latter
print(n)
 #output[1.5.6.3.2.1]

print(n.count(6))#koi no kitni baraa rha hai count krne ke liye
print(n) #output[2]


print(n)
#dusri file ko copy krne ke liye
m=n.copy()
m[0]=0
print(n)

# insert method 
n.insert(4,786) #position 4 ki pas786
print(n)

# index method
# n ko open kr end me m ki value ko put
m=[785,86,542,545]
n.extend(m)
print(n)
#concanating two list
m=[2112,55,55]
k=m+n
print(k)
# print (n.index(3))