from src.vacancy import Vacancy


def test_vacancy_cast_to_object_list(vacancies_fixture):
    vacancies_obj_list = Vacancy.cast_to_object_list(vacancies_fixture)
    for vac in vacancies_obj_list:
        print(vac)
    assert str(vacancies_obj_list[0]) == ('PHP-разработчик / PHP (Symfony) developer, зарплата 250000-300000 RUR, '
                                          'Москва, https://hh.ru/vacancy/117788146\nпрофилирование и оптимизирования '
                                          'запросов. Опыт работы с RESTful API. Docker, GIT. Будет плюсом: хотя бы '
                                          'базовые знания JAVA, <highlighttext>Python</highlighttext>; понимание...')

    Vacancy.vacancies_obj_list.clear()


def test_vacancy_creation():
    test_vacancy = Vacancy('DevOps инженер',
            'https://hh.ru/vacancy/119079884',
            None,
            None,
            None,
            None,
            None)

    assert test_vacancy.name == 'DevOps инженер'
    assert test_vacancy.url == 'https://hh.ru/vacancy/119079884'
    assert test_vacancy.salary_from == 0
    assert test_vacancy.salary_to == 0
    assert test_vacancy.currency == ''
    assert test_vacancy.requirements == 'Требования не указаны'
    assert test_vacancy.city == 'Город не указан'

    Vacancy.vacancies_obj_list.clear()


def test_vacancy_comparison(vacancies_fixture):
    vacancies_obj_list = Vacancy.cast_to_object_list(vacancies_fixture)

    assert (vacancies_obj_list[0] > vacancies_obj_list[1]) == True
    assert (vacancies_obj_list[0] < vacancies_obj_list[1]) == False

    Vacancy.vacancies_obj_list.clear()


def test_add_vacancies(vacancies_fixture):
    vacancies_obj_list = Vacancy.cast_to_object_list(vacancies_fixture)

    assert len(Vacancy.vacancies_obj_list) == 77

    Vacancy.add_vacancies(vacancies_fixture)

    assert len(Vacancy.vacancies_obj_list) == 154

    Vacancy.vacancies_obj_list.clear()


def test_remove_vacancies(vacancies_fixture):
    vacancies_obj_list = Vacancy.cast_to_object_list(vacancies_fixture)

    vacancy_1 = vacancies_obj_list[0]
    vacancy_2 = vacancies_obj_list[1]

    Vacancy.remove_vacancy(vacancy_1)
    Vacancy.remove_vacancy(vacancy_2)

    assert len(Vacancy.vacancies_obj_list) == 75

    Vacancy.vacancies_obj_list.clear()