""" last corners handler """

from pyrubik.data.cube import Cube
from solver3x3.handlers.handler import Handler

class LastCornersHandler(Handler):
    """ last corners handler """
    
    def __init__(self):
        super().__init__()

    def _permute(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    def _orient(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    def handle(self, cube: Cube) -> Cube:
        cube = self._permute(cube)
        cube = self._orient(cube)
        return cube
