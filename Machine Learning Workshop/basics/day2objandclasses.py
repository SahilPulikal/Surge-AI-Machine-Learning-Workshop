# 
class Person:
    
    def __init__(self): #initialising variables / Constructor
      self.name = 'Raju'
      self.age = 20
    
    def talk(self):
        print(self.name)
        print(self.age)

p1=Person()
p1.talk()
print(p1.name)
print(p1.age)