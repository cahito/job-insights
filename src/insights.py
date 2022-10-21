from . import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    result = {job["job_type"] for job in all_jobs}

    return result


def filter_by_job_type(jobs, job_type):
    result = [job for job in jobs if job["job_type"] == job_type]

    return result


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    result = {job["industry"] for job in all_jobs if job["industry"] != ""}

    return result


def filter_by_industry(jobs, industry):
    result = [job for job in jobs if job["industry"] == industry]

    return result


def get_max_salary(path):
    all_jobs = jobs.read(path)
    temp = [
        job["max_salary"] for job in all_jobs if job["max_salary"].isdigit()
    ]
    result = max([int(max_sal) for max_sal in temp])

    return result


def get_min_salary(path):
    all_jobs = jobs.read(path)
    temp = [
        job["min_salary"] for job in all_jobs if job["min_salary"].isdigit()
    ]
    result = min([int(min_sal) for min_sal in temp])

    return result


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
