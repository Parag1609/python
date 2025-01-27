
class TwilightBus: 
    """A bus model that makes passengers vanish"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] 
        else:
            self.passengers = passengers 
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)
"""The problem here is that the bus is aliasing the list that is passed to the constructor.
Instead, it should keep its own passenger list. The fix is simple: in __init__, when the
passengers parameter is provided, self.passengers should be initialized with a copy
of it,"""

def __init__(self, passengers=None):
 if passengers is None:
    self.passengers = []
 else:
    self.passengers = list(passengers)
