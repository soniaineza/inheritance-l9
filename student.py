class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname, self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year
obj=student("priyanka","gaba",2024)
obj.printname()
print(obj.year)


