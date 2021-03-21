from abc import ABCMeta, abstractmethod

"""
Define an interface for creating an object,
but let subclasses decide which class to instantiate. 
Factory Method lets a class defer instantiation to subclasses.

Products are: Truck and Ship
Factories are: RoadLogistics, SeaLogistics
Each factory is responsible for creating a type of object.
"""
class Transport(metaclass=ABCMeta):
    def __init__(self, capacity=0):
        self.capacity = capacity
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):

    def deliver(self):
        print("Delivered items by Truck with Capacity of {}".format(self.capacity))

class Ship(Transport):
    def deliver(self):
        print("Delivered items by Ship with Capacity of {}".format(self.capacity))

class Logistics(metaclass=ABCMeta):
    @abstractmethod
    def create_transport(self):
        pass
    @abstractmethod
    def plan_delivery(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self):
        self.transport = Truck(capacity=200)

    def plan_delivery(self):
        self.transport.deliver()


class SeaLogistics(Logistics):
    def create_transport(self):
        self.transport = Ship(capacity=5000)

    def plan_delivery(self):
        self.transport.deliver()



if __name__ == '__main__':
    RL = RoadLogistics()
    SL = SeaLogistics()
    RL.create_transport()
    RL.plan_delivery()
    SL.create_transport()
    SL.plan_delivery()
