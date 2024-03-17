import pytest

list_data = [1, "2", 0.1]
dict_data = {"test": 1, "test2": "2"}


@pytest.fixture(scope="module")
def list_data_test():
    list_data = [1, "2", 0.1]
    return list_data


@pytest.fixture(scope="module")
def dict_data_test():
    dict_data = {"test": 1, "test2": "2"}
    return dict_data


@pytest.mark.parametrize("a, b, result", [
    (1, 3, True)
])
def test_float(a, b, result):
    assert isinstance(a / b, float) == result


def test_exception_float_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_exception_float_type():
    with pytest.raises(TypeError):
        1 / "0"


@pytest.mark.parametrize("list_data, result", [
    (list_data, True),
    (dict_data, False),

])
def test_list(list_data, result):
    assert isinstance(list_data, list) == result


def test_exception_list(list_data_test):
    with pytest.raises(IndexError):
        list_data_test[4]


@pytest.mark.parametrize("dict_data, result", [
    (dict_data, True),
    (list_data, False)
])
def test_dict(dict_data, result):
    assert isinstance(dict_data, dict) == result


def test_exception_dict(dict_data_test):
    with pytest.raises(LookupError):
        dict_data_test["qwe"]