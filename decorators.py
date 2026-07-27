def greet(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Thank You!")
    return wrapper

@greet
def message():
    print("Learning Python Decorators")

message()
