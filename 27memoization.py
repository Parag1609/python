import functools, time

def clock(func):  # Outer function
    def clocked(*args):  # Inner function
        t0 = time.perf_counter()
        result = func(*args)  # Accessing func from enclosing scope
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked  # Return inner function

@functools.lru_cache() # 
@clock # 
def fibonacci(n):
 if n < 2:
    return n
 return fibonacci(n-2) + fibonacci(n-1)
if __name__=='__main__':
 print(fibonacci(6))






