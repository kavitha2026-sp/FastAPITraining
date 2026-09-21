#Concept: decorator
#lets you modify a funtion using @ symbol
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_hello():
    print("hello !")

say_hello()