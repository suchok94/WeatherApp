from abc import ABC, abstractmethod


class IWWeatherDataPublisher(ABC):
    
    @abstractmethod
    def add_subscriber(self, subscriber):
        pass
    
    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class WeatherData(IWWeatherDataPublisher):
    
    def __init__(self):
        self.__subscribers = []

    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber):
        self.__subscribers.remove(subscriber)
    
    def notify(self):
        for subscriber in self.__subscribers:
            subscriber.update()
    
class IClientSubscriber(ABC):

    @abstractmethod
    def update(self):
        pass

class Client(IClientSubscriber):

    def __init__(self):
        pass

    def update(self, message):
        pass