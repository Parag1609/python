import builtins
from collections import ChainMap

# Defining a local variable
a = 10

# Creating a ChainMap of locals, globals, and builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

# Accessing variables through the ChainMap
print(pylookup['a'])  # Output: 10 (from locals())
print(pylookup['print'])  # Output: <built-in function print> (from builtins)
