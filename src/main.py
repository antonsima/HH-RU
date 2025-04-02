import json

import requests
from abc import ABC, abstractmethod

url_get = "https://api.hh.ru/vacancies" # используемый адрес для отправки запроса

response = requests.get(url_get, headers={'User-Agent': 'HH-User-Agent'}, params={'text': 'Python', 'page': 19, 'per_page': 100}) # отправка GET-запроса

print(response) # вывод объекта класса Response


print(response.status_code) # вывод статуса запроса, 200 означает, что всё хорошо, остальные коды нас пока не интересуют и их можно считать показателем ошибки


print(response.text) # печать ответа в виде текста того, что вернул нам внешний сервис

print(response.json()) # печать ответа в виде json-объекта того, что нам вернул внешний сервис
# Вывод:

with open('../json/information.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)




class BaseHeadHunterAPI(ABC):
    """ Абстрактный класс для HeadHunterAPI """

    @property
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class HeadHunterAPI(BaseHeadHunterAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies


class Vacancy():
    def cast_to_object_list(self):



if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Пример работы конструктора класса с одной вакансией
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                      "Требования: опыт работы от 3 лет...")

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)


    # Функция для взаимодействия с пользователем
    def user_interaction():
        platforms = ["HeadHunter"]
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)


    if __name__ == "__main__":
        user_interaction()
