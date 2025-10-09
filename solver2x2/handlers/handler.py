""" handler mother class """
from pyrubik.moves.mover import Mover

class Handler:
    """ handler base class """
    def __init__(self):
        self.mover = Mover()
