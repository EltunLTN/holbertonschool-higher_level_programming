# Python - Inheritance

This directory contains Python exercises on object-oriented inheritance from the Holberton Higher Level Programming curriculum. Tasks cover type checking, class inheritance, method overriding, and custom subclasses of built-in types.

## Learning Objectives

- Inspect object attributes and class relationships
- Distinguish between exact type, subclass, and instance checks
- Build inheritance hierarchies with base and derived classes
- Override methods and extend built-in types (`list`, `int`)

## Files

- `0-lookup.py`: Defines `lookup(obj)` — returns all attributes and methods of an object
- `1-my_list.py`: Defines `MyList` class inheriting from `list` with a `print_sorted()` method
- `2-is_same_class.py`: Defines `is_same_class(obj, a_class)` — exact class match check
- `3-is_kind_of_class.py`: Defines `is_kind_of_class(obj, a_class)` — subclass-aware check
- `4-inherits_from.py`: Defines `inherits_from(obj, a_class)` — True only for subclasses, not exact match
- `5-base_geometry.py`: Defines empty `BaseGeometry` class
- `6-base_geometry.py`: Adds `area()` raising an exception (placeholder)
- `7-base_geometry.py`: Adds validated `integer_validator()` and `area()` methods
- `8-rectangle.py`: Defines `Rectangle` inheriting from `BaseGeometry`
- `9-rectangle.py`: Adds `size` property with validation to `Rectangle`
- `10-square.py`: Defines `Square` inheriting from `Rectangle`
- `11-square.py`: Adds `size` setter and `print()` method to `Square`
- `100-my_int.py`: Defines `MyInt` inheriting from `int` with custom `__eq__`
- `101-add_attribute.py`: Defines `add_attribute(obj, name, value)` — adds attribute if allowed

## Requirements

- Python 3.x
- PEP 8 style (pycodestyle)
- Files should be executable where required

## Usage

Run any script with:

```bash
python3 7-base_geometry.py
```

Import classes in the Python interpreter:

```python
from importlib import import_module
Rect = import_module('8-rectangle').Rectangle
r = Rect(width=3, height=4)
print(r.area())
```
