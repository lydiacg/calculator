import math


class Calculator:
    def __init__(self, memory: float = 0):
        """
        Instantiates calculator object with provided memory

        :param memory: value to set memory to (0 if not provided)
        :type memory: float
        """
        self._memory = memory

    def add(self, *numbers: float, ans: bool = False):
        """
        Addition. If 1 number is provided, added to the memory. If multiple numbers
        are provided, sum overwrites memory, except when ans is True - then all numbers
        are added to memory.

        :param numbers: number(s) to sum
        :type numbers: float
        :param ans: if True add to memory, if False overwrite memory. Only applicable for multiple numbers
        :type ans: bool
        """
        if len(numbers) == 1:
            self._memory += numbers[0]
        elif len(numbers) > 1:
            if ans:
                self._memory += sum(numbers)
            else:
                self._memory = sum(numbers)

    def subtract(self, *numbers: float, ans: bool = False):
        """
        Subtraction. If 1 number is provided, subtracted from memory. If multiple numbers
        are provided, memory is overwritten with numbers[0] - sum(numbers[1:]), except when 
        ans is True - then all numbers are subtracted from memory.

        :param numbers: number(s) to subtract
        :type numbers: float
        :param ans: if True sub from memory, if False overwrite memory. Only applicable for multiple numbers
        :type ans: bool
        """
        if len(numbers) == 1:
            self._memory -= numbers[0]
        elif len(numbers) > 1:
            if ans:
                self._memory -= sum(numbers)
            else:
                self._memory = numbers[0] - sum(numbers[1:])

    def multiply(self, *numbers: float, ans: bool = False):
        """
        Multiplication. If 1 number is provided, memory is multiplied by it. If multiple numbers
        are provided, product overwrites memory, except when ans is True - then memory is multiplied
        by all numbers

        :param numbers: number(s) to multiply
        :type numbers: float
        :param ans: if True multiply memory, if False overwrite memory. Only applicable for multiple numbers
        :type ans: bool
        """
        if len(numbers) == 1:
            self._memory *= numbers[0]
        elif len(numbers) > 1:
            product = 1
            for number in numbers:
                product *= number
            if ans:
                self._memory *= product
            else:
                self._memory = product


    def divide(self, *numbers: float, ans: bool = False):
        """
        Division. If 1 number is provided, memory is divided by number. If multiple numbers
        are provided, memory is overwritten with numbers[0] / numbers[1] / numbers[2] ..., except when 
        ans is True - then memory is divided by all numbers

        :param numbers: number(s) to divide
        :type numbers: float
        :param ans: if True divide memory, if False overwrite memory. Only applicable for multiple numbers
        :type ans: bool
        """
        if len(numbers) == 1:
            self._memory /= numbers[0]
        elif len(numbers) > 1:
            for i, number in enumerate(numbers):
                if i == 0:
                    if ans:
                        self._memory /= number
                    else:
                        self._memory = number
                else:
                    self._memory /= number
                    

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
