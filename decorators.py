from functools import wraps

def exception_decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except AttributeError:
            print("You must create a parking lot before you can do anything with vehicles")
        except Exception as e:
            print(f"Exception raised: {e}\nType 'help {f.__name__[3:]}' for information on this command")
    return wrapped