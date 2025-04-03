class Vacancy:
    vacancies_obj_list = []

    def __init__(self, name, url, salary, requirements, address):
        self.name = name
        self.url = url
        self.__validate_salary(salary)
        self.__validate_requirements(requirements)
        self.__validate_city(address)

    def __validate_salary(self, salary):
        if salary:
            self.currency = salary['currency']
            if salary['from']:
                self.salary_from = salary['from']
            else:
                self.salary_from = 0

            if salary['to']:
                self.salary_to = salary['to']
            else:
                self.salary_to = 0
        else:
            self.currency = ''
            self.salary_from = 0
            self.salary_to = 0

    def __validate_requirements(self, requirements):
        if requirements:
            self.requirements = requirements
        else:
            self.requirements = 'Требования не указаны'

    def __validate_city(self, address):
        if address:
            if address['city']:
                self.city = address['city']
            else:
                self.city = 'Город не указан'
        else:
            self.city = 'Город не указан'

    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        for vac_info in vacancies_data:
            name = vac_info['name']
            url = vac_info['alternate_url']
            salary = vac_info['salary']
            requirements = vac_info['snippet']['requirement']
            address = vac_info['address']

            Vacancy.vacancies_obj_list.append(Vacancy(name, url, salary, requirements, address))

        return Vacancy.vacancies_obj_list

    def __str__(self):
        return f'{self.name}, зарплата {self.salary_from} - {self.salary_to} {self.currency}, {self.city}, {self.url}'

    def __lt__(self, other):
        if self.salary_from < other.salary_from:
            return True
        else:
            return False
