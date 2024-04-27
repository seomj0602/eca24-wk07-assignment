from typing import List, Tuple, Union

Scalar = Union[int, float]
Vector = Union[List[Scalar], Tuple[Scalar]]


def probability_below(x_data:Vector, bound:float) -> float:

    # Implement your idea in this function
    # 자신의 생각을 이 함수에 구현하시오

    return None

# End of function. Please leave the followings unchanged
# 함수의 끝. 이 아래는 이대로 두시오


def main():
    data = (0, 1, 2, 3, 4)
    bound = 1.5
    print(probability_below(data, bound))


if "__main__" == __name__:
    main()
