from src.classes import HHApi
from src.json_saver import JSONSaver
from pathlib import Path
from src.utils import hh_vacancies_list, sort_vacancies_by_salary, validate_salary_input, vacancy_presentation

VACANCIES_JSON = Path.cwd() / 'vacancies_list.json'
def main():
    json_file = JSONSaver(VACANCIES_JSON)

    search_query = input("Введите поисковый запрос: ")

    min_salary = validate_salary_input()

    hh_api = HHApi(search_query)

    hh_vacs = hh_vacancies_list(hh_api.get_vacancies())

    json_file.add_vacancies(hh_vacs)

    sorted_vacancies_by_salary = sort_vacancies_by_salary(hh_vacs, min_salary)
    if len(sorted_vacancies_by_salary) == 0:
        print("Нет подходящих вакансий")
    else:
        print(f"Мы подобрали {len(sorted_vacancies_by_salary)} вакансий")
        vacancy_presentation(sorted_vacancies_by_salary)


if __name__ == '__main__':
    main()
