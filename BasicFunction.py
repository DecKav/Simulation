# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:42:57 2018

A simulation for an intelligent warehouse, using cars, nodes, and links.

@author: Declan Kavanagh
@author: Samuel Bloom


"""

import math

class Node:
    """ Represents a node in a warehouse that cars need to move between.
    Attributes:
        Name
        Location [x,y]
        Queue (car times)
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

    def getName(self):
        return self.name

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
        Task ID
        Start and finish nodes
        Deadline time to be completed by

    """
    def __init__(self, ID, node1, node2, duration):
        self.ID = ID
        self.start = node1
        self.finish = node2
        self.deadline = duration

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


class OrderTracker:
    """ A class which keeps track of the progress of all current tasks.
    Attributes:
        Current tasks
        Completed tasks
        Current node of car assigned to the task
        Task completion time
    """
    def __init__(self):
        self.currentTasks = {}
        self.completedTasks = {}

    def addNewTask(self, task):
         # Add all new tasks to this list
         self.currentTasks.append(task)
         print("Task", task.ID, "added to order list")


    def addCompletedTask(self, completeTask):
        #If a task has been completed, add it to this list
        self.completedTasks.append(completeTask)




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
        self.orders = OrderTracker()


    def addNode(self, name, x, y):
        nodeAdd = Node(name,x,y)
        self.nodes[nodeAdd.name] = nodeAdd
        print(name, "created.")

    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.ID] = carAdd
        print(carAdd.ID, "created.")

    def addLink(self, node1, node2):
        linkAdd = Link(node1, node2)
        self.links[linkAdd.name] = linkAdd
        print("Link",linkAdd.name, "created.")

    def addTask(self, ID, node1, node2, duration):
        taskAdd = Task(ID, node1, node2, duration)
        self.tasks[taskAdd.ID] = taskAdd
        print("Job number", taskAdd.ID, "created.")


    def time_step(self):
        linkRemove = []
        nodeRemove = []

        #Increments cars in nodes, and update tasks
        for node in self.nodes:
            nodeRemove = []
            for car in self.nodes[node].queue:
                self.nodes[node].queue[car] = self.nodes[node].queue[car] - 1 # Decrement the queue by 1 timestep

                #Check for cars finishing when the queue time is 0
                if self.nodes[node].queue[car] == 0:
                    nodeRemove.append(car)
                    print(car.ID, "finished at", node+".")

                # Check for completed tasks - for each node, check if the current car's
                # task ends at that node.
                if car.task.finish == node:
                    orders.addCompletedTask(car.task)
                    print(task, "completed.")

                #Remove finished cars
            if nodeRemove:
                for car in nodeRemove:
                    print(car.ID, "removed from", node+".")
                    self.nodes[node].removeCar(car)
                    car.state = 2

        #Increment cars in links
        for link in self.links:
            for car in self.links[link].queue:
                linkRemove = []
                self.links[link].queue[car] = self.links[link].queue[car] - 1
                #Check for cars finishing
                if self.links[link].queue[car] == 0:
                    linkRemove.append(car)
                    print(car.ID, "finished travelling along", link+".")

            #Remove finished cars
            if linkRemove:
                for car in linkRemove:
                    print(car.ID, "removed from", link+".")
                    self.links[link].removeCar(car)
                    car.state = 3

       #Move cars onto next state in task
        for car in self.cars:
            if self.cars[car].state == 2: # If car state is 'moving'
                #Progress from node to link
                sim.links["AB"].addCar(self.cars[car],6)
                self.cars[car].state = 1

            if self.cars[car].state == 3: # If car state is 'at node'
                #Progress from link to node
                sim.nodes[self.cars[car].task.finish.name].addCar(self.cars[car],6)
                self.cars[car].state = 1



if __name__ == "__main__":
    sim = Simulator()
    sim.addNode("nodeA", 1, 1)
    sim.addNode("nodeB", 2, 1)
    sim.addCar("Car1")
    sim.addLink(sim.nodes["nodeA"], sim.nodes["nodeB"])
    sim.addTask(1, sim.nodes["nodeA"], sim.nodes["nodeB"], 5)

    sim.cars["Car1"].addTask(sim.tasks[1])

    sim.nodes[sim.cars["Car1"].task.start.name].addCar(sim.cars["Car1"], 6)

    count = 0

    while(count<20):

        sim.time_step()
        count = count + 1
