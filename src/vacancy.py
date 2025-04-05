class Vacancy:
    """
    Класс для работы создания вакансий
    """

    vacancies_obj_list: list['Vacancy'] = []

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, currency: str,
                 requirements: str, city: str) -> None:
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirements = requirements
        self.city = city

    @classmethod
    def __validate_salary_and_currency(cls, vac_info: dict) -> tuple[int, int, str]:
        """
        Валидация зарплаты от, зарплаты до и валют
        """

        try:
            salary_from = vac_info['salary']['from']

            if not salary_from:
                salary_from = 0
        except (AttributeError, TypeError):
            salary_from = 0
        try:
            salary_to = vac_info['salary']['to']

            if not salary_to:
                salary_to = 0
        except (AttributeError, TypeError):
            salary_to = 0
        try:
            currency = f' {vac_info['salary']['currency']}'

            if not currency:
                currency = ''
        except (AttributeError, TypeError):
            currency = ''

        return salary_from, salary_to, currency

    @classmethod
    def __validate_requirements(cls, vac_info: dict) -> str:
        """
        Валидация требований
        """

        try:
            requirements = f' {vac_info['snippet']['requirement']}'

            if not requirements:
                requirements = 'Требования не указаны'
        except (AttributeError, TypeError):
            requirements = 'Требования не указаны'

        return requirements

    @classmethod
    def __validate_city(self, vac_info: dict) -> str:
        """
        Валидация города
        """

        try:
            city = str(vac_info['address']['city'])

            if not city:
                city = 'Город не указан'
        except (AttributeError, TypeError):
            city = 'Город не указан'

        return city

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[dict]) -> list['Vacancy']:
        """
        Создание списка экземпляров класса Vacancy из списка словарей с вакансиями
        """

        for vac_info in vacancies_data:
            name = vac_info['name']
            url = vac_info['alternate_url']
            salary_from, salary_to, currency = cls.__validate_salary_and_currency(vac_info)
            requirements = cls.__validate_requirements(vac_info)
            city = cls.__validate_city(vac_info)

            Vacancy.vacancies_obj_list.append(Vacancy(name, url, salary_from, salary_to, currency, requirements, city))

        return Vacancy.vacancies_obj_list

    @classmethod
    def add_vacancies(cls, vacancies: list[dict]) -> None:
        """
        Добавление экземпляров класса Vacancy из списка словарей вакансий
        """

        for vac_info in vacancies:
            name = vac_info['name']
            url = vac_info['alternate_url']
            salary_from, salary_to, currency = cls.__validate_salary_and_currency(vac_info)
            requirements = cls.__validate_requirements(vac_info)
            city = cls.__validate_city(vac_info)

            cls.vacancies_obj_list.append(Vacancy(name, url, salary_from, salary_to, currency, requirements, city))

    @classmethod
    def remove_vacancy(cls, vacancy: 'Vacancy') -> None:

        tmp_url_list = []

        for vac in cls.vacancies_obj_list:
            tmp_url_list.append(vac.url)

        if vacancy.url in tmp_url_list:
            index = tmp_url_list.index(vacancy.url)

            cls.vacancies_obj_list.pop(index)

    def __str__(self) -> str:
        if self.salary_from and self.salary_to:
            return (f'{self.name}, зарплата {self.salary_from}-{self.salary_to}{self.currency}, '
                    f'{self.city}, {self.url}'
                    f'{self.requirements}')
        elif self.salary_from and not self.salary_to:
            return f'{self.name}, зарплата от {self.salary_from}{self.currency}, {self.city}, {self.url}' \
                   f'{self.requirements}'
        elif not self.salary_from and self.salary_to:
            return f'{self.name}, зарплата до {self.salary_to}{self.currency}, {self.city}, {self.url}' \
                   f'{self.requirements}'
        else:
            return f'{self.name}, зарплата не указана, {self.city}, {self.url}'\
                   f'{self.requirements}'

    def __lt__(self, other: 'Vacancy') -> bool:
        if self.salary_from < other.salary_from:
            return True
        else:
            return False
