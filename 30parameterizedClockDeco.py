import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# Outer decorator function
def clock(fmt=DEFAULT_FMT):  
    def decorate(func):  # Decorator function
        def clocked(*_args):  # Wrapper function
            t0 = time.time()  # Start time
            _result = func(*_args)  # Call the original function
            elapsed = time.time() - t0  # Calculate elapsed time
            name = func.__name__  # Function name
            args = ', '.join(repr(arg) for arg in _args)  # Format arguments
            result = repr(_result)  # Format result
            print(fmt.format(**locals()))  # Print the formatted string
            return _result  # Return the result of the original function
        return clocked  # Return the wrapper function
    return decorate  # Return the decorator function

if __name__ == '__main__':
    @clock()  # Apply the clock decorator
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)  # Call the decorated snooze function

    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)