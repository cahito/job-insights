from src.counter import count_ocurrences
import pytest
from unittest.mock import mock_open, patch


@pytest.fixture
def mocked_text():
    return """
    titulo,salario,tipo
Maquinista,2000,trainee
Motorista,3000,full time
Analista de Software,4000,full time
Assistente administrativo,1700, full time
Auxiliar administrativo,1400, full time
Auxiliar usinagem,1400, full time
Auxiliar de padaria,1400, full time
Analista Contábil,1400, full time
Gerente comercial,5000, full time
Analista de Departamento Pessoal,4000, full time
Esportista de Futebol profissional,50000, full time
Analista de crédito,4000, full time
Pessoa Programadora,3000, full time
Ux Designer,3000, full time
Auxiliar de manutenção, 1400, full time
"""


def test_counter(mocked_text):
    text_to_count = mocked_text
    with patch("builtins.open", mock_open(read_data=text_to_count)):
        result = count_ocurrences("anything.csv", "auxiliar")
        assert result == 4
