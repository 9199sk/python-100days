#super keyword in python
class parentclass:
    def parent_method(self):
        print("this is parent method.")
class childclass(parentclass):
    def parent_method(self):
         print("samir")
    def child_method(self):
            print("this is the child method.")
            super().parent_method()

child_object=childclass()
child_object.childmethod()
child_object.parent_method()





