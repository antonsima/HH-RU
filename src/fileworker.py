import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR, JSON_DIR
from src.vacancy import Vacancy


class BaseFileWorker(ABC):
    """ Абстрактный класс для FileWorker """

    @abstractmethod
    def write_vacancies_to_file(self, vacancies: list['Vacancy']) -> None:
        pass

    @abstractmethod
    def read_vacancies_from_file(self) -> str:
        pass


class FileWorker(BaseFileWorker):
    def __init__(self, filename: str = 'vacancies.txt') -> None:
        self.__file_path = os.path.join(DATA_DIR, filename)
        self.__check_and_create()

    def __check_and_create(self) -> None:
        """
        Проверяет, существует ли файл, если нет создает его
        """

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('')

    def write_vacancies_to_file(self, vacancies: list['Vacancy']) -> None:
        """
        Принимает список экземпляров класса Vacancy и записывает информацию о них в файл
        """

        tmp_vacancies_info_list = []

        for vac in vacancies:
            tmp_vacancies_info_list.append(str(vac))

        tmp_vacancies_info_str = '\n'.join(tmp_vacancies_info_list)

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(tmp_vacancies_info_str)

    def read_vacancies_from_file(self) -> str:
        """
        Считывает информацию о вакансиях из файла
        """

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            vacancies_info = file.read()

        return vacancies_info


class JSONSaver:
    def __init__(self, filename: str = 'vacancies.json'):
        self.__file_path = os.path.join(JSON_DIR, filename)
        self.__check_and_create()

    def __check_and_create(self) -> None:
        """
        Проверяет, существует ли файл, если нет создает его
        """

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('[]]')

    def write_vacancies_to_file(self, vacancies: list[dict]) -> None:
        """
        Принимает список словарей вакансий, записывает их в файл в формате JSON
        """

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)
