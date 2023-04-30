from PySide6.QtWidgets import QPushButton, QSizePolicy
from .objects.gui import Screen


class MainMenu(Screen):
    def __init__(self, index, name, main_window) -> None:
        super().__init__(index, name, main_window)
        self.button_config = {
            "Button 1": {"func": self.changeScreen, "img": "button12.gif"},
            "Button 2": {"func": self.printButtons, "img": "button9.gif"},
            "Button 3": {"func": self.printButtons, "img": "button5.gif"},
            "Button 4": {"func": self.printButtons, "img": "button4.gif"},
            "Button 5": {"func": self.changeScreen, "img": "button8.gif"},
            "Button 6": {"func": self.printButtons, "img": "button2.gif"},
            "Button 7": {"func": self.printButtons, "img": "button3.gif"},
            "Button 8": {"func": self.printButtons, "img": "button1.gif"},
            "Button 9": {"func": self.changeScreen, "img": "button6.gif"},
            "Button 10": {"func": self.printButtons, "img": "button11.gif"},
            "Button 11": {"func": self.printButtons, "img": "button4.gif"},
            "Button 12": {"func": self.printButtons, "img": "button7.gif"},
            "Button 13": {"func": self.changeScreen, "img": "button2.gif"},
            "Button 14": {"func": self.printButtons, "img": "button3.gif"},
            "Button 15": {"func": self.printButtons, "img": "button10.gif"},
            "Button 16": {"func": self.printButtons, "img": "button4.gif"},
        }
        self.initConfig()
        self.applyConfig()
        self.makeButtons()

    def printButtons(self):
        for button in self.buttons:
            print(f"Button: {button.name}, Gif: {button.gif.name}")
