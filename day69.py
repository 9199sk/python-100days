#what are python class method
class Employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    def changecompany(cls, newcompany):
        cls.company=newcompany

e1=Employee()
e1.name="sameer"
e1.show()
e1.changecompany("tesla")
e1.show()
print(Employee.company)





