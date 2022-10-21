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
    try:
        job["min_salary"] and job["max_salary"]
    except Exception:
        raise ValueError
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError
    result = job["min_salary"] <= salary <= job["max_salary"]

    return result


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass

    return result
