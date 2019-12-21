# base class accept radius from user
# derived class volume of sphere
# derived class area of circle

class Radius(object):
    def __init__(self, fname):
      # self.name = fname
      # self.color = "red"
      self.radius = fname = int(input("enter radius of circle"))
      
    # def horn(self):
    #     print("peep peep")

class Volofsphere(Radius):
    def __init__(self, fname, num_wheels):
      self.num_wheels = num_wheels
      super().__init__(fname)
      self.color = "green"
      vol=4/3(3.14*fname^3)
      print(vol)

class AreaOfCircle(Radius):
    def __init__(self, fname, num_wheels):
      super().__init__(fname)
      self.color = "blue"
      self.wheels = num_wheels

# veh_1 = Vehicle('Four wheeler')
# c_1 = Car("second four wheeler",4)
# m_1 = MarutiEsteem

# print("Vehicle:",id (veh_1))
# print("CustomVehicle:",id (c_1))

# print(veh_1.color)
# print(veh_1.name)
# print(c_1.color)
# print(c_1.vehicle_name)
# print(c_1.name)
# c_1.horn()

Vehicle