from abc import ABC, abstractmethod

import requests


class BaseHeadHunterAPI(ABC):
    """ Абстрактный класс для HeadHunterAPI """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass


class HeadHunterAPI(BaseHeadHunterAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.url: str = 'https://api.hh.ru/vacancies'
        self.headers: dict = {'User-Agent': 'HH-User-Agent'}
        self.params: dict = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies: list[dict] = []

    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Получение списка вакансий в виде словарей
        """

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies
