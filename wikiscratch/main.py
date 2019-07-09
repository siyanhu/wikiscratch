import pandas as pd
import numpy as np

from urllib.request import urlopen
# from urllib.response import
from urllib.error import HTTPError

import re
from bs4 import BeautifulSoup
import sys

# reload(sys)
# sys.setdefaultencoding("utf8")


# for UnicodeEncodeError
def SaveFile(content, filename):
    f = open("wikiData/" + filename, "a")
    f.write(str(content) + "\n")
    f.close()


def SpideWiki(words):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        for i in range(len(words)):
            url = "https://en.wikipedia.org/wiki/" + words[i]
            response = urlopen(url)
            wikiHtml = response.read().decode('utf-8')
            html = BeautifulSoup(str(wikiHtml), "html.parser")
            div = html.find(name='div', id='mw-content-text')
            ps = div.find_all(name='li', limit=3, recursive=False)  # only direct children
            for p in ps:
                pText = p.get_text()
                SaveFile(pText, words[i])
            print(words[i], "process over...", "==" * 20)
            return html
    # except urllib.error
    except HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

words = ["Lists_of_universities_and_colleges_by_country"]
textStr = SpideWiki(words)
SaveFile(textStr, "test.txt")
