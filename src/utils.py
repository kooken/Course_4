from src.vacancies import Vacancy


def hh_vacancies_list(vacancies: list[dict]):
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
    sorted_vacancies = []
    for vacancy in vacancies:
        if vacancy.salary_from >= min_salary and vacancy.vacancy_currency == 'USD' or vacancy.vacancy_currency == 'usd':
            sorted_vacancies.append(vacancy)
    return sorted(sorted_vacancies)


def validate_salary_input():
    while True:
        salary = 0
        salary_query = input("Enter minimum desired salary: ")
        if not salary_query.isdigit():
            print("Enter an integer")
            continue
        elif int(salary_query) < 0:
            print("Enter an integer")
            continue
        else:
            salary = salary_query
            break
    return int(salary)


def vacancy_presentation(vacancies):
    while True:
        number = input("How many vacancies to print on the screen?\n"
                       "Enter an integer: ")
        if not number.isdigit():
            print("Enter an integer")
            continue
        else:
            break
    print("\nWhat we found for you:\n")
    for vacancy in vacancies[0:int(number)]:
        if vacancy.salary_to > 0:
            print(f'Vacancy: {vacancy.vacancy_name}\n'
                  f'Salary : {vacancy.salary_repr}\n'
                  f'Description: {vacancy.vacancy_skills[0].replace("<highlighttext>", "").replace("</highlighttext>",
                                                                                                   "")}\n'
                  f'Link: {vacancy.vacancy_url}\n'
                  f'\n')
        else:
            print(f'Vacancy: {vacancy.vacancy_name}\n'
                  f'Salary : от {vacancy.salary_from}\n'
                  f'Description: {vacancy.vacancy_skills.replace("<highlighttext>", "").replace("</highlighttext>",
                                                                                                "")}\n'
                  f'Link: {vacancy.vacancy_url}\n'
                  f'\n')
