# exercise6 next day complete
class library:
    def __init__(self) :
        self.nobooks=0
        self.books=[]
    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self): 
        print(f"the library has {self.nobooks}books.the books are")
        for book in self.books:
            print(book)
l1=library()
l1.addbooks("sameer potter 1")
l1.addbooks("aman potter 2")
l1.addbooks("lucky potter 3")
l1.addbooks("arbaz potter 4")
l1.showinfo()







