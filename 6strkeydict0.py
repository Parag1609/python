class StrKeyDict0(dict): 
 def __missing__(self, key):
    if isinstance(key, str): 
        raise KeyError(key)
        return self[str(key)] 
 def get(self, key, default=None):
    try:
        return self[key] 
    except KeyError:
        return default 
 def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()
 

d = StrKeyDict0({1: "one", "2": "two"})

# Access using `__getitem__` (square brackets)
print(d[1])       # Key 1 converts to '1', Output: "one"
print(d["2"])     # Key "2" found directly, Output: "two"
print(d.get(3))   # Key 3 not found, Output: None
print(d.get(3, "NA")) # Key 3 not found, Output: "NA"

# Check membership using `in`
print(1 in d)     # Converts 1 to '1', Output: True
print("3" in d)   # "3" not found, Output: False
