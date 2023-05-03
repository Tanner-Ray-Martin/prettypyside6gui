from typing import Optional
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QMovie, QIcon, QBitmap
from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QSizePolicy,
    QMainWindow,
    QLabel,
    QLayout,
)


from app import constants

from os.path import join

FAST_GIFS = ["black-pink-border.gif"]


class Gif(QMovie):
    def __init__(self, img_name, parent: QPushButton | QLabel):
        super().__init__(join(constants.IMAGES, img_name))
        self.name = img_name
        self.setObjectName(img_name)
        self.parent_object = parent

        self.frameChanged.connect(self.updateGif)

        self.start()

    def updateGif(self):
        parent_size = self.parent_object.size()
        parent_w, parent_h = parent_size.width(), parent_size.height()

        p_map = self.currentPixmap()

        new_p_map_size = (
            p_map.scaledToWidth(parent_w).size()
            if parent_w < parent_h
            else p_map.scaledToHeight(parent_h).size()
        )

        if isinstance(self.parent_object, Button):
            new_p_map_size.setWidth(new_p_map_size.width() - 20)
            new_p_map_size.setHeight(new_p_map_size.height() - 20)
            self.parent_object.setIcon(QIcon(p_map))
            self.parent_object.setIconSize(new_p_map_size)
        elif isinstance(self.parent_object, QLabel):
            self.parent_object.setPixmap(self.currentPixmap())


class Button(QPushButton):
    def __init__(self, img_path, parent, function, name):
        super().__init__()
        self.name = name
        self.setObjectName(name)
        self.image_name = img_path
        self.gif = Gif(img_path, self)
        self.setContentsMargins(20, 20, 20, 20)
        self.clicked.connect(function)
        self.setToolTip(f"Name: {name}\nGif: {img_path}")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        parent.buttons.append(self)


class Label(QLabel):
    def __init__(self, image_name, parent: QWidget, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window
        self.parent_object = parent
        self.image_name = image_name
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gif = Gif(image_name, self)
        monitor_size = self.main_window.monitor().size()
        mon_w = monitor_size.width()
        mon_h = monitor_size.height()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumHeight(mon_h)
        self.setMaximumWidth(mon_w)
        self.setMinimumHeight(100)
        self.setMinimumWidth(100)
        self.setMovie(self.gif)


class PopUpWindow(QWidget):
    def __init__(self, name, image_name, main_window: QMainWindow):
        super().__init__()
        self.name = name
        self.main_window = main_window
        self.image_name = image_name

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = Label(self.image_name, self, self.main_window)
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(
            self.label,
        )
        self.show()


class Screen(QWidget):
    def __init__(self, index, name, main_window) -> None:
        super().__init__()
        self.main_window = main_window
        self.index = index
        self.name = name
        self.setObjectName(name)
        self.buttons = []
        self.gifs = []
        self.movies = []
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

    def initConfig(self):
        self.config = constants.GUI_CONFIG[self.name]
        self.min_width = self.config["min_width"]
        self.min_height = self.config["min_height"]
        self.max_cols = self.config["max_columns"]
        self.max_rows = self.config["max_rows"]

    def applyConfig(self):
        self.main_window.setMinimumHeight(self.min_height)
        self.main_window.setMinimumWidth(self.min_width)
        change_size = False
        if self.main_window.width() > self.min_width:
            w = self.min_width
            change_size = True
        else:
            w = self.main_window.width()
        if self.main_window.height() > self.min_height:
            h = self.min_height
            change_size = True
        else:
            h = self.main_window.height()
        if change_size:
            size = QSize(w, h)
            self.main_window.resize(size)

    def makeButtons(self):
        col = 0
        row = 0
        for button_name, button_info in self.button_config.items():
            img_name = button_info["img"]
            func = button_info["func"]
            button = Button(img_name, self, func, button_name)
            if col > self.max_cols - 1:
                col = 0
                row += 1
            self.main_layout.addWidget(button, row, col)
            self.buttons.append(button)
            col += 1

    def changeScreen(self, evt):
        print(evt, self.objectName(), "need to add chaingScreenFunctionality")

    def showPopup(self, evt):
        for button in self.buttons:
            if button.underMouse():
                PopUpWindow(button.name, button.image_name, self.main_window)
                break
