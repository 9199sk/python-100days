#inheritance in python
# is ki use krke hm class ka name change kr skte hai
class employ:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self) :
        print(f"the name of empoly:{self.id}is{self.name}")
class program(employ):
    def showlanguage(self):
        print("The defualt language is python")

e1=employ("samir khan", 111)
e1.showdetails()
e2=program ("lucky", 112)
e2.showdetails()
e2.showlanguage()










