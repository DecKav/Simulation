# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:42:57 2018

@author: decka
"""

import math

class Node:
    
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
        
        
class Link:
    
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.xDist = abs(node1.xPos - node2.xPos)
        self.yDist = abs(node1.yPos - node2.yPos)
        self.absDist = math.sqrt(self.xDist^2 + self.yDist^2)
        self.queue = {}
        
    def addCar(self, Car, time):
        self.queue[Car] = time
        print(Car.ID, "added to", self.node1.name+self.node2.name+".")
    
    def removeCar(self, Car):
        del self.queue[Car]

        
class Car:
    
    def __init__(self, ID):
        self.ID = ID
        self.state = 0
    
    

class Simulator:
    
    def __init__(self):
        self.nodes = {}
        self.cars = {}
        self.links = {}
    
    def addNode(self, name, x, y):
        self.nodes[name] = Node(name,x,y)
        print(name, "created. [Node]")
    
    def addCar(self, ID):
        self.cars[ID] = Car(ID)
        print(ID, "created. [Car]")
        
    def addLink(self, name, node1, node2):
        self.links[name] = Link(node1, node2)
        print(name, "created. [Link]")
    
    def time_step(self):
        print("Stepping time.")
        for node in self.nodes:
            for car in self.nodes[node].queue:
                self.nodes[node].queue[car] = self.nodes[node].queue[car] - 1
                if self.nodes[node].queue[car] == 0:
                    #self.nodes[node].removeCar(car)
                    print(car, "finished at", node+".")
                    
        for link in self.links:
            for car in self.links[link].queue:
                self.links[link].queue[car] = self.links[link].queue[car] - 1
                if self.links[link].queue[car] == 0:
                    #self.links[link].removeCar(car)
                    print(car.ID, "finished travelling along", link+".")
 
                   

if __name__ == "__main__":
    sim = Simulator()
    sim.addNode("nodeA", 1, 1)
    sim.addNode("nodeB", 2, 2)
    sim.addCar("Car1")
    sim.addLink("AB", sim.nodes["nodeA"], sim.nodes["nodeB"])
    
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
    