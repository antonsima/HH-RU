import json
from abc import abstractmethod, ABC

import requests

from config import JSON_DIR


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
        while self.params.get('page') != 5:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies

hh_api = HeadHunterAPI()
vac = hh_api.get_vacancies('Python')

with open(f'{JSON_DIR}/information.json', 'w', encoding='utf-8') as file:
    json.dump(vac, file, ensure_ascii=False)
