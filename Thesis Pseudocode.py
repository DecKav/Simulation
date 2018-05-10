### Thesis project pseudocode

### Sam Bloom


### Notes ###
# Control everything at the top level through the timestep function! It will control the whole simulation
# Directed graph structure/layout for the simulation - specify node locations and links between them - find a graph library
# Focus on simulator- carts, nodes and links between nodes for now - orders and optimisation can wait until later

# Include number of timesteps for each process at each node - include dynamics of each process in the Node class, not the cart - it should be
# encoded into the graph since it's invariant to which cart is doing it
# To decide which cart goes where, test number of distance steps taken with each timestep, and assign based on how little time it will take for
# a cart to get to a node

### First step  for next meeting - start simple, get 2 nodes, queue of carts at node A, go to B along the link, perform a task and then sit idle ###

class Cart(object):
# A class to simulate the robotic cart

### Attributes:
# Battery charge
# Location (x,y)
# Current load/item carried
# Current task
# Schedule of future tasks

        def __init__(self, x, y, velocity, charge_level, load, task, schedule):
                self._x = x
                self._y = y
                self._velocity
                self._charge_level = charge_level
                self._load = load
                self._task = task
                self._schedule = schedule

### Methods:
# Find shortest path to task
# Get time to complete task


class ChargingStation(cart_capacity, charging_rate):
# A class to simulate the robot charging station

### Attributes:
# Number of robots present
# Rate of charging

class Node(x, y, orders):
# A class to simulate processing/delivery nodes of the system
### Attributes
# Node location
# Queue of orders/tasks expected (backlog)
# Current time expected
    self._x = x
    self._y = y

class Task(destination_node, deadline_time):
# A class for keeping track of each new task which is added to the schedule


class Simulator(carts, nodes, orders):
# Simulator for the system
### Attributes
# Number of carts
# Number of nodes
# Links between nodes
# Overeall cart battery levels
# Backlog of orders
# Total time expected

   def get_carts
   def get_nodes
	def get_orders

	def setup_graph #Set up the graph with nodes, links and carts
	def create_schedule # Get the current orders and arrange them into a schedule
	def assign_tasks # Assign tasks to each robot based on proximity
	def assign_optimal_paths #Find the optimal paths for each robot to take between nodes



def main():
# The main function which runs the program.        
     
# Initialise, run and handle the end of the simulation
        while(1):
                initialise_simulation()
                timestep()
                end_simulation()

def initialise_simulation():
    simulator = Simulator(carts, nodes, orders)

    simulator.setup_graph()
    simulator.create_schedule()
    simulator.assign_tasks()
    simulator.assign_optimal_paths()


def timestep():
# The timestep function which increments and updates the overall system
# Move the carts to their new positions based on path
# get new orders
# Update order schedule
# Re-allocate tasks to robots
# Re-allocate which carts are charging and which are in service
# Re-optimize path planning

        def check_for_new_orders
        def update_order_schedule
        def reassign_tasks
        def update_charging_carts
        def assign_new_optimal_paths


def end_simulation():
# Function for handling the end of the simulation once the timestep() function finishes
        



