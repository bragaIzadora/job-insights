from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"

    result = count_ocurrences(path, word)

    assert isinstance(result, int), "O resultado deve ser um inteiro"

    result_upper = count_ocurrences(path, word.upper())
    assert result == result_upper, "A contagem de palavras deve ser insensível a maiúsculas e minúsculas"
