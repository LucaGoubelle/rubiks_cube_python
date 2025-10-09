""" handler base class """
from pyminx.moves.kilominx.kilominx_mover import KilominxMover

class Handler:
    """ handler base class """
    
    def __init__(self):
        self.mover = KilominxMover()
