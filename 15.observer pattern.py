class Observer:
    def update(self, message):
        print("Received:", message)

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

observer1 = Observer()
observer2 = Observer()

subject = Subject()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify("New Notification!")
