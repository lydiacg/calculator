import math


class Calculator:
    def __init__(self, memory: float = 0):
        """
        Instantiates calculator object with provided memory

        :param memory: value to set memory to (0 if not provided)
        :type memory: float
        """
        self._memory = memory

    def add(self, *numbers: float, overwrite_memory: bool = False):
        """
        Adds all numbers to stored memory, or overwrites memory with sum of all numbers.

        :param numbers: number(s) to sum
        :type numbers: float
        :param overwrite_memory: flag to indicate if memory should be overwritten or not
        :type overwrite_memory: bool
        """
        if overwrite_memory:
            self._memory = 0

        if len(numbers) > 0:
            self._memory = self._memory + sum(numbers)

    def subtract(self, *numbers: float, overwrite_memory: bool = False):
        """
        Subtracts all numbers from stored memory, or overwrites memory with first number minus all other numbers.

        :param numbers: number(s) to subtract
        :type numbers: float
        :param overwrite_memory: flag to indicate if memory should be overwritten or not
        :type overwrite_memory: bool
        """
        num_list = list(numbers)
        if len(numbers) > 0:
            if overwrite_memory:
                self._memory = num_list[0]
                num_list.pop(0)

            self._memory = self._memory - sum(num_list)
        else:
            if overwrite_memory:
                self._memory = 0

    def multiply(self, *numbers: float, overwrite_memory: bool = False):
        """
        Multiplies stored memory by all numbers, or overwrites memory with product of all numbers.

        :param numbers: number(s) to multiply
        :type numbers: float
        :param overwrite_memory: flag to indicate if memory should be overwritten or not
        :type overwrite_memory: bool
        """
        if len(numbers) > 0:
            if overwrite_memory or self._memory == 0:
                self._memory = 1

            for number in numbers:
                self._memory *= number
        else:
            if overwrite_memory:
                self._memory = 0

    def divide(self, *numbers: float, overwrite_memory: bool = False):
        """
        Divides stored memory by all numbers, or overwrites memory with first number divided all other numbers.

        :param numbers: number(s) to divide
        :type numbers: float
        :param overwrite_memory: flag to indicate if memory should be overwritten or not
        :type overwrite_memory: bool
        """
        num_list = list(numbers)
        if len(numbers) > 0:
            if overwrite_memory or self._memory == 0:
                self._memory = num_list[0]
                num_list.pop(0)

            for number in num_list:
                self._memory /= number
        else:
            if overwrite_memory:
                self._memory = 0

    def root(self, x: float = None):
        """
        Takes the root of x, or memory if x is not provided.

        :param x: number to take root of (optional, memory is used if not provided)
        :type x: float
        """
        if x is not None:
            self._memory = math.sqrt(x)
        else:
            self._memory = math.sqrt(self._memory)
        return self._memory

    def reset_memory(self):
        """
        Sets memory property to 0
        """
        self._memory = 0

    @property
    def memory(self):
        return self._memory
