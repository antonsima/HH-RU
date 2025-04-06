from src.utils import sort_vacancies, filter_vacancies_requirements, filter_vacancies_city, filter_vacancies_salary
from src.vacancy import Vacancy


def test_sort_vacancies(vacancies_fixture):
    vacancies_list = Vacancy.cast_to_object_list(vacancies_fixture)
    sorted_vacancies_list = sort_vacancies(vacancies_list)

    assert sorted_vacancies_list[0].salary_from == 500000
    assert sorted_vacancies_list[1].salary_from == 350000
    assert sorted_vacancies_list[2].salary_from == 250000
    assert sorted_vacancies_list[3].salary_from == 250000
    assert sorted_vacancies_list[4].salary_from == 245000
    assert sorted_vacancies_list[5].salary_from == 200000
    assert sorted_vacancies_list[6].salary_from == 150000
    assert sorted_vacancies_list[7].salary_from == 150000
    assert sorted_vacancies_list[8].salary_from == 150000
    assert sorted_vacancies_list[9].salary_from == 120000
    assert sorted_vacancies_list[10].salary_from == 120000

    Vacancy.vacancies_obj_list.clear()


def test_filter_vacancies(vacancies_fixture):
    vacancies_list = Vacancy.cast_to_object_list(vacancies_fixture)
    sorted_vacancies_list = sort_vacancies(vacancies_list)

    filtered_vacancies_by_words = filter_vacancies_requirements(sorted_vacancies_list, ['знание'])
    filtered_vacancies_by_city = filter_vacancies_city(filtered_vacancies_by_words, 'Москва')
    filtered_vacancies_by_salary = filter_vacancies_salary(filtered_vacancies_by_city, 50000)

    top_vacancies = filtered_vacancies_by_salary[0:5]

    assert top_vacancies[0].city == 'Москва'
    assert 'знание' in top_vacancies[0].requirements.lower()
    assert top_vacancies[0].salary_from == 245000

    assert top_vacancies[1].city == 'Москва'
    assert 'знание' in top_vacancies[1].requirements.lower()
    assert top_vacancies[1].salary_from == 100000

    assert top_vacancies[2].city == 'Москва'
    assert 'знание' in top_vacancies[2].requirements.lower()
    assert top_vacancies[2].salary_from == 100000

    assert top_vacancies[3].city == 'Москва'
    assert 'знание' in top_vacancies[3].requirements.lower()
    assert top_vacancies[3].salary_from == 50000

    Vacancy.vacancies_obj_list.clear()