from PySide6.QtWidgets import (
    QPushButton,
    QSizePolicy,
    QWidget,
    QGridLayout,
    QLabel,
    QGraphicsWidget,
)
from PySide6.QtGui import QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from .objects.gui import Screen, Gif
from .constants import IMAGES
from .kdaExplorer import getTXVolume, getHtml
from os.path import join
from os import listdir
import sys
import matplotlib
from matplotlib import pyplot

matplotlib.use("Qt5Agg")


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=100, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor("#FF00F6")
        fig.set_edgecolor("#FF00F6")
        self.axes = fig.add_subplot(111)
        self.axes.set_facecolor("#000000")
        super(MplCanvas, self).__init__(fig)


class KDAWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setHtml(getHtml(), QUrl("https://kdaexplorer.com/"))
        # self.reload()
        self.show()


class KDAExplorer2(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_label = QLabel()
        self.main_label_background = QPixmap(join(IMAGES, "black-label.png"))
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_label.setPixmap(self.main_label_background)
        self.main_layout.addWidget(self.main_label)
        self.setLayout(self.main_layout)
        self.show()


class KDAExplorer(QWidget):
    def __init__(self):
        super().__init__()
        counts, dates = getTXVolume()
        self.sc = MplCanvas(self, width=10, height=5, dpi=100)
        self.main_layout = QGridLayout()
        self.sc.axes.plot(dates, counts)
        for line in self.sc.axes.get_lines():
            line.set_color("#FF00F6")
            line.set_linestyle("dashed")
        self.sc.axes.set_ylabel("<<< Qty >>>")
        self.sc.axes.set_xlabel("<<< Date >>>")
        self.main_layout.addWidget(self.sc, 0, 0, 10, 10)
        self.img_label = QLabel()
        self.img_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.img_map = Gif("kda-explorer.gif", self.img_label)
        self.main_layout.addWidget(self.img_label, 0, 0, 1, 1)
        self.setLayout(self.main_layout)
        self.show()


class GifViewer(Screen):
    def __init__(self, index, name, main_window) -> None:
        super().__init__(index, name, main_window)
        self.button_config = dict()
        for image_name in listdir(IMAGES):
            if image_name.endswith(".gif"):
                button_name = image_name.split(".")[0].title()
                self.button_config[button_name] = {
                    "func": self.showPopup,
                    "img": image_name,
                }

        self.initConfig()
        self.applyConfig()
        self.makeButtons()

    def printButtons(self):
        for button in self.buttons:
            print(f"Button: {button.name}, Gif: {button.gif.name}")
