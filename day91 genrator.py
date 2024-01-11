# Generator is very useful in python this is very fast
def my_genrator():
    # is se hamara memory save hota hai it is 
    # very fast
    for i in range (10):
        yield i
gen=my_genrator()        
 
for j in gen:
    print(j)