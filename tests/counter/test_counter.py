from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"

    result = count_ocurrences(path, word)

    result_upper = count_ocurrences(path, word.upper())
    assert_msg = "A contagem de palavras deve ser insensível"
    assert result == result_upper, assert_msg
