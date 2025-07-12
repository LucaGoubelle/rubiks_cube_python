""" solver 7x7 """
from pyrubik.data.cube import Cube


class Solver7x7:
    """ solver 7x7 """
    
    def __init__(self):
        pass
    
    def solve(self, cube: Cube) -> Cube:
        cube = self._solveCenters(cube)
        # TODO: implement remaining lines
        return cube
