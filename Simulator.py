# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:51:18 2018

@author: Declan Kavanagh
"""

from Node import Node, Charger
from Task import Task
from Car import Car
from collections import OrderedDict
import math
import sys

class Simulator:
    """ Controls all nodes, links, and cars. Advances time, manages job list.

    Attributes:
        Node list
        Car list
        Task list
        Time steps taken
    """
    def __init__(self):
        self.nodes = {}
        self.chargers = {}
        self.cars = {}
        self.tasks = OrderedDict()
        self.time = 0
        self.totalEnergy = 0
        self.moveCost = -5
        self.idleCost = -5
        self.nodeCost = -5
        self.chargeCost = 10
        self.taskEnergy = 0
        self.totalCost = 0
        root = Node(0,0)
        self.nodes[root.getID()] = root
        self.futureCost = 0
        self.totalTasks = 0
        self.horiz1 = 0
        self.horiz2 = 0
        self.output = []
        w, h = 10, 50;
        self.positions = [[0 for x in range(w)] for y in range(h)] 

    def addNode(self, x, y):
        nodeAdd = Node(x,y)
        self.nodes[nodeAdd.getID()] = nodeAdd
        print("Node", nodeAdd.getID(), "created.")
        
    def addCharger(self, x, y):
        nodeAdd = Charger(x,y)
        self.chargers[nodeAdd.getID()] = nodeAdd
        print("Charger", nodeAdd.getID(), "created.")

    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.getID()] = carAdd
        self.totalEnergy = self.totalEnergy + carAdd.getCharge()
        print("Car", carAdd.getID(), "created.")

    def addTask(self, ID, time, nodes):
        taskAdd = Task(ID, time, nodes)
        self.tasks[self.totalTasks] = taskAdd
        self.totalTasks = self.totalTasks + 1
        print("Job at time step", taskAdd.getTime(), "created.")
        
    def addTaskSet(self, tasks):
        for time, task in tasks.items():
            pass                
    
    def timeStep(self, thresh1, thresh2):
        self.time = self.time + 1
        print("Step Number:", self.time)   
        print("======")
        
        self.totalEnergy = 0
        self.totalCost = 0
        self.futureCost = 0
        self.horiz1 = 0
        self.horiz2 = 0
        
        
        #Iterate through tasks to establish current waiting cost and horizon cost
        for ID, task in self.tasks.items():
            if(task.getTime() <= self.time):
                prevNode = "00"
                for node in task.nodes:
                    currentNode = node
                    x1 = self.nodes[currentNode].getPos()[0]
                    x2 = self.nodes[prevNode].getPos()[0]
                    y1 = self.nodes[currentNode].getPos()[1]
                    y2 = self.nodes[prevNode].getPos()[1]
                    distance = abs(round(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0))
                    nodeTimeCost = task.nodes[node]*self.nodeCost*-1
                    moveTimeCost = distance*self.moveCost*-1
                    self.totalCost = self.totalCost + nodeTimeCost + moveTimeCost
                    prevNode = currentNode
                    
            if(task.getTime() <= self.time + 6) and (task.getTime() > self.time):
                prevNode = "00"
                for node in task.nodes:
                    currentNode = node
                    x1 = self.nodes[currentNode].getPos()[0]
                    x2 = self.nodes[prevNode].getPos()[0]
                    y1 = self.nodes[currentNode].getPos()[1]
                    y2 = self.nodes[prevNode].getPos()[1]
                    distance = abs(round(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0))
                    nodeTimeCost = task.nodes[node]*self.nodeCost*-1
                    moveTimeCost = distance*self.moveCost*-1
                    self.futureCost = self.futureCost + nodeTimeCost + moveTimeCost
                    prevNode = currentNode
                    
            if(task.getTime() <= self.time + 3) and (task.getTime() > self.time):
                prevNode = "00"
                for node in task.nodes:
                    currentNode = node
                    x1 = self.nodes[currentNode].getPos()[0]
                    x2 = self.nodes[prevNode].getPos()[0]
                    y1 = self.nodes[currentNode].getPos()[1]
                    y2 = self.nodes[prevNode].getPos()[1]
                    distance = abs(round(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0))
                    nodeTimeCost = task.nodes[node]*self.nodeCost*-1
                    moveTimeCost = distance*self.moveCost*-1
                    self.horiz1 = self.horiz1 + nodeTimeCost + moveTimeCost
                    prevNode = currentNode
                    
            if(task.getTime() <= self.time + 6) and (task.getTime() > self.time + 3):
                
                prevNode = "00"
                for node in task.nodes:
                    currentNode = node
                    x1 = self.nodes[currentNode].getPos()[0]
                    x2 = self.nodes[prevNode].getPos()[0]
                    y1 = self.nodes[currentNode].getPos()[1]
                    y2 = self.nodes[prevNode].getPos()[1]
                    distance = abs(round(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0))
                    nodeTimeCost = task.nodes[node]*self.nodeCost*-1
                    moveTimeCost = distance*self.moveCost*-1
                    self.horiz2 = self.horiz2 + nodeTimeCost + moveTimeCost
                    prevNode = currentNode
        
        
        #Iterate through idling cars
        i = 0
        for car in self.cars:
            self.positions[self.time][i] = self.cars[car].getLocation()[0]
            self.positions[self.time][i+1] = self.cars[car].getLocation()[1]
            i = i + 2
            if self.cars[car].getCharge() < 0:
                sys.exit("Car completely drained.")
            self.totalEnergy = self.totalEnergy + self.cars[car].getCharge()
            if self.cars[car].state == 1:
                """ This is basic control - 47 Time Steps
                if (self.tasks) and (self.cars[car].getCharge() > 35):
                    for ID, task in self.tasks.items():
                        if(task.getTime() <= self.time):
                            self.cars[car].addTask(self.tasks.pop(ID))
                            break
                """
                """ This is basic horizon control - 38 Time Steps
                if (self.tasks):
                    if (self.futureCost > self.totalCost):
                        self.cars[car].state = 0
                    else:
                        for ID, task in self.tasks.items():
                            if(task.getTime() <= self.time):
                                self.cars[car].addTask(self.tasks.pop(ID))
                                break
                """
                if (self.tasks):
                    if (self.horiz1 < self.horiz2):
                        self.cars[car].state = 0
                    else:
                        for ID, task in self.tasks.items():
                            if(task.getTime() <= self.time):
                                self.cars[car].addTask(self.tasks.pop(ID))
                                break
                elif (self.cars[car].getCharge() < 20):
                    self.cars[car].state = 0
                    print("Car", self.cars[car].getID(), "is now moving to be charged.")
                else:
                    self.cars[car].state = 1
               
        
        #Iterate through all node queues
        totalClear = []
        for node in self.nodes:
            carClear = []
            currentNode = self.nodes[node]
            for car in currentNode.queue: 
                #Decrease time of each car at node
                currentNode.queue[car] = currentNode.queue[car] - 1
                if currentNode.queue[car] == 0:
                    #Remove from queue
                    carClear.append(car)
                    totalClear.append(car)
                else:
                    print("Car", car.getID(), "is at Node", currentNode.getID(), "for", currentNode.queue[car], "more time steps.")
            if carClear:
                for car in carClear:
                    self.nodes[node].removeCar(car)
                    car.state = 2
                    car.progressTask()
                            
                    
        # Iterate through every car, update charge
        for car in self.cars:
            currentCar = self.cars[car]
            if currentCar not in totalClear:
                if currentCar.state == 0: # If car state is 'charging'
                    if(currentCar.moveTowardCharge(self.chargers["10"])==True):
                        currentCar.changeCharge(self.chargeCost)
                    else:
                        currentCar.changeCharge(self.moveCost)
                elif currentCar.state == 1: # If car state is 'idling'
                    currentCar.changeCharge(self.idleCost)
                    print("Car", currentCar.getID(), "idling at", str(currentCar.getLocation())+".")
                elif currentCar.state == 2: # If car state is 'moving'
                    currentCar.moveToward(self.nodes[currentCar.getCurrentNodeID()])
                    currentCar.changeCharge(self.moveCost)
                elif currentCar.state == 3: # If car state is 'at node'
                    currentCar.changeCharge(self.nodeCost)
            print("Car "+str(currentCar.getID())+" Charge: "+str(currentCar.getCharge())+"%")
            
            
        ##Change in energy
        print("======")
        delta = 0
        for car in self.cars:
            delta = delta + self.cars[car].getCharge()
        
        deltaE = delta - self.totalEnergy 
        print("Total Energy at start:", str(self.totalEnergy))
#        print("Average Energy at start:", str(self.totalEnergy/len(self.cars)))
        print("Energy Change in this step:", str(deltaE))
        
        self.totalEnergy = delta
        
        print("======")
        print("Current Job Queue Cost: "+str(self.totalCost))
        print("Total Horizon Job Cost: "+str(self.futureCost))
        print("Horizon 1 hr Job Cost: "+str(self.horiz1))
        print("Horizon 2 hr Job Cost: "+str(self.horiz2))
               
        
        
        print("\n")
        
        for car in self.cars:
            currentCar = self.cars[car]
            if currentCar.state == 2:
                return False
            if currentCar.state == 3:
                return False
        
        if not self.tasks:
            print("TERMINATE")
            return True
        
        return False