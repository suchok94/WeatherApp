from abc import ABC, abstractmethod
import requests

class IRequest(ABC):

    @abstractmethod
    def give_data(self):
        pass

class WeatherRequest(IRequest):

    def give_data(self):
        data = self.__do_request()
        return data

    def __do_request(self, city_name, api_key):
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Fail retrieve weather data: {response.status_code} {response.text}")