import functools
import time

def clock(func):
    @functools.wraps(func)  # Preserve the original function's metadata
    def clocked(*args, **kwargs):  # Wrapper function
        t0 = time.time()  # Start the timer
        result = func(*args, **kwargs)  # Call the original function
        elapsed = time.time() - t0  # Calculate elapsed time
        name = func.__name__  # Get the function name

        # Build argument string
        arg_lst = []
        if args:  # Handle positional arguments
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:  # Handle keyword arguments
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)  # Combine args and kwargs into one string

        # Log the result and execution time
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result  # Return the result of the original function
    return clocked  # Return the wrapper
