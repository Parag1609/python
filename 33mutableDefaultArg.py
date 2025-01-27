class HauntedBus:
    def __init__(self, passengers=[]): 
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

"""bus1 = HauntedBus()

bus1.pick('Alice')
bus1.pick('Bob')
print(bus1.passengers)  # ['Alice', 'Bob']
bus1.drop('Alice')
print(bus1.passengers)  # ['Bob']
"""
# Create two buses
bus1 = HauntedBus()
bus2 = HauntedBus()

# Add passengers to bus1
bus1.pick('Alice')

# Check passengers in both buses
print(bus1.passengers)  # ['Alice']
print(bus2.passengers)  # ['Alice'] <-- Unexpected!


"""The default value of passengers ([]) is a mutable object (list).
When a mutable default argument is used, it is shared among all 
instances of the class that do not explicitly pass a value for passengers."""
