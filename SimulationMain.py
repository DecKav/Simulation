# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

"""
Energy cost of jobs
"""


from collections import OrderedDict
from Simulator import Simulator

def optimise(simulator):
    """
    Set initial guess (worst case with finite sol) thresholds for:
        Send to charge if task available vs take task (Thresh1)
        Send to charge if no task available vs send to idle (Thresh2)
    While timestep == true
        Simulate operation, count steps
    Second guess thresholds
    While timestep == true
        Simulate operation, count steps
    Based on time steps from guesses, new guess to converge on optimal solution
    Return thresholds, time steps, and optimal solution
    """
    thresh1 = 60
    thresh2 = 60
    
    finish = False
    
    while(finish == False):
        finish = simulator.timeStep(thresh1, thresh2)
        
    first = simulator.time
    
    return first
    
    
    

if __name__ == "__main__":
    print("=======================")
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(1, 2)
    sim.addNode(2, 1)
    sim.addNode(2, 2)
    sim.addCharger(1, 3)
    sim.addCar(1)
    sim.addCar(2)
    taskNodes1 = OrderedDict()
    taskNodes1["11"] = 2
    taskNodes1["12"] = 2
    taskNodes1["11"] = 2
    sim.addTask(1, taskNodes1)
    sim.addTask(3, taskNodes1)
    sim.addTask(5, taskNodes1)
    sim.addTask(7, taskNodes1)
    taskNodes2 = OrderedDict()
    taskNodes2["21"] = 2
    taskNodes2["22"] = 2
    taskNodes2["21"] = 2
    sim.addTask(2, taskNodes2)
    sim.addTask(4, taskNodes2)
    sim.addTask(6, taskNodes2)
    sim.addTask(8, taskNodes2)
    
    
    print("=======================")
    print("\n")
    
    print(optimise(sim))
