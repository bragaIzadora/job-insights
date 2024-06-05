from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [
            int(job['max_salary'])
            for job in self.jobs_list
            if job.get('max_salary') and job['max_salary'].isdigit()
        ]
        return max(salaries) if salaries else None

    def get_min_salary(self) -> int:
        salaries = [
            int(job['min_salary'])
            for job in self.jobs_list
            if job.get('min_salary') and job['min_salary'].isdigit()
        ]
        return min(salaries) if salaries else None

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if not all(key in job for key in ('min_salary', 'max_salary')):
            raise ValueError("Informações de salário ausentes no emprego")

        min_wage = self.str_to_int(job['min_salary'])
        max_wage = self.str_to_int(job['max_salary'])
        desired_salary = self.str_to_int(salary)

        if max_wage < min_wage:
            raise ValueError("Salário máximo é menor que o salário mínimo")

        return min_wage <= desired_salary <= max_wage

    def str_to_int(self, value: Union[int, str]) -> int:
        if isinstance(value, str) and value.isdigit():
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError("Valor não numérico fornecido")

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
