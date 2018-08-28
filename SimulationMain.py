# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and links.


@author: Declan Kavanagh
@author: Sam Bloom

"""

class Node:
    """ Represents a node in a warehouse that cars need to move between.
    Attributes:
        ID = str(xy)
        Location [x,y]
        Queue (car times)
    """
    def __init__(self, x, y):
        self.ID = str(x)+str(y)
        self.x = x
        self.y = y
        self.queue = {}

    def addCar(self, Car, time):
        self.queue[Car] = time
        print(Car.ID, "added to", self.ID+".")

    def removeCar(self, Car):
        del self.queue[Car]

    def getID(self):
        return self.ID

    def getPos(self):
        return self.x, self.y


class Goods(Node):
    """ Represents a node in a warehouse that cars will retrieve and store goods at.
    Inherits from Node.
    Attributes:
        Goods
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)


class Picker(Node):
    """ Represents a node in a warehouse that cars will transport goods to.
    Inherits from Node.
    Attriubutes:
        Working Order
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)


class Charger(Node):
    """ Represents a node in a warehouse that cars will be charged at.
    Inherits from Node.
    Attributes:
        Charge Rate
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)


class Task:
    """ Represents a warehouse job.
    Attributes:
        Task ID
        Start and finish nodes
        Deadline time to be completed by
    """
    def __init__(self, ID, node1, node2, deadline):
        self.ID = ID
        self.start = node1
        self.finish = node2
        self.deadline = deadline

    def getStart(self):
        return self.start

    def getFinish(self):
        return self.finish

    def getID(self):
        return self.ID


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
        self.state = 1
        self.task = None
        self.x = 0
        self.y = 0

    def addTask(self, task):
        self.task = task
        self.state = 2

    def getID(self):
        return self.ID

    def getLocation(self):
        return self.x, self.y
    
    def setLocation(self, xNew, yNew):
        self.x = xNew
        self.y = yNew
    
    def moveToward(self, node):
        goalx, goaly = node.getPos()

        if (self.x == goalx) & (self.y == goaly):
            #Now at node
            self.state = 3
            print("Car", self.ID, "is already at Node", node.getID()+".")
            
        if (abs(self.x - goalx) > abs(self.y - goaly)):
            #Move in x dimension, further to go
            if(self.x > goalx):
                self.setLocation(self.x - 1, self.y)
                print("Car", self.ID, "moved left. New position:", self.getLocation())
            if(self.x < goalx):
                self.setLocation(self.x + 1, self.y)
                print("Car", self.ID, "moved right. New position:", self.getLocation())
                
        elif (abs(self.x - goalx) < abs(self.y - goaly)):
            #Move in y dimension, further to go
            if(self.y > goaly):
                self.setLocation(self.x, self.y - 1)
                print("Car", self.ID, "moved down. New position:", self.getLocation())
            if(self.y < goaly):
                self.setLocation(self.x, self.y + 1)
                print("Car", self.ID, "moved up. New position:", self.getLocation())
                
        elif (abs(self.x - goalx) == abs(self.y - goaly)):
            #Even distance, move x
            if(self.x > goalx):
                self.setLocation(self.x - 1, self.y)
                print("Car", self.ID, "moved left. New position:", self.getLocation())
            if(self.x < goalx):
                self.setLocation(self.x + 1, self.y)
                print("Car", self.ID, "moved right. New position:", self.getLocation())
                
        if (self.x == goalx) & (self.y == goaly):
            #Now at node
            self.state = 3
            print("Car", self.ID, "is now at Node", node.getID()+".")


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
        self.tasks = {}
        self.time = 0

    def addNode(self, x, y):
        nodeAdd = Node(x,y)
        self.nodes[nodeAdd.getID()] = nodeAdd
        print("Node", nodeAdd.getID(), "created.")

    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.getID()] = carAdd
        print("Car", carAdd.getID(), "created.")

    def addTask(self, ID, node1ID, node2ID, duration, carID):
        taskAdd = Task(ID, self.nodes[node1ID], self.nodes[node2ID], duration)
        self.tasks[taskAdd.getID()] = taskAdd
        self.cars[carID].addTask(taskAdd)
        print("Job number", taskAdd.getID(), "created.")

    def timeStep(self):
        self.time = self.time + 1
        print("Step Number:", self.time)
        # Iterate through every car
        for car in self.cars:
            current = self.cars[car]
            if current.state == 0: # If car state is 'charging'
                pass
            elif current.state == 1: # If car state is 'idling'
                pass
            elif current.state == 2: # If car state is 'moving'
                current.moveToward(current.task.start)
                
            elif current.state == 3: # If car state is 'at node'
                pass
        print("\n")


""" Main """
if __name__ == "__main__":
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(2, 2)
    sim.addCar(1)
    sim.addTask(1, "11", "22", 5, 1)
        
        
    
    
    count = 0
    while(count<20):

        sim.timeStep()
        count = count + 1
