import os
from abc import ABC


class BaseWorker(ABC):
    pass


class JSONWorker(BaseWorker):
    def __init__(self, filename='vacancies.json'):
        self.__filename = filename
        self.__check_and_create()

    def __check_and_create(self):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'w', encoding='utf-8') as file:
                file.write('[]')