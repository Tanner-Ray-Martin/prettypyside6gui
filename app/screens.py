from PySide6.QtWidgets import QPushButton, QSizePolicy
from .objects.gui import Screen


class MainMenu(Screen):
    def __init__(self, index, name, main_window) -> None:
        super().__init__(index, name, main_window)
        self.button_config = {
            "Button 1": {"func": self.changeScreen, "img": "button1.gif"},
            "Button 2": {"func": self.printButtons, "img": "button2.gif"},
            "Button 3": {"func": self.printButtons, "img": "button3.gif"},
            "Button 4": {"func": self.printButtons, "img": "button4.gif"},
            "Button 5": {"func": self.changeScreen, "img": "button1.gif"},
            "Button 6": {"func": self.printButtons, "img": "button2.gif"},
            "Button 7": {"func": self.printButtons, "img": "button3.gif"},
            "Button 8": {"func": self.printButtons, "img": "button4.gif"},
        }
        self.initConfig()
        self.applyConfig()
        self.makeButtons()

    def printButtons(self):
        for button in self.buttons:
            print(f"Button: {button.name}, Gif: {button.gif.name}")
