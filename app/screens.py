from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget
from .objects.gui import Screen, Gif
from .constants import IMAGES
from os.path import join
from os import listdir


class MainMenu(Screen):
    def __init__(self, index, name, main_window) -> None:
        super().__init__(index, name, main_window)
        self.button_config = {
            img_name: {"func": self.showPopup, "img": img_name}
            for img_name in listdir(IMAGES)
        }

        self.initConfig()
        self.applyConfig()
        self.makeButtons()

    def printButtons(self):
        for button in self.buttons:
            print(f"Button: {button.name}, Gif: {button.gif.name}")
