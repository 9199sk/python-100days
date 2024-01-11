# method overriding in python
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y 

rec=shape(8,9)
print(rec.area())




