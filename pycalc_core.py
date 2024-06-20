"""
pycalc_core.py

This module contains core functions and constants for the PyCalc application.
"""

from sympy import sympify, SympifyError

# Constants
ERROR_MSG = "ERROR"


def evaluate_expression(expression):
    """
    Evaluate a mathematical expression using sympy.

    Parameters:
        expression (str): The mathematical expression to evaluate.

    Returns:
        str: The result of the evaluation or an error message if the expression is invalid.
    """
    try:
        result = str(sympify(expression))
    except SympifyError:
        result = ERROR_MSG
    return result
