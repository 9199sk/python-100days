#match case statement
x=int(input("enter the value of x : "))
#x is a variable to match 
match x:
    case 0:
        print("x is zero")
    case 5:
        print("case is 5") 
    case _ if x==90:
        print(x,"x is  equal to 90")
    
    case _ if x==79:
        print(x,"this is eual to x")




    case _:
        print(x,"this is not match any number")

     