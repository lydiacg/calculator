# Calculator class 
#### Module 1, sprint 2

## Installation

## Calculator object

`Calculator(memory: float = 0)`

The calculator class is instantiated with 1 property, `_memory`. This is set to 0 by default but can set to any float. `_memory` should only be changed by class methods.

Requires math package

## Methods

### Add

`calculator.add(*numbers: float, overwrite_memory: bool = False)`

Adds any number of numbers together. Option to add to stored memory or overwrite memory with result.

If `overwrite_memory` flag is enabled, the memory will be overwritten with only the sum of the provided number(s), otherwise the provided number(s) will be added to the stored memory. 

If no numbers are provided, no calculation is preformed. If the `overwrite_memory` flag is enabled when no numbers are provided, the memory will be reset to 0.

### Subtract

`calculator.subtract(*numbers: float, overwrite_memory: bool = False)`

Subtracts provided number(s). Option to add to stored memory or overwrite memory with result - subtraction behaviour differs based on this flag.

If `overwrite_memory` flag is not enabled, all provided number(s) will be subtracted from the stored memory (including when 0). If no numbers are provided, no calculation will be preformed and the memory will not change.

If `overwrite_memory` flag is enabled, the memory will be overwritten with the first provided number and then all other numbers will be subtracted from this. If the `overwrite_memory` flag is enabled when no numbers are provided, the memory will be reset to 0 and no further calculations will be preformed. If only 1 number is provided when this flag is enabled, the memory will be overwritten with this number and no further calculations will be preformed.

### Multiply

`calculator.multiply(*numbers: float, overwrite_memory: bool = False)`

Multiplies any number of number(s) together. Option to add to stored memory or overwrite memory with result.

If `overwrite_memory` flag is enabled, the memory will be overwritten with only the product of the provided number(s). If only 1 number is provided, the memory will be reset with this number and no further calculations will be preformed. If the `overwrite_memory` flag is enabled when no numbers are provided, the memory will be reset to 0 and no further calculations will be preformed.

If `overwrite_memory` flag is not enabled, the stored memory will be multiplied by all numbers, staring from the first provided number, except if the stored memory is 0 - then the function will behave as though the `overwrite_memory` is enabled. If no numbers are provided, no calculation is preformed and the memory will remain the same. 

### Divide

`calculator.divide(*numbers: float, overwrite_memory: bool = False)`

Divides provided number(s). Option to add to stored memory or overwrite memory with result - divide behaviour differs based on this flag. 

If `overwrite_memory` flag is not enabled, the stored memory will be divided by all provided number(s), starting from the first number, except when the stored memory is 0. In this case, the function will behave as though the `overwrite_memory` flag is enabled. Otherwise, if no numbers are provided and `overwrite_memory` flag is not enabled, no calculation will be preformed and the memory will not change.

If `overwrite_memory` flag is enabled, the memory will be overwritten with the first provided number and then divided by all other numbers, starting with the second number. If the `overwrite_memory` flag is enabled when no numbers are provided, the memory will be reset to 0. If only 1 number is provided when this flag is enabled, the memory will be overwritten with this number and no further calculations will be preformed.

### Root

`calculator.root(x: float = None)`

Takes the root of either the provided number or the memory, if no number is provided. If a number is provided, the memory is overwritten with the result.

### Reset Memory

`calculator.reset_memory()`

Resets the stored memory to 0. 
