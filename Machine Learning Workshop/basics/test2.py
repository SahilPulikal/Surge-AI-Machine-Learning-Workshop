class Bank:
    
    def __init__(self): #initialising variables / Constructor
      self.accno = 100
      self.name = "Sahil"
      self.balance = 999
      self.__loanamt = 12345 #private variable
    
    def details(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        print(self.loanamt)

p1=Bank()
p1.details()