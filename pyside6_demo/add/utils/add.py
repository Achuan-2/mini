from typing import Union


def add(a: Union[float, int],
        b: Union[float, int]) -> float:
    """
    计算两数之和 (取到小数点后两位)
    :param a: 第一个数
    :param b: 第二个数
    :return: 两数之和
    """
    return round(a + b, 2)


if __name__ == '__main__':
    print(add(1, 2))  # result: 3
