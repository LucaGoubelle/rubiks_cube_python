""" blue center handler """
from pyrubik.data.cube import Cube
from solver5x5.handlers.handler import Handler

class BlueCenterHandler(Handler):
    """ blue center handler """
    
    def __init__(self):
        super().__init__()

    def handle(self, cube: Cube) -> Cube:
        # implement this
        return cube
