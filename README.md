# Python Calculators :abacus:

## Overview
This repository is dedicated to various Python scripts that function as calculators for different purposes including grade calculation, population growth estimation, and retirement planning.

## Files Description
- `grade_calc.py`: Script for calculating grades.
- `grade_calc_exec.py`: Executable for the grade calculator.
- `pop_calc.py`: Population growth calculator script.
- `pop_calc_exec.py`: Executable for the population calculator.
- `retirement_calc.py`: Script to calculate retirement savings.
- `retirement_calc_exec.py`: Executable for the retirement calculator.

## Requirements
Python 3

## Usage
- Many of the Python Scripts contain small description of script and variables and functions.
- Any file with _exec are executor scripts used to excute the funtions of pair script

### Grade Calculator
Calculates student grades based on input scores.

```python
# Example usage from grade_calc.py
def calculate_grade(scores):
    return sum(scores) / len(scores)  # Simplified average calculation

#To Run
python grade_calc_exec.py
```

### Population Calculator
```python
# Snippet from pop_calc.py
def age_urban(file_name):
    import pandas as pd
    import matplotlib.pyplot as plt
    df_pop = pd.read_csv(file_name)

#To Run
python pop_calc_exec.py
```

### Retirement Calculator
```python
# Excerpt from retirement_calc.py
class Retirement:
    def __init__(self, initial_amount):
        self.balance = initial_amount
    def deposit(self, amount):
        self.balance += amount
        return self.balance
#To Run
python retirment_calc_exec.py
```

