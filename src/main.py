# import json
#
# import requests
# from abc import ABC, abstractmethod
#
# url_get = "https://api.hh.ru/vacancies" # используемый адрес для отправки запроса
#
# response = requests.get(url_get, headers={'User-Agent': 'HH-User-Agent'}, params={'text': 'Python', 'page': 19, 'per_page': 100}) # отправка GET-запроса
#
# print(response) # вывод объекта класса Response
#
#
# print(response.status_code) # вывод статуса запроса, 200 означает, что всё хорошо, остальные коды нас пока не интересуют и их можно считать показателем ошибки
#
#
# print(response.text) # печать ответа в виде текста того, что вернул нам внешний сервис
#
# print(response.json()) # печать ответа в виде json-объекта того, что нам вернул внешний сервис
# # Вывод:
#
# with open(f'{JSON_DIR}/information.json', 'w', encoding='utf-8') as file:
#     json.dump(vac, file, ensure_ascii=False)
from src.utils import user_interaction

if __name__ == '__main__':
    user_interaction()
