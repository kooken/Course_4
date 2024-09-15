from abc import ABC, abstractmethod
import requests


class API(ABC):
    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        pass


class HHApi(API):
    def __init__(self, query: str):
        self.query = query
        self.params = {
            'text': self.query,
            'page': 0,
            'per_page': 100,
            'only_with_salary': True,
            'search_field': 'name'
        }

    def get_vacancies(self) -> list[dict]:

        response = requests.get('https://api.hh.ru/vacancies', params=self.params).json()
        return response['items']
