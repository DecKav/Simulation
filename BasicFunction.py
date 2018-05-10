# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:42:57 2018

A simulation for an intelligent warehouse, using cars, nodes, and links.

@author: Declan Kavanagh
@author: Samuel Bloom

Next: different node types, automatic car change, jobs, car attributes, charge node/battery model, payload

"""

import math

class Node:
    """ Represents a node in a warehouse that cars need to move between. 
    Attributes:
        Name
        Location [x,y]
    """
    def __init__(self, name, x, y):
        self.name = name
        self.xPos = x
        self.yPos = y
        self.queue = {}
    
    def addCar(self, Car, time):
        self.queue[Car] = time
        print(Car, "added to", self.name+".")
    
    def removeCar(self, Car):
        del self.queue[Car]
        
class Goods(Node):
    """ Represents a node in a warehouse that cars will retrieve and store goods at. 
    Inherits from Node.
    Attributes:
        Goods
        Car Queue
    """
    def __init__(self, name, x, y):
        Node.__init__(self, name, x, y)

class Picker(Node):
    """ Represents a node in a warehouse that cars will transport goods to. 
    Inherits from Node.
    Attriubutes:
        Working Order
        Car Queue
    """
    def __init__(self, name, x, y):
        Node.__init__(self, name, x, y)

class Charger(Node):
    """ Represents a node in a warehouse that cars will be charged at. 
    Inherits from Node.
    Attributes:
        Charge Rate
        Car Queue
    """
    def __init__(self, name, x, y):
        Node.__init__(self, name, x, y)

class Task:
    
    def __init__():
        pass
      
class Link:
    """ Represents a link between nodes that cars will travel along. 
    Attributes:
        Connected Nodes
        Travel Distance/Time
    """
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.xDist = abs(node1.xPos - node2.xPos)
        self.yDist = abs(node1.yPos - node2.yPos)
        self.absDist = math.sqrt(self.xDist^2 + self.yDist^2)
        self.queue = {}
        self.name = node1.name.translate(str.maketrans('','','node'))+node2.name.translate(str.maketrans('','','node'))
        
    def addCar(self, Car, time):
        self.queue[Car] = time
        print(Car.ID, "added to", self.name+".")
    
    def removeCar(self, Car):
        del self.queue[Car]

        
class Car:
    """ Represents a car in the warehouse that will travel between nodes along links. 
    Attributes:
        Number (ID)
        Current Charge
        Current Location/Direction
        Current State 
    """
    def __init__(self, ID):
        self.ID = ID
        self.state = 0
    
    

class Simulator:
    """ Controls all nodes, links, and cars. Advances time, manages job list.  
    
    Attributes:
        Node list
        Link list
        Car list    
    """
    def __init__(self):
        self.nodes = {}
        self.cars = {}
        self.links = {}
    
    def addNode(self, name, x, y):
        self.nodes[name] = Node(name,x,y)
        print(name, "created.")
    
    def addCar(self, ID):
        self.cars[ID] = Car(ID)
        print(ID, "created.")
        
    def addLink(self, node1, node2):
        linkAdd = Link(node1, node2)
        self.links[linkAdd.name] = linkAdd
        print(linkAdd.name, "created.")
    
    def time_step(self):
        print("Stepping time.")
        
        for node in self.nodes:
            nodeRemove = []
            for car in self.nodes[node].queue:
                self.nodes[node].queue[car] = self.nodes[node].queue[car] - 1
                if self.nodes[node].queue[car] == 0:
                    nodeRemove = nodeRemove.append(car)
                    print(car, "finished at", node+".")
            #for car in nodeRemove:
                #node.removeCar(car)
                    
        for link in self.links:
            for car in self.links[link].queue:
                self.links[link].queue[car] = self.links[link].queue[car] - 1
                if self.links[link].queue[car] == 0:
                    #self.links[link].removeCar(car)
                    print(car.ID, "finished travelling along", link+".")
 
                   

if __name__ == "__main__":
    sim = Simulator()
    sim.addNode("nodeA", 1, 1)
    sim.addNode("nodeB", 2, 1)
    sim.addCar("Car1")
    sim.addLink(sim.nodes["nodeA"], sim.nodes["nodeB"])
    
    sim.nodes["nodeA"].addCar(sim.cars["Car1"].ID, 6)
    
    count = 0
    while(count<6):
        sim.time_step()
        count += 1
    
    sim.links["AB"].addCar(sim.cars["Car1"], 6)
    
    count = 0
    while(count<6):
        sim.time_step()
        count += 1
    
    sim.nodes["nodeB"].addCar(sim.cars["Car1"].ID, 6)
    count = 0
    while(count<6):
        sim.time_step()
        count += 1

