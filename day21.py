# function argument
def average(a,b,c=3):
    print("the average is ",(a+b+c)/2)
average(8,10)
# defualt value are not provided
def name(fullname,midname="Samir",lastname="khan"):
    print("hello",fullname,midname,lastname)
name("md","Lucky","don")
#keyword example
#requried argument
average(5,6)
#variable length argunment
# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#         print("average is :",sum/len(numbers))
#         average(5,6,7,1)