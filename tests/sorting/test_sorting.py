from src.sorting import sort_by
import pytest


@pytest.fixture
def mocked_data():
    data = [
        {
            "title": "Back end developer",
            "min_salary": "500",
            "max_salary": "3000",
            "date_posted": "2020-05-11",
        },
        {
            "title": "Web developer",
            "min_salary": "",
            "max_salary": "1000",
            "date_posted": "2020-08-08",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
            "date_posted": "2020-06-10",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "invalid",
        }
    ]

    return [
        data,
        [data[0], data[2], data[1], data[3]],
        [data[3], data[0], data[1], data[2]],
        [data[0], data[2], data[3], data[1]],
        "date_posted",
        "max_salary",
        "min_salary",
    ]


def test_sort_by_criteria(mocked_data):
    mocked_jobs, mock_date, mock_max, mock_min, *criterias = mocked_data
    # sort_by(mocked_jobs, criterias[0])
    # assert mocked_jobs == mock_date
    sort_by(mocked_jobs, criterias[1])
    assert mocked_jobs == mock_max
    sort_by(mocked_jobs, criterias[2])
    assert mocked_jobs == mock_min
