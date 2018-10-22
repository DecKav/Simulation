# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

"""
Charging bays, queue
Ruleset into Simulator? Car?
Aggregate vs Individual battery management
Fleet thresholds - Different rulesets?

Have warehouse aware of demand over the day
Maximise spare capacity
Two cases, full charger and stop taking jobs
See Simulator decision making
"""


from collections import OrderedDict
from Simulator import Simulator

if __name__ == "__main__":
    print("=======================")
#    sim = Simulator()
#    sim.addNode(1, 1)
#    sim.addNode(2, 2)
#    sim.addNode(1, 2)
#    sim.addCar(1)
#    sim.addCar(2)
#    taskNodes1 = OrderedDict()
#    taskNodes1["11"] = 2
#    taskNodes1["22"] = 3
#    taskNodes1["12"] = 2
#    sim.addTask(taskNodes1)
#    taskNodes2 = OrderedDict()
#    taskNodes2["22"] = 1
#    taskNodes2["12"] = 1
#    taskNodes2["11"] = 1
#    sim.addTask(taskNodes2)
    
    sim = Simulator()
    
    sim.addNode(1,1)
    sim.addNode(3,1)
    sim.addCharger(2,2)
    
    sim.addCar(1)
    sim.addCar(2)
    
    taskNodes1 = OrderedDict()
    taskNodes1["31"] = 4
    taskNodes1["11"] = 2
    taskNodes1["31"] = 3
    
    sim.addTask(taskNodes1)
    
    print("=======================")
    print("\n")
    
    count = 0
    while(count<20):

        sim.timeStep()
        count = count + 1
