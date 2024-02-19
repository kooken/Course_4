class Vacancy:
    """Класс, собирающий информацию с разных платформ и создающий унифицированный вариант вакансии для работы"""
    def __init__(
            self,
            vacancy_name: str,
            salary_from: int,
            salary_to: int,
            vacancy_currency: str,
            vacancy_skills: str,
            vacancy_duties: str,
            vacancy_url: str
    ):
        self.vacancy_name = vacancy_name
        self.salary_from = self.validate_salary(salary_from)
        self.salary_to = self.validate_salary(salary_to)
        self.salary_repr = self.salary_representation(salary_from, salary_to)
        self.vacancy_currency = self.validate_currency(vacancy_currency)
        self.vacancy_skills = vacancy_skills
        self.vacancy_duties = vacancy_duties
        self.vacancy_url = vacancy_url

    @staticmethod
    def validate_salary(salary):
        if salary is None:
            return 0
        return salary

    @staticmethod
    def validate_currency(currency):
        if currency == 'rub':
            currency = 'RUR'
        return currency

    def salary_representation(self, salary_from, salary_to):
        return f'{self.validate_salary(salary_from)} - {self.validate_salary(salary_to)}'

    def to_json(self):
        return {
            "vacancy_name": self.vacancy_name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "vacancy_currency": self.vacancy_currency,
            "vacancy_url": self.vacancy_url,
            "vacancy_skills": self.vacancy_skills,
            "vacancy_duties": self.vacancy_duties
        }

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        return self.salary_from > other.salary_from
