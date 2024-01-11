#manipulating tuples
#is trah se hm tuplr ko change kr skte hai directly nhi
countries=("india","nepal","pakistan")
temp=list(countries)
temp.append("russia")
temp.pop(3)#remove krne ke liye apend ko
temp[2]="hindustand"#change item

countries=tuple(temp)
print(countries)

#15 kitni no pr hai.index
num=(1,9,7,2,15,1,8,2)
s=num.index(15)
print(s)