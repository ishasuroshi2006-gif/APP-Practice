def outer(message):
    def inner():
        print("Message:", message)
    return inner

greet = outer("Hello, Python!")

greet()
