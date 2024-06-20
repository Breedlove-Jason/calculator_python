"""
pycalc_window.py

This module contains the UI components for the PyCalc application using PyQt.
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from pycalc_core import evaluate_expression, ERROR_MSG

# Constants
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    """
    PyCalcWindow is the main window for the PyCalc application.
    It sets up the calculator's display and buttons.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()

        # Set the central widget and layout
        central_widget = QWidget(self)
        central_widget.setLayout(self.generalLayout)
        self.setCentralWidget(central_widget)

        # Create display and buttons
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Create the display widget."""
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _create_buttons(self):
        """Create the buttons for the calculator."""
        self.buttons = {}
        buttons_layout = QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttons[key] = QPushButton(key)
                self.buttons[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttons_layout.addWidget(self.buttons[key], row, col)
        self.generalLayout.addLayout(buttons_layout)

    def set_display_text(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        """Get the display's text."""
        return self.display.text()

    def clear_display(self):
        """Clear the display."""
        self.set_display_text("")


def main():
    """Main function to run the PyCalc application."""
    pycalc_app = QApplication([])
    pycalc_window = PyCalcWindow()
    pycalc_window.show()
    from pycalc import (
        PyCalc,
    )  # Import moved inside main to avoid circular imports at module level

    PyCalc(model=evaluate_expression, view=pycalc_window)
    sys.exit(pycalc_app.exec())


if __name__ == "__main__":
    main()
