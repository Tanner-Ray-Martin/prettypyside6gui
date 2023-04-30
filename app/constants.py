from os.path import abspath, basename, join
from json import load

FILE = abspath(__file__)

MAIN = FILE.replace(basename(FILE), "")

RESOURCES = join(MAIN, "resources")

CONFIGS = join(RESOURCES, "configs")
GUI_CONFIG_PATH = join(CONFIGS, "gui.json")
with open(GUI_CONFIG_PATH, "r") as fp:
    GUI_CONFIG = load(fp)

IMAGES = join(RESOURCES, "images")

GIF_CREATION_IMAGES = join(RESOURCES, "gif-creation-images")

VIDEOS = join(RESOURCES, "videos")


# Main Window - QMainWindow
MW_MIN_W = 200
MW_MIN_H = 200
# Main Menu - QWidget
MM_MIN_W = 200
MM_MIN_H = 200
MM_MAX_COLS = 3
