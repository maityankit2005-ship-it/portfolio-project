#class person:
 #   def __init__(self,fname,lname):
  #      self. firstname= fname
   #     self. lastname=lname
#
 #   def printname(self):
  #      print(self.firstname,self.lastname)
#
#class student(person):
 #   def __init__(self, fname, lname,marks):
  #      super().__init__(fname, lname)
   #     self.graduationyear = 2019
    #    self.marks = marks
    #def show(self):
     #   print(self.marks)
#
#x=student("karthik","malasi",67)
#print(x.graduationyear)
#x.printname()
#x.show()

#class employee:
#    def __init__(self,name,salary):
 #       self.name =name
  #      self.salary=salary

   # def xyz(self):
    #    print(self.name,self.salary)

#class manager(employee):
 #   def __init__(self, name, salary,department):
  #      super().__init__(name, salary)
   #     self.department=department
    #def show(self):
     #   print(self.department)

#x=manager("priyanshu",200000,"internal")
#print(x.name)
#x.xyz()
#x.show()


class marks:
    def __init__(self,m1,m2):
        self.marks=m1
        self.marks=m2
    
    def show_marks(self):
        print(self.marks1, self.marks2)
