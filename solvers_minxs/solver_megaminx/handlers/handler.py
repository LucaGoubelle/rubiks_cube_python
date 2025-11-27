""" handler base class """
from pyminx.moves.megaminx.megaminx_mover import MegaminxMover

class Handler:
    """ handler base class """
    
    def __init__(self):
        self.mover = MegaminxMover()
