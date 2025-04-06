import os
import tempfile
import unittest

from config import TESTS_DIR
from src.fileworker import FileWorker, JSONSaver
from src.vacancy import Vacancy
from tests.variables_for_tests import test_content, test_vacancies


class TestFileWriting(unittest.TestCase):
    def test_write_txt(self):
        Vacancy.vacancies_obj_list.clear()

        vacancies = Vacancy.cast_to_object_list(test_vacancies)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_filename = tmp.name

        try:
            txt_saver = FileWorker(tmp_filename)
            txt_saver.write_vacancies_to_file(vacancies)

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, test_content)
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

        try:
            FileWorker(tmp_filename)

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, '')
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

        try:
            txt_saver = FileWorker(tmp_filename)
            txt_saver.write_vacancies_to_file(vacancies)

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = txt_saver.read_vacancies_from_file()
                self.assertEqual(content, test_content)
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

        try:
            txt_saver = FileWorker(tmp_filename)
            txt_saver.add_vacancies('Повар, зарплата 60000 руб.')

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, 'Повар, зарплата 60000 руб.\n')
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

        try:
            txt_saver = FileWorker(tmp_filename)
            txt_saver.add_vacancies('Повар, зарплата 60000 руб.')
            txt_saver.remove_all_vacancies()

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, '')
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)
                Vacancy.vacancies_obj_list.clear()


class TestJSONWriting(unittest.TestCase):
    def test_write_json(self):
        Vacancy.vacancies_obj_list.clear()

        Vacancy.cast_to_object_list(test_vacancies)
        with open(os.path.join(TESTS_DIR, 'json_test.json'), 'r', encoding='utf-8') as file:
            test_json = file.read()

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_filename = tmp.name

        try:
            json_saver = JSONSaver(tmp_filename)
            json_saver.write_vacancies_to_file(test_vacancies)

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, test_json)
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)

        try:
            JSONSaver(tmp_filename)

            with open(tmp_filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertEqual(content, '[]')
        finally:
            if os.path.exists(tmp_filename):
                os.unlink(tmp_filename)
                Vacancy.vacancies_obj_list.clear()
