#instance vs class variables
class employee:
    def __init__(self,name):
        self.name=name
        def showdetails(self):
            print("the name the employee is {self.name}")
emp1=employee("harry")
# emp1.showdetails()
employee.showdetails(emp1)






