from collections import UserDict

class MyDict(UserDict):
    def __getitem__(self, key):
        print(f"Getting the value for {key}")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"Setting value for {key} to {value}")
        super().__setitem__(key, value)

# Creating an instance of MyDict
my_dict = MyDict()

# Setting and getting items
my_dict['a'] = 1
print(my_dict['a'])  # Output: Getting the value for a 1
