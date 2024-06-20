"""
pycalc.py

This module contains the main application logic for PyCalc.
"""

from functools import partial
from pycalc_window import PyCalcWindow
from pycalc_core import evaluate_expression, ERROR_MSG


class PyCalc:
    """
    PyCalc is the main controller class that connects the model (evaluate_expression)
    with the view (PyCalcWindow).
    """

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connect_signals_and_slots()

    def _calculate_results(self):
        """Evaluate the current expression and display the result."""
        result = self._evaluate(expression=self._view.display_text())
        self._view.set_display_text(result)

    def _build_expression(self, sub_exp):
        """Build the expression by appending the pressed button's text."""
        if self._view.display_text() == ERROR_MSG:
            self._view.clear_display()
        expression = self._view.display_text() + sub_exp
        self._view.set_display_text(expression)

    def _connect_signals_and_slots(self):
        """Connect signals and slots."""
        for key_symbol, btn in self._view.buttons.items():
            if key_symbol not in {"=", "C"}:
                btn.clicked.connect(partial(self._build_expression, key_symbol))
        self._view.buttons["="].clicked.connect(self._calculate_results)
        self._view.buttons["C"].clicked.connect(self._view.clear_display)
        self._view.display.returnPressed.connect(self._calculate_results)
