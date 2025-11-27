""" solver 3x3 """

from pyrubik.data.cube import Cube

from solvers_cubes.solver3x3.handlers.StartHandler import StartHandler
from solvers_cubes.solver3x3.handlers.WhiteCrossHandler import WhiteCrossHandler
from solvers_cubes.solver3x3.handlers.FirstLayerHandler import FirstLayerHandler
from solvers_cubes.solver3x3.handlers.SecondLayerHandler import SecondLayerHandler
from solvers_cubes.solver3x3.handlers.YellowCrossHandler import YellowCrossHandler
from solvers_cubes.solver3x3.handlers.LastCornersHandler import LastCornersHandler 

class Solver3x3:
    """ solver 3x3 """

    def __init__(self):
        self.start_handler = StartHandler()
        self.white_cross_handler = WhiteCrossHandler()
        self.first_layer_handler = FirstLayerHandler()
        self.second_layer_handler = SecondLayerHandler()
        self.yellow_cross_handler = YellowCrossHandler()
        self.last_corners_handler = LastCornersHandler()

    def solve(self, cube: Cube) -> Cube:
        """ solve 3x3 """
        cube = self.start_handler.start(cube)
        cube = self.white_cross_handler.handle(cube)
        cube = self.first_layer_handler.handle(cube)
        cube = self.second_layer_handler.handle(cube)
        cube = self.yellow_cross_handler.handle(cube)
        cube = self.last_corners_handler.handle(cube)
        return cube
