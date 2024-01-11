#joing set kese kre

s1={1,2,3,5}
s2={3,5,6,9,}
print(s1.union(s2)) #{1,2,3,5,6,9}

#update krne ka rule
s1.update(s2)
print(s1,s2)

#intersection ka use krke double use latter ko dekh skte hai
cities={"patna ","mumbai","kolkata"}
cities2={"nepal","mumbai"}
cities3=cities.intersection(cities2)
print(cities3)

#symmetric_differemce and symmetric_difference_update
cities={"patna ","mumbai","kolkata"}
cities2={"nepal","mumbai","patna"}
cities3=cities.symmetric_difference(cities2)
print(cities3)


#set method
#1-isdisjointt()
#isme koi intersection nhi hota

cities={"patna2 ","mumbai","kolkata"}
cities2={"nepal","mumbai1","patna"}
print(cities.isdisjoint(cities2))   #true all word change 1 and 2

#issuperset
cities={"patna ","mumbai","kolkata"}
cities2={"nepal","mumbai","patna"}
print(cities.issuperset(cities2))  #(false) beacuse cities 2 word not in the cities 1

#issubst
cities={"patna ","mumbai","kolkata"}
cities2={"nepal","mumbai","patna"}
print(cities.issubset(cities2))  #(false) beacuse cities 2 word not in the cities 1

# add method
cities={"patna ","mumbai","kolkata"}
cities.add("darbhanga")
print(cities)

#remove/discard
cities={"patna ","mumbai","kolkata"}
cities.remove("patna ")
print(cities)

# pop method use remove item
cities={"patna ","mumbai","kolkata"}
item=cities.pop("patna")
print(cities)
print(item)

#del method
cities8={"patna ","mumbai","kolkata"}
del cities
print(cities8)

#clear method
cities9={"patna ","mumbai","kolkata"}
cities9.clear()
print(cities9)



info={"carla",19,False,5.6,19}
if "carla" in info:
    print("carla is present")
else:
    print("carla is absent") 
    


