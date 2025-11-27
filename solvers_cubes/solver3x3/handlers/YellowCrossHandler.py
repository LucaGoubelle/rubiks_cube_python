""" yellow cross handler """

from pyrubik.data.cube import Cube
from solvers_cubes.solver3x3.handlers.handler import Handler

class YellowCrossHandler(Handler):
    """ yellow cross handler """
    
    def __init__(self):
        super().__init__()
    
    def _create(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def _correct(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def handle(self, cube: Cube) -> Cube:
        cube = self._create(cube)
        cube = self._correct(cube)
        return cube
