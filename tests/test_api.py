from unittest.mock import patch, MagicMock

from src.api import HeadHunterAPI
from tests.conftest import vacancies_fixture


@patch('requests.get')
def test_get_vacancies(mock_get, vacancies_fixture):
    test_dict = {'items': vacancies_fixture}
    mock_get.return_value.json.return_value = test_dict
    mock_get.return_value.status_code = 200
    hh_api = HeadHunterAPI()
    hh_api._HeadHunterAPI__params['page'] = 19
    vacancies = hh_api.get_vacancies('Python')

    assert len(hh_api.vacancies) == 77
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies',
                                     headers={'User-Agent': 'HH-User-Agent'},
                                     params={'text': 'Python', 'page': 20, 'per_page': 100})


@patch('requests.get')
def test_get_vacancies_error(mock_get, vacancies_fixture):
    test_dict = {'items': vacancies_fixture}
    mock_get.return_value.json.return_value = test_dict
    mock_get.return_value.status_code = 404
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies('Python')

    assert len(hh_api.vacancies) == 0
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies',
                                     headers={'User-Agent': 'HH-User-Agent'},
                                     params={'text': 'Python', 'page': 0, 'per_page': 100})