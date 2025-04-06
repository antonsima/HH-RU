class Vacancy:
    """
    Класс для работы создания вакансий
    """

    __slots__ = ('name', 'url', 'salary_from', 'salary_to', 'currency', 'requirements', 'city')

    vacancies_obj_list: list['Vacancy'] = []

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, currency: str,
                 requirements: str, city: str) -> None:
        self.name = name
        self.url = url
        self.salary_from, self.salary_to, self.currency = self.__validate_salary_and_currency(salary_from, salary_to, currency)
        self.requirements = self.__validate_requirements(requirements)
        self.city = self.__validate_city(city)

        Vacancy.vacancies_obj_list.append(self)

    @classmethod
    def __validate_salary_and_currency(cls, salary_from: int, salary_to: int, currency: str) -> tuple[int, int, str]:
        """
        Валидация зарплаты от, зарплаты до и валют
        """

        if not salary_from:
            salary_from = 0

        if not salary_to:
            salary_to = 0

        if not currency:
            currency = ''
        else:
            currency = f' {currency}'

        return salary_from, salary_to, currency

    @classmethod
    def __validate_requirements(cls, requirements: str) -> str:
        """
        Валидация требований
        """

        if not requirements:
            requirements = 'Требования не указаны'

        return requirements

    @classmethod
    def __validate_city(self, city: str) -> str:
        """
        Валидация города
        """

        if not city:
            city = 'Город не указан'

        return city

    @classmethod
    def __attributes_from_dict(cls, vac_info: dict) -> tuple[int | None, int | None, str | None, str | None, str | None]:
        """
        Получение зарплаты, валюты, требований и города из словаря
        """

        try:
            salary_from = vac_info['salary']['from']
        except (KeyError, TypeError):
            salary_from = None

        try:
            salary_to = vac_info['salary']['to']
        except (KeyError, TypeError):
            salary_to = None

        try:
            currency = vac_info['salary']['currency']
        except (KeyError, TypeError):
            currency = None

        try:
            requirements = vac_info['snippet']['requirement']
        except (KeyError, TypeError):
            requirements = None

        try:
            city = vac_info['address']['city']
        except (KeyError, TypeError):
            city = None

        return salary_from, salary_to, currency, requirements, city

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[dict]) -> list['Vacancy']:
        """
        Создание списка экземпляров класса Vacancy из списка словарей с вакансиями
        """

        for vac_info in vacancies_data:
            name = vac_info['name']
            url = vac_info['alternate_url']
            salary_from, salary_to, currency, requirements, city = cls.__attributes_from_dict(vac_info)

            Vacancy(name, url, salary_from, salary_to, currency, requirements, city)

        return Vacancy.vacancies_obj_list

    @classmethod
    def add_vacancies(cls, vacancies: list[dict]) -> None:
        """
        Добавление экземпляров класса Vacancy из списка словарей вакансий
        """

        for vac_info in vacancies:
            name = vac_info['name']
            url = vac_info['alternate_url']
            salary_from, salary_to, currency, requirements, city = cls.__attributes_from_dict(vac_info)

            Vacancy(name, url, salary_from, salary_to, currency, requirements, city)

    @classmethod
    def remove_vacancy(cls, vacancy: 'Vacancy') -> None:
        """
        Принимается экземпляр класса Vacancy, который необходимо удалить из списка
        """

        tmp_url_list = []

        for vac in cls.vacancies_obj_list:
            tmp_url_list.append(vac.url)

        if vacancy.url in tmp_url_list:
            index = tmp_url_list.index(vacancy.url)

            cls.vacancies_obj_list.pop(index)

    def __str__(self) -> str:
        if self.salary_from and self.salary_to:
            return (f'{self.name}, зарплата {self.salary_from}-{self.salary_to}{self.currency}, '
                    f'{self.city}, {self.url}\n'
                    f'{self.requirements}')
        elif self.salary_from and not self.salary_to:
            return f'{self.name}, зарплата от {self.salary_from}{self.currency}, {self.city}, {self.url}\n' \
                   f'{self.requirements}'
        elif not self.salary_from and self.salary_to:
            return f'{self.name}, зарплата до {self.salary_to}{self.currency}, {self.city}, {self.url}\n' \
                   f'{self.requirements}'
        else:
            return f'{self.name}, зарплата не указана, {self.city}, {self.url}\n'\
                   f'{self.requirements}'

    def __lt__(self, other: 'Vacancy') -> bool:
        if self.salary_from < other.salary_from:
            return True
        else:
            return False
