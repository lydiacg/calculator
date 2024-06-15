import math
from calculator_lydiacg.calculator import Calculator


def main():
    test_init()
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_root()


def test_init():
    # no memory set
    calculator_test_init_1 = Calculator()
    assert calculator_test_init_1._memory == 0

    # positive memory set
    calculator_test_init_2 = Calculator(100)
    assert calculator_test_init_2._memory == 100
    calculator_test_init_3 = Calculator(5)
    assert calculator_test_init_3._memory == 5

    # negative memory set
    calculator_test_init_4 = Calculator(-100)
    assert calculator_test_init_4._memory == -100
    calculator_test_init_5 = Calculator(-10)
    assert calculator_test_init_5._memory == -10

    # float memory set
    calculator_test_init_6 = Calculator(1.5)
    assert calculator_test_init_6._memory == 1.5


def test_add():
    # one input
    calculator_test_add_1 = Calculator()
    calculator_test_add_1.add(5)
    assert calculator_test_add_1._memory == 5

    # memory tracked
    calculator_test_add_1.add(10)
    assert calculator_test_add_1._memory == 15

    # mutliple inputs
    calculator_test_add_1.add(10, 5, 5, 10)
    assert calculator_test_add_1._memory == 30
    calculator_test_add_1.add(10, 5, ans = True)
    assert calculator_test_add_1._memory == 45

    # decimal input
    calculator_test_add_1.add(1.5)
    assert calculator_test_add_1._memory == 46.5

    # no input == no change
    calculator_test_add_1.add()
    assert calculator_test_add_1._memory == 46.5

    # negative inputs
    calculator_test_add_1.add(-6.5)
    assert calculator_test_add_1._memory == 40


def test_subtract():
    # one input
    calculator_test_subtract_1 = Calculator(10)
    calculator_test_subtract_1.subtract(5)
    assert calculator_test_subtract_1._memory == 5

    # memory tracked
    calculator_test_subtract_1.subtract(10)
    assert calculator_test_subtract_1._memory == -5

    # mutliple inputs
    calculator_test_subtract_1.subtract(10, 5, 5, 10)
    assert calculator_test_subtract_1._memory == -10
    calculator_test_subtract_1.subtract(10, 5, 10, ans = True)
    assert calculator_test_subtract_1._memory == -35

    # decimal input
    calculator_test_subtract_1.subtract(1.5)
    assert calculator_test_subtract_1._memory == -36.5

    # no input == no change
    calculator_test_subtract_1.subtract()
    assert calculator_test_subtract_1._memory == -36.5

    # negative inputs
    calculator_test_subtract_1.subtract(-6.5)
    assert calculator_test_subtract_1._memory == -30


def test_multiply():
    # one input
    calculator_test_multiply_1 = Calculator(10)
    calculator_test_multiply_1.multiply(5)
    assert calculator_test_multiply_1._memory == 50

    # memory tracked
    calculator_test_multiply_1.multiply(10)
    assert calculator_test_multiply_1._memory == 500

    # mutliple inputs
    calculator_test_multiply_1.multiply(6, 10)
    assert calculator_test_multiply_1._memory == 60
    calculator_test_multiply_1.multiply(10, 100, ans = True)
    assert calculator_test_multiply_1._memory == 60000

    # decimal input
    calculator_test_multiply_1.multiply(0.5)
    assert calculator_test_multiply_1._memory == 30000

    # no input == no change
    calculator_test_multiply_1.multiply()
    assert calculator_test_multiply_1._memory == 30000

    # negative inputs
    calculator_test_multiply_1.multiply(-1)
    assert calculator_test_multiply_1._memory == -30000


def test_divide():
    # one input
    calculator_test_divide_1 = Calculator(10)
    calculator_test_divide_1.divide(5)
    assert calculator_test_divide_1._memory == 2

    # memory tracked
    calculator_test_divide_1.divide(10)
    assert calculator_test_divide_1._memory == 0.2

    # mutliple inputs
    calculator_test_divide_1.divide(400,2)
    assert calculator_test_divide_1._memory == 200
    calculator_test_divide_1.divide(2, 5, 4, ans = True)
    assert calculator_test_divide_1._memory == 5

    # decimal input
    calculator_test_divide_1.divide(0.5)
    assert calculator_test_divide_1._memory == 10

    # no input == no change
    calculator_test_divide_1.divide()
    assert calculator_test_divide_1._memory == 10

    # negative inputs
    calculator_test_divide_1.divide(-1)
    assert calculator_test_divide_1._memory == -10


def test_root():
    # no input
    calculator_test_root_1 = Calculator(16)
    assert calculator_test_root_1.root() == 4

    # 1 input
    assert calculator_test_root_1.root(25) == 5


if __name__ == "__main__":
    main()
