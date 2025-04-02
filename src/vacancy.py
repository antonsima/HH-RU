class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, requirements):
        self.salary_from = self.__validate_salary(salary_from)

    def __validate_salary(self, salary_from):
        pass

    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        vacancies_list = []

        for vac_info in vacancies_data:
            name = vac_info['name']
            salary = vac_info['salary']

            if salary:
                salary_from = salary['from'] if salary['from'] else 0
                salary_to = salary['to'] if salary['to'] else 0
            else:
                salary_from = 0
                salary_to = 0

            url = vac_info['alternate_url']

    def __str__(self):
        return f'{self.name}, зарплата {self.salary_from}, {self.city}, {self.url}'

    def __lt__(self):
        pass
