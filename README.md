# Calculator class 
#### Module 1, sprint 2

## Installation

From TestPyPi, install using pip

`pip install -i https://test.pypi.org/simple/ calculator-lydiacg`

Import the Calculator class

`from calculator_lydiacg.calculator import Calculator`

## Calculator object

`Calculator(memory: float = 0)`

The calculator class is instantiated with 1 property, `_memory`. This is set to 0 by default but can set to any float. `_memory` should only be changed by class methods.

Requires math package

## Methods

### Add

`calculator.add(*numbers: float, ans: bool = False)`

Addition. Any number of digits can be summed.

If only 1 number is input, it is always added to the memory. `ans` flag has no impact on behaviour with only 1 number.

If multiple numbers are input, by default the memory is overwritten with the sum of these numbers. If `ans` flag is set to `True`, all numbers will be added to the memory.

If no numbers are provided, the memory is not changed.

### Subtract

`calculator.subtract(*numbers: float, ans: bool = False)`

Subtraction. Any numbers of digits are subtracted.

If only 1 number is input, it is always subtracted from the memory. `ans` flag has no impact on behaviour with only 1 number.

If multiple numbers are input, by default the memory is overwritten by the first number minus the rest of the numbers. If `ans` flag is set to `True`, all numbers will be subtracted from the memory.

If no numbers are provided, the memory is not changed.

### Multiply

`calculator.multiply(*numbers: float, ans: bool = False)`

Multiplication. Any numbers of digits are multiplied together.

If only 1 number is input, memory is always multiplied by this numbers. `ans` flag has no impact on behaviour with only 1 number.

If multiple numbers are input, by default the memory is overwritten by the product of the numbers. If `ans` flag is set to `True`, the memory will be multiplied by all numbers.

If no numbers are provided, the memory is not changed.

### Divide

`calculator.divide(*numbers: float, ans: bool = False)`

Division. Any numbers of digits are divided by each other.

If only 1 number is input, memory is always divided by this numbers. `ans` flag has no impact on behaviour with only 1 number.

If multiple numbers are input, by default the memory is overwritten by the first number divided by the remaining numbers, starting from the second number. If `ans` flag is set to `True`, the memory will be divided by all numbers.

If no numbers are provided, the memory is not changed.

### Root

`calculator.root(x: float = None)`

Takes the root of either the provided number or the memory, if no number is provided. If a number is provided, the memory is overwritten with the result.

### Reset Memory

`calculator.reset_memory()`

Resets the stored memory to 0. 
