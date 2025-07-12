""" solver 6x6 """
from pyrubik.data.cube import Cube


class Solver6x6:
    """ solver 6x6 """
    
    def __init__(self):
        pass
    
    def solve(self, cube: Cube) -> Cube:
        cube = self._solveCenters(cube)
        # TODO: implement remaining lines
        return cube
