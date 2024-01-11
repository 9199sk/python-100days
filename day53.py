#map filter and reduce
def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,4,6,4,5,8]
# for item in l:


# newl=map(cube,l)
# print(newl)

newl=list(map(lambda x:x*x*x,l))
print(newl)
#filter

# filter
def filter_function(a):
    return a>4
newnewl=filter=list(filter(filter_function,l))
print(newnewl)










