# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and links.

Authors: 
    Declan Kavanagh
    Sam Bloom
        
Notes:
    Look for a graph library
    Investigate plotting nodes onto a graph rather than arbitrary
    Simulator as a time stepper and supervisor
    Queue, nodes have time steps required, car capacity, cars currently at node and remaining time, idle queue
    Start with two nodes, link, cars. Idling, queues, etc
"""

class Node:
    """ Represents a node in a warehouse that cars need to move between. 
    Has a location, represented by associated links.
    """
    def __init__(self):
        pass
    

class Charger(Node):
    """ Represents a node in a warehouse that cars will be charged at. 
    Inherits from Node, also has a charge rate and car capacity.
    """
    def __init__(self):
        Node.__init__(self)
        pass
    

class Picker(Node):
    """ Represents a node in a warehouse that cars will transport goods to. 
    Inherits from Node, has an order and associated car hold time.
    """
    def __init__(self):
        Node.__init__(self)
        pass
    

class Goods(Node):
    """ Represents a node in a warehouse that cars will retrieve and store goods at. 
    Inherits from Node, either contains required goods or is empty.
    """
    def __init__(self):
        Node.__init__(self)
        pass
    

class Link:
    """ Represents a link between nodes that cars will travel along. 
    Has two nodes it is connecting, and a travel distance/time.
    """
    
    def __init__(self, node1, node2, distance):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
    
    

class Car:
    """ Represents a car in the warehouse that will travel between nodes along links. 
    Has a number, current charge, location, and state. 
    
    Order, battery, what carrying, direction on link
    """
    population = 0

    def __init__(self, number, charge, state, location):
        """ Initialise a car. 
        number(int):
            Car identifier, must be unique.
        charge (int):
            % of battery charged at creation
        state(int):
            0 = Charging
            1 = Idling
            2 = Moving
            3 = At goods/picking node
        location(???):
            ???
        """
        self.number = number
        self.charge = charge
        self.state = state
        self.location = location
        Car.population += 1
    
    def change_state(self, newState):
        """ Change to a new state. 
        newState (int): 
            0 = Charging
            1 = Idling
            2 = Moving
            3 = At goods/picking node"""
        self.state = newState    
        
    def check_charge(self):
        """ Check the car's current battery charge. """
        return self.charge
    
    def update_charge(self):
        """ Change battery charge based on current state. """
        if self.state == 0:
            #Charging
            pass
        elif self.state == 1:
            #Idling
            pass
        elif self.state == 2:
            #Moving
            pass
        elif self.state == 3:
            #At node
            pass
        else:
            pass
   
class Simulator:
    pass

""" Main """


