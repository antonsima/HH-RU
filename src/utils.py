import json
import os

from config import JSON_DIR
from src.api import HeadHunterAPI
from src.fileworker import FileWorker, JSONSaver
from src.vacancy import Vacancy
from tests.variables_for_tests import test_vacancies


def sort_vacancies(vacancies: list['Vacancy']) -> list['Vacancy']:
    """
    Сортировка по убыванию зарплаты от
    """

    return sorted(vacancies, reverse=True)


def filter_vacancies_requirements(vacancies_list: list['Vacancy'], filter_words: list[str]) -> list['Vacancy']:
    """
    Фильтрация по требованиям к навыкам
    """

    filtered_vacancies = []

    for vac in vacancies_list:
        for word in filter_words:
            if word.lower() in vac.requirements.lower():
                filtered_vacancies.append(vac)

    return filtered_vacancies


def filter_vacancies_city(vacancies_list: list['Vacancy'], filter_city: str) -> list['Vacancy']:
    """
    Фильтрация по городу
    """

    filtered_vacancies = []

    for vac in vacancies_list:
        if filter_city.lower() in vac.city.lower():
            filtered_vacancies.append(vac)

    return filtered_vacancies


def filter_vacancies_salary(vacancies_list: list['Vacancy'], filter_salary: int) -> list['Vacancy']:
    """
    Фильтрация по зарплате от
    """

    filtered_vacancies = []

    for vac in vacancies_list:
        if vac.salary_from >= filter_salary:
            filtered_vacancies.append(vac)

    return filtered_vacancies


def print_vacancies(top_vacancies: list['Vacancy']) -> None:
    """
    принт вакансий одной за другой в консоль
    """

    for vac in top_vacancies:
        print(vac)


def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filter_city = input("Введите город для фильтрации вакансий: ")
    salary_range = int(input("Введите зарплату от: "))

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    sorted_vacancies_list = sort_vacancies(vacancies_list)

    filtered_vacancies_by_words = filter_vacancies_requirements(sorted_vacancies_list, filter_words)
    filtered_vacancies_by_city = filter_vacancies_city(filtered_vacancies_by_words, filter_city)
    filtered_vacancies_by_salary = filter_vacancies_salary(filtered_vacancies_by_city, salary_range)

    top_vacancies = filtered_vacancies_by_salary[0:top_n]

    txt_saver = FileWorker('vacancies.txt')
    txt_saver.write_vacancies_to_file(top_vacancies)

    json_saver = JSONSaver('vacancies.json')
    json_saver.write_vacancies_to_file(hh_vacancies)

    print_vacancies(top_vacancies)

vacancies_list = Vacancy.cast_to_object_list(test_vacancies)

print_vacancies(vacancies_list)