from abc import ABC, abstractmethod
from typing import Any

import requests
from requests import Response


class BaseHeadHunterAPI(ABC):
    """ Абстрактный класс для HeadHunterAPI """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass

    @abstractmethod
    def __get_response(self, url: str, headers: dict, params: dict) -> 'Response':
        pass


class HeadHunterAPI(BaseHeadHunterAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:

        self.__url: str = 'https://api.hh.ru/vacancies'
        self.__headers: dict = {'User-Agent': 'HH-User-Agent'}
        self.__params: dict = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies: list[dict] = []

    def _BaseHeadHunterAPI__get_response(self, url: str, headers: dict, params: dict) -> Any:
        """
        Получение экземпляра класса Response
        """

        response = requests.get(url, headers=headers, params=params)

        return response

    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Получение списка вакансий в виде словарей
        """

        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self._BaseHeadHunterAPI__get_response(self.__url, self.__headers, self.__params)

            if response.status_code == 200:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                return self.__vacancies

        return self.__vacancies

    @property
    def vacancies(self) -> list[dict]:
        """ Геттер для вакансий """

        return self.__vacancies
