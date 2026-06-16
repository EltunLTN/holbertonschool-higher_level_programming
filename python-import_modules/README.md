# Python - Import Modules

This directory contains Python exercises on modules, imports, and command-line arguments from the Holberton Higher Level Programming curriculum.

## Learning Objectives

- Import functions and variables from other modules
- Use `sys.argv` to read command-line arguments
- Build simple calculators and utilities from imported code
- Understand module-level execution and `if __name__ == "__main__"`

## Files

- `0-add.py`: Imports `add(a, b)` from `add_0` and prints the sum of two CLI arguments
- `1-calculation.py`: Imports calculator functions and performs an operation from CLI args
- `2-args.py`: Prints the number of command-line arguments
- `3-infinite_add.py`: Sums all integer CLI arguments
- `5-variable_load.py`: Imports and prints a variable from another module
- `100-my_calculator.py`: Simple calculator using imported arithmetic functions
- `101-easy_print.py`: Prints a string without using `print` or `sys.stdout`
- `102-magic_calculation.py`: Performs a chained calculation using imported functions
- `103-fast_alphabet.py`: Prints the alphabet using `__import__` dynamically

## Support Files

- `add_0.py`: Defines `add(a, b)`
- `calculator_1.py`: Defines basic arithmetic functions
- `variable_load_5.py`: Defines a module-level variable
- `pythoniscool.py`: Module used for import demonstrations

## Requirements

- Python 3.x
- PEP 8 style (pycodestyle)
- Files should be executable where required

## Usage

Run scripts with command-line arguments:

```bash
python3 0-add.py 1 2
python3 1-calculation.py 10 + 5
python3 3-infinite_add.py 1 2 3 4
```
