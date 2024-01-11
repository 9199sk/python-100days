# python class and object
class  person:
    name="samir"
    occupation="software devloper"
    netorth=5000
    def info(self):
        print(f"{self.name} is a {self.occupation}")


#self parameter

a=person()
b=person()
a.name ="lucky"
a.occupation="accountant"


b.name="aman"
b.occupation="dervloper"
print(a.name, a.occupation)

a.info()
b.info()














