# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

"""
Goods/Picking classes
Charging bays, queue
Ruleset into Simulator? Car?
Input battery characteristics?
Proportional vs Unit cost for actions?
Collision checks
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
    print("Initialisation:")
    print("")
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(2, 2)
    sim.addNode(1, 2)
    sim.addCar(1)
    sim.addCar(2)
    taskNodes1 = OrderedDict()
    taskNodes1["11"] = 2
    taskNodes1["22"] = 3
    taskNodes1["12"] = 2
    sim.addTask(taskNodes1)
    taskNodes2 = OrderedDict()
    taskNodes2["22"] = 1
    taskNodes2["12"] = 1
    taskNodes2["11"] = 1
    sim.addTask(taskNodes2)
    
    print("\n")
    
    count = 0
    while(count<15):

        sim.timeStep()
        count = count + 1
