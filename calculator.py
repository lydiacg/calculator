import math


class Calculator:
    def __init__(self, memory: float = 0):
        self._memory = memory

    def add(self, *numbers: float, overwrite_memory: bool = False):
        if overwrite_memory:
            self._memory = 0

        if len(numbers) > 0:
            self._memory = self._memory + sum(numbers)

    def multiply(self, *numbers: float, overwrite_memory: bool = False):
        if len(numbers) > 0:
            if overwrite_memory or self._memory == 0:
                self._memory = 1

            for number in numbers:
                self._memory *= number
        else:
            if overwrite_memory:
                self._memory = 0

    def subtract(self, *numbers: float, overwrite_memory: bool = False):
        if len(numbers) > 0:
            if overwrite_memory:
                self._memory = numbers[0]
                numbers.pop(0)

            self._memory = self._memory - sum(numbers)
        else:
            if overwrite_memory:
                self._memory = 0

    def divide(self, *numbers: float, overwrite_memory: bool = False):
        if len(numbers) > 0:
            if overwrite_memory:
                self._memory = numbers[0]
                numbers.pop(0)

            for number in numbers:
                self._memory /= number
        else:
            if overwrite_memory:
                self._memory = 0

    def root(self, x: float = None):
        if x is not None:
            self._memory = math.sqrt(x)
        else:
            self._memory = math.sqrt(self._memory)
        return self._memory

    def reset_memory(self):
        self._memory = 0

    @property
    def memory(self):
        return self._memory


def main():
    calculator = Calculator()


if __name__ == "__main__":
    main()
