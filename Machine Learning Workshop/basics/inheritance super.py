class Vehicle(object):
    def __init__(self, fname):
      self.name = fname
      self.color = "red"
      
    def horn(self):
        print("peep peep")

class Car(Vehicle):
    def __init__(self, fname, num_wheels):
      self.mum_wheels = num_wheels
      super().__init__(fname)
      self.color = "green"

class MarutiEsteem(Vehicle):
    def __init__(self, fname, num_wheels):
      super().__init__(fname)
      self.color = "blue"
      self.wheels = num_wheels

veh_1 = Vehicle('Four wheeler')
c_1 = Car("second four wheeler",4)
# m_1 = MarutiEsteem

print("Vehicle:",id (veh_1))
print("CustomVehicle:",id (c_1))

print(veh_1.color)
print(veh_1.name)
print(c_1.color)
print(c_1.vehicle_name)
print(c_1.name)
c_1.horn()