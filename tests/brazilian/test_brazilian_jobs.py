from src.brazilian_jobs import read_brazilian_file
import pytest
from unittest.mock import patch


@pytest.fixture
def mocked_dict():
    return [
        [
            {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"},
            {"titulo": "Motorista", "salario": "3000", "tipo": "full time"},
        ],
        [
            {"title": "Maquinista", "salary": "2000", "type": "trainee"},
            {"title": "Motorista", "salary": "3000", "type": "full time"},
        ],
    ]


def test_brazilian_jobs(mocked_dict):
    dict_to_translate, translated_dict = mocked_dict
    with patch("src.jobs.read", return_value=dict_to_translate):
        result = read_brazilian_file("src/anything.csv")
        assert result == translated_dict
