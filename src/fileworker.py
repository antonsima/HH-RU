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


class BaseJSONSaver(ABC):
    """ Абстрактный класс для FileWorker """

    @abstractmethod
    def write_vacancies_to_file(self, vacancies: list[dict]) -> None:
        pass

    @abstractmethod
    def get_vacancies_from_file(self) -> list[dict]:
        pass

    @abstractmethod
    def delete_vacancies_from_file(self) -> None:
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

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            for vac in vacancies:
                if str(vac) not in file:
                    tmp_vacancies_info_list.append(str(vac))

        tmp_vacancies_info_str = '\n'.join(tmp_vacancies_info_list)

        with open(self.__file_path, 'a', encoding='utf-8') as file:
            file.write(tmp_vacancies_info_str + '\n\n')

    def read_vacancies_from_file(self) -> str:
        """
        Считывает информацию о вакансиях из файла
        """

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            vacancies_info = file.read()

        return vacancies_info

    def add_vacancies(self, vacancies_info: str) -> None:
        """
        Добавление информации о вакансиях
        """

        with open(self.__file_path, 'a', encoding='utf-8') as file:
            file.write(vacancies_info + '\n')

    def remove_all_vacancies(self) -> None:
        """
        Очистить файл с информацией о вакансиях
        """

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write('')


class JSONSaver(BaseJSONSaver):
    def __init__(self, filename: str = 'vacancies.json'):
        self.__file_path = os.path.join(JSON_DIR, filename)
        self.__check_and_create()

    def __check_and_create(self) -> None:
        """
        Проверяет, существует ли файл, если нет создает его
        """

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('[]')

        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) == 0:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('[]')

    def write_vacancies_to_file(self, vacancies: list[dict]) -> None:
        """
        Принимает список словарей вакансий, записывает их в файл в формате JSON
        """

        vacancies_from_json = self.get_vacancies_from_file()
        tmp_vacancies = []
        for vacancy in vacancies:
            if vacancy not in vacancies_from_json:
                tmp_vacancies.append(vacancy)
        vacancies_from_json.extend(tmp_vacancies)
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies_from_json, file, ensure_ascii=False)

    def get_vacancies_from_file(self) -> list[dict]:
        """
        Возвращает список словарей с вакансиями
        """

        with open(self.__file_path, 'r') as file:
            vacancies = json.load(file)

        return vacancies

    def delete_vacancies_from_file(self) -> None:
        """
        Очищает файл JSON
        """

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write('[]')
