import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            self.jobs_list = [row for row in reader]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_type = job.get('job_type')
            if job_type:
                job_types.add(job_type)
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError(
                "O filtro fornecido para o método "
                "filter_by_multiple_criteria não é um dicionário."
            )
        return [
            job for job in jobs
            if all(job.get(key) == value for key, value
                   in filter_criteria.items())
        ]
