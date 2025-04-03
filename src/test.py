# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.api import HeadHunterAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", {"from": None,
                                                                       "to": 5000,
                                                                       "currency": "USD",
                                                                       "gross": True},
                  "Требования: опыт работы от 3 лет...", {
      "city": "Саратов",
      "street": "проспект 50 лет Октября",
      "building": "108А",
      "lat": 51.569735,
      "lng": 45.992584,
      "description": None,
      "raw": "Саратов, проспект 50 лет Октября, 108А",
      "metro": None,
      "metro_stations": [],
      "id": "725410"
    })
for vac in sorted(vacancies_list, reverse=True):
    print(vac)
print(vacancy)