# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35


class PyCalcWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCal")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.generalLayout)
        self.setCentralWidget(central_widget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)


def main():
    pycalc_app = QApplication([])
    pycalc_window = PyCalcWindow()
    pycalc_window.show()
    sys.exit(pycalc_app.exec())


if __name__ == "__main__":
    main()
