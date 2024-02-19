import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class Saver(ABC):
    """Класс для сохранения полученных данных в JSON"""
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies) -> None:
        pass


class JSONSaver(Saver):

    @staticmethod
    def currency_cut(vacancies: list[Vacancy]):
        """Отбирает вакансии только с зарплатой в рублях"""
        filtered_vacancies = []
        for vacancy in vacancies:
            if vacancy.vacancy_currency == 'RUR':
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def add_vacancies(self, vacancies):
        """Записывает вакансии в JSON"""
        all_vacancies = [vacancy.to_json() for vacancy in self.currency_cut(vacancies)]
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)