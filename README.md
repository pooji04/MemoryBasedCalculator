# Calculator with Combinational Circuits

This Python program implements a versatile calculator that leverages combinational circuits for arithmetic and logic operations. It provides support for a wide range of operations, including basic arithmetic operations (`+`, `-`, `*`, `/`), bitwise operations (`&`, `|`, `!`), exponentiation (`^`), and trigonometric/exponential functions (`sin`, `cos`, `tan`, `e`, `ln`).

## Usage

1. Run the Python script.
2. Enter the number of inputs (`input_num`) based on your operation:
   - For trigonometric/exponential functions, enter `1`.
   - For other operations, enter the number of operands.
3. Enter the operands or select previous answers using `'ans'`.
4. Choose the operation (`op`) based on the available options.
5. View the result.

## Combinational Circuits

The program utilizes various combinational circuit functions for basic arithmetic and logic operations:

- `ALU`: Arithmetic Logic Unit that performs addition and bitwise operations.
- `mux16`, `not16`, `and16`: Functions for 16-bit multiplexers, NOT gates, and AND gates.
- `or_gate`: Function for an OR gate.
- `or8way`: Function for an 8-way OR gate.
- `add16`: Function for adding two 16-bit binary numbers.

## Memory Register

The program maintains a memory register (`Register1`, `Register2`, `Register3`, `Register4`, `Register5`) to store the results of previous calculations.

## Trigonometric and Exponential Functions

For trigonometric and exponential functions, the program utilizes the `math` module to perform calculations.

## Continuous Operation

The program allows continuous operation, providing users with the option to enter more calculations. To exit, enter `'N'` when prompted.

## Explore and Experiment

Feel free to explore and use the calculator for various mathematical operations. If you encounter any issues or have suggestions for improvement, please let me know.
