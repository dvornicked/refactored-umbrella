class Observer:
    def __init__(self, name, observable):
        self.name = name
        observable.subscribe(self)

    def notify(self, observable, message):
        print(f'{self.name} got {message} from {observable.name}')


class Observable:
    def __init__(self, name):
        self.name = name
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for obs in self._observers:
            obs.notify(self, message)

    def unsubscribe(self, observer):
        self._observers.remove(observer)
