from threading import Thread, Event, Lock
from bot import Bot
from parser import Parser
import pandas as pd

class Server:
    """
    Running forever to satisfy the precious users
    """
    def __init__(self):
        self.parser = Parser()
        self.bot = Bot(token = )


if __name__ == '__main__':
    pass