""" red center handler """
from pyrubik.data.cube import Cube
from solvers_cubes.solver5x5.handlers.handler import Handler


class RedCenterHandler(Handler):
    """ red center handler """
    
    def __init__(self):
        super().__init__()

    def handle(self, cube: Cube) -> Cube:
        #  implement this
        return cube
