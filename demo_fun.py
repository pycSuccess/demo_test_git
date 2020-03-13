#coding:utf-8
import time
import datetime

def use_time():
    time.sleep(3)
    print('say hello')
    return 200

# use_time()
def warpper(func):
    start  = datetime.datetime.now()
    res = func()
    end = datetime.datetime.now() - start
    print(end)
    return res

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        res = func(*args, **kwargs)
        end = datetime.datetime.now()-start
        print(end)
        return res
    return wrapper

def two(con_type):
    def timer(func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            res = func(*args, **kwargs)
            end = datetime.datetime.now() - start
            if con_type == 'fz':
               print('fz'+ str(end))
            return res
        return wrapper
    return timer



@two(con_type='fz')
def home():
    time.sleep(1)
    return 'home'

result = home()
print(result)
# warpper(use_time)