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
        print(Car.ID, "added to", self.name+".")
    
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
    """ Represents a warehouse job.
    Attributes:
        Node list
        Time at each stage
    
    """
    def __init__(self, ID, node1, node2):
        self.ID = ID
        self.start = node1
        self.finish = node2
      
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
        
    State(int):
            0 = Charging
            1 = Idling
            2 = Moving
            3 = At goods/picking node
    """
    def __init__(self, ID):
        self.ID = ID
        self.state = 0
        self.task = None
    
    def addTask(self, task):
        self.task = task
        self.state = 1

class Simulator:
    """ Controls all nodes, links, and cars. Advances time, manages job list.  
    
    Attributes:
        Node list
        Link list
        Car list
        Task list
    """
    def __init__(self):
        self.nodes = {}
        self.cars = {}
        self.links = {}
        self.tasks = {}
    
    def addNode(self, name, x, y):
        self.nodes[name] = Node(name,x,y)
        print(name, "created.")
    
    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.ID] = carAdd
        print(carAdd.ID, "created.")
        
    def addLink(self, node1, node2):
        linkAdd = Link(node1, node2)
        self.links[linkAdd.name] = linkAdd
        print(linkAdd.name, "created.")
        
    def addTask(self, ID, node1, node2):
        taskAdd = Task(ID, node1, node2)
        self.tasks[taskAdd.ID] = taskAdd
        print("Number", taskAdd.ID, "job created.")
    
    def time_step(self):
        linkRemove = []
        nodeRemove = []
        
        #Increments cars in nodes
        for node in self.nodes:
            nodeRemove = []
            for car in self.nodes[node].queue:
                self.nodes[node].queue[car] = self.nodes[node].queue[car] - 1
                #Check for cars finishing
                if self.nodes[node].queue[car] == 0:
                    nodeRemove = nodeRemove.append(car)
                    print(car.ID, "finished at", node+".")
            #Remove finished cars
            if nodeRemove:
                for car in nodeRemove:
                    print(car.ID, "removed from", node+".")
                    node.removeCar(car)
                    car.state = 2
        
        #Increment cars in links            
        for link in self.links:
            for car in self.links[link].queue:
                linkRemove = []
                self.links[link].queue[car] = self.links[link].queue[car] - 1
                #Check for cars finishing
                if self.links[link].queue[car] == 0:
                    linkRemove = linkRemove.append(car)
                    print(car.ID, "finished travelling along", link+".")
            #Remove finished cars
            if linkRemove:
                for car in linkRemove:
                    link.removeCar(car)
                    car.state = 3
        
       #Move cars onto next state in task             
        for car in sim.cars:
            if self.cars[car].state == 2:
                #Progress from node to link
                sim.links["AB"].addCar(car,6)
                self.cars[car].state = 1
                
            if self.cars[car].state == 3:
                #Progress from link to node
                #Dependent on path assigned
                sim.nodes[self.cars[car].task.finish.name].addCar(car,6)
                self.cars[car].state = 1 

if __name__ == "__main__":
    sim = Simulator()
    sim.addNode("nodeA", 1, 1)
    sim.addNode("nodeB", 2, 1)
    sim.addCar("Car1")
    sim.addLink(sim.nodes["nodeA"], sim.nodes["nodeB"])
    sim.addTask(1, sim.nodes["nodeA"], sim.nodes["nodeB"])
    
    sim.cars["Car1"].addTask(sim.tasks[1])
    
    sim.nodes[sim.cars["Car1"].task.start.name].addCar(sim.cars["Car1"], 6)
    
    count = 0
    
    while(count<50):
        
        sim.time_step()
        count = count + 1
        
                
                
        
    """
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
    """

