import json
import os
from abc import ABC

from config import DATA_DIR, JSON_DIR


class BaseFileWorker(ABC):
    """ Абстрактный класс для FileWorker """

    def write_vacancies_to_file(self, vacancies):
        pass

    def read_vacancies_from_file(self):
        pass


class FileWorker(BaseFileWorker):
    def __init__(self, filename='vacancies.txt'):
        self.__file_path = os.path.join(DATA_DIR, filename)
        self.__check_and_create()

    def __check_and_create(self):
        """
        Проверяет, существует ли файл, если нет создает его
        """

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('')

    def write_vacancies_to_file(self, vacancies):
        """
        Принимает список экземпляров класса Vacancy и записывает информацию о них в файл
        """

        tmp_vacancies_info_list = []
        tmp_vacancies_info_str = '\n'.join(tmp_vacancies_info_list)

        for vac in vacancies:
            tmp_vacancies_info_list.append(str(vac))

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(tmp_vacancies_info_str)

    def read_vacancies_from_file(self):
        """
        Считывает информацию о вакансиях из файла
        """

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            vacancies_info = file.read()

        return vacancies_info

class JSONSaver:
    def __init__(self, filename='vacancies.json'):
        self.__file_path = os.path.join(JSON_DIR, filename)
        self.__check_and_create()

    def __check_and_create(self):
        """
        Проверяет, существует ли файл, если нет создает его
        """

        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('[]]')

    def write_vacancies_to_file(self, vacancies):
        """
        Принимает список словарей вакансий, записывает их в файл в формате JSON
        """

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)