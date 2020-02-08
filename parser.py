
import bs4
import pandas as pd

class Parser:
    """
    Parser should translate all the web info to .xlsx and pandas.DataFrame files
    a.  Parse the Categories, prices, discounts etc.
    b.  Every product must be documented inside the pandas.DataFrame and .xlsx
        product should contain the product name, category, price, discount, url to image
    """

    def __init__(self):
        self.main_url = 'https://www.kaufland.de/angebote/aktuelle-woche.html'