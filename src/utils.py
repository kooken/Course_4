from src.vacancies import Vacancy


def hh_vacancies_list(vacancies: list[dict]):
    """Создает экземпляр класса Vacancy, принимая данные от НН по заданным полям"""
    vacancies_list = []
    for vacancy in vacancies:
        example_vacancy = Vacancy(
            vacancy_name=vacancy['name'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_currency=vacancy['salary']['currency'],
            vacancy_skills=vacancy['snippet']['requirement'],
            vacancy_duties=vacancy['snippet']['responsibility'],
            vacancy_url=vacancy['alternate_url']
        )
        vacancies_list.append(example_vacancy)
    return vacancies_list


def sort_vacancies_by_salary(vacancies: list[Vacancy], min_salary=0):
    """Фильтрует вакансии по заданной пользователем минимальной зарплате в рублях"""
    sorted_vacancies = []
    for vacancy in vacancies:
        if vacancy.salary_from >= min_salary and vacancy.vacancy_currency == 'RUR' or vacancy.vacancy_currency == 'rub':
            sorted_vacancies.append(vacancy)
    return sorted(sorted_vacancies)


def validate_salary_input():
    """Валидирует ввод ползователем минмальной зарплаты"""
    while True:
        salary = 0
        salary_query = input("Введите минимальную желаемую ЗП: ")
        if not salary_query.isdigit():
            print("Введите целое число")
            continue
        elif int(salary_query) < 0:
            print("Введите целое число")
            continue
        else:
            salary = salary_query
            break
    return int(salary)


def vacancy_presentation(vacancies):
    """Выводит конечный результат пользователю"""
    while True:
        number = input("Сколько вывести на экран?\n"
                       "Введите целое число: ")
        if not number.isdigit():
            print("Введите целое число")
            continue
        else:
            break
    print("\nВот, что мы для Вас подобрали:\n")
    for vacancy in vacancies[0:int(number)]:
        # if vacancy.vacancy_skills:
        #     skills = vacancy.vacancy_skills.split('.')
        if vacancy.salary_to > 0:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'ЗП : {vacancy.salary_repr}\n'
                  f'Описание: {vacancy.vacancy_skills[0].replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n'
                  f'\n')
        else:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'ЗП : от {vacancy.salary_from}\n'
                  f'Описание: {vacancy.vacancy_skills.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n'
                  f'\n')
