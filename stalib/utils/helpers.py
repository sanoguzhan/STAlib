import time



def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        for x in range(5000):
            results = func(*args, **kwargs)
        t2 = time.time()
        print('%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0))
        return results
    return wrapper