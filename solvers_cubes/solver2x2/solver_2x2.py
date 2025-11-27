""" solver 2x2 """

from pyrubik.data.cube import Cube

from solvers_cubes.solver2x2.handlers.first_layer_handler import FirstLayerHandler
from solvers_cubes.solver2x2.handlers.last_layer_handler import LastLayerHandler
from solvers_cubes.solver2x2.handlers.start_handler import StartHandler


class Solver2x2:
    """ solver 2x2 """

    def __init__(self):
        self.start_handler = StartHandler()
        self.first_layer_handler = FirstLayerHandler()
        self.last_layer_handler = LastLayerHandler()

    def solve(self, cube: Cube) -> Cube:
        """ solve 2x2 """
        cube = self.start_handler.handle(cube)
        cube = self.first_layer_handler.handle(cube)
        cube = self.last_layer_handler.handle(cube)
        return cube
