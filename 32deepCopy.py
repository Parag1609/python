import copy

class Bus:
    def __init__(self, passengers=None):
        self.passengers = passengers if passengers else []

    def drop(self, name):
        self.passengers.remove(name)

    def drop(self, name):
        self.passengers.remove(name)

# Create an instance of Bus
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])

# Create shallow and deep copies
bus2 = copy.copy(bus1)     # Shallow copy
bus3 = copy.deepcopy(bus1) # Deep copy

# Display IDs of the bus objects
print("IDs of bus objects:")
print(id(bus1), id(bus2), id(bus3))

# Modify bus1
bus1.drop('Bill')

# Check the passengers in each bus
print("\nPassengers after dropping 'Bill' from bus1:")
print("bus1 passengers:", bus1.passengers)
print("bus2 passengers:", bus2.passengers)
print("bus3 passengers:", bus3.passengers)

# Display IDs of the passengers list
print("\nIDs of passengers list:")
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
