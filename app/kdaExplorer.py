MAIN_URL = "https://backend-staging.euclabs.net/kadena-indexer/v1/"
STATS_ENDPOINT = "statistics"
STATS_TX_VOLUME_URL = "/".join(
    [MAIN_URL, STATS_ENDPOINT, "transaction-volume-sparkline"]
)
DATE_FORMAT = "%Y-%m-%d"

import requests
from datetime import datetime
from bs4 import BeautifulSoup


def getTXVolume():
    r = requests.get(STATS_TX_VOLUME_URL)
    response = r.json()
    vertical_axis = []
    horizontal_axis = []
    for i in response:
        date = i["date"]
        count = i["count"]
        date = datetime.strptime(date, DATE_FORMAT)
        vertical_axis.append(count)
        horizontal_axis.append(date)
    return vertical_axis, horizontal_axis


def getHtml():
    r = requests.get("https://kdaexplorer.com/")
    html = r.content.decode()
    html_lines = html.split("\n")
    for line in html_lines:
        if line.strip().startswith("<canvas "):
            print(line)


if __name__ == "__main__":
    getHtml()
