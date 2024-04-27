import math
import pathlib
import random
import sys


from typing import Tuple


import numpy as np
import numpy.random as nr
import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(0, str(proj_folder))


import main


@pytest.fixture
def expected_int() -> int:
    return random.randint(10, 90)


@pytest.fixture
def expected(expected_int:int) -> float:
    return expected_int * 0.01


@pytest.fixture
def bound() -> float:
    return random.randint(10, 90) + random.uniform(0.1, 0.9)


@pytest.fixture
def factor() -> int:
    return random.randint(2, 5)


@pytest.fixture
def data(bound:float, factor:int, expected_int:int) -> Tuple[float]:
    data_below = nr.uniform(0, int(bound), expected_int*factor)
    data_above = nr.uniform(int(bound)+1, bound * 2, (100 - expected_int)*factor)
    return tuple(np.concatenate((data_below, data_above)).tolist())


@pytest.fixture
def result(data, bound) -> float:
    return main.probability_below(data, bound)


def test_probabilty_below_type(result):
    assert isinstance(result, float), f"결과값의 변수형 {type(result)} 이 예상과 다름"


def test_probabilty_below_value(data:float, bound:float, expected:float, result:float):
    assert math.isclose(result, expected), (
        f"결과값 {result} 이 예상 {expected} 와 다름\n"
        f"x_data = {data}\n"
        f"bound = {bound}\n"
    )


if "__main__" == __name__:
    pytest.main([__file__])
