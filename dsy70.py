# class Method as alternative constructor
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=Employee("sameer",80000)
print(e1.name)      
print(e1.salary)

string="samir-80000"
e2=Employee(string.split("_"),800000)
print(e2.name)
print(e2.salary)
      
















