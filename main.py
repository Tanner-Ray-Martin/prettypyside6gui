from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app.screens import MainMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_Widget = QStackedWidget(self)
        self.stacked_Widget.addWidget(MainMenu(0, "Main Menu", self))
        self.setCentralWidget(self.stacked_Widget)
        self.stacked_Widget.show()


if __name__ == "__main__":
    app = QApplication()
    MW = MainWindow()
    MW.show()
    app.exec()
