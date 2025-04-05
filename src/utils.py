from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def sort_vacancies(vacancies):
    """
    Сортировка по убыванию зарплаты от
    """

    return sorted(vacancies, reverse=True)


def filter_vacancies_requirements(vacancies_list, filter_words):
    """
    Фильтрация по требованиям к навыкам
    """

    filtered_vacancies = []

    for vac in vacancies_list:
        for word in filter_words:
            if word.lower() in vac.requirements.lower():
                filtered_vacancies.append(vac)

    return filtered_vacancies


def filter_vacancies_city(vacancies_list, filter_city):
    """
    Фильтрация по городу
    """

    filtered_vacancies = []

    for vac in vacancies_list:
        if filter_city.lower() in vac.city.lower():
            filtered_vacancies.append(vac)

    return filtered_vacancies


def filter_vacancies_salary(vacancies_list, filter_salary):
    """
        Фильтрация по зарплате от
        """

    filtered_vacancies = []

    for vac in vacancies_list:
        if vac.salary_from >= filter_salary:
            filtered_vacancies.append(vac)

    return filtered_vacancies


def print_vacancies(top_vacancies):
    """
    принт вакансий одной за другой в консоль
    """

    for vac in top_vacancies:
        print(vac)


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filter_city = input("Введите город для фильтрации вакансий: ")
    salary_range = input("Введите зарплату от: ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    sorted_vacancies_list = sort_vacancies(vacancies_list)

    filtered_vacancies_by_words = filter_vacancies_requirements(sorted_vacancies_list, filter_words)
    filtered_vacancies_by_city = filter_vacancies_city(filtered_vacancies_by_words, filter_city)
    filter_vacancies_salary = filter_vacancies_salary(filtered_vacancies_by_city, salary_range)

    top_vacancies = filter_vacancies_salary[0:top_n]

    print_vacancies(top_vacancies)
