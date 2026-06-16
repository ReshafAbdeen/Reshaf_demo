def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World!")

say_hello()

