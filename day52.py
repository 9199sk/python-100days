#lemda function in python
def appl(fx,value):

    return 6+fx(value)

double=lambda x:x*2
cube= lambda x:x*x*x
avg= lambda x,y,z: (x+y+z)/2




print(double(5))#10
print(cube(5))#125

print(avg(5,8,9))
print(appl(lambda x:x*x,2))






