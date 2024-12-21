from types import MappingProxyType

# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Create a read-only proxy of the original dictionary
proxy_dict = MappingProxyType(original_dict)

# Accessing items through the proxy
print(proxy_dict['a'])  # Output: 1
print(proxy_dict['b'])  # Output: 2

# Modifications to the proxy will raise a TypeError
try:
    proxy_dict['a'] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# Modifying the original dictionary will be reflected in the proxy
original_dict['a'] = 99
print(proxy_dict['a'])  # Output: 99 (reflects the change in the original dictionary)

# Deleting items from the original dictionary will also reflect in the proxy
del original_dict['b']
print(proxy_dict)  # Output: {'a': 99, 'c': 3}
