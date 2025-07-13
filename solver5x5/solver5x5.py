""" solver 5x5 """
from pyrubik.data.cube import Cube

from solver5x5.handlers.centers.white_center_handler import WhiteCenterHandler
from solver5x5.handlers.centers.yellow_center_handler import YellowCenterHandler
from solver5x5.handlers.centers.blue_center_handler import BlueCenterHandler
from solver5x5.handlers.centers.red_center_handler import RedCenterHandler
from solver5x5.handlers.centers.last_centers_handler import LastCentersHandler


class Solver5x5:
    """ solver 5x5 """
    
    def __init__(self):
        self.white_center_handler = WhiteCenterHandler()
        self.yellow_center_handler = YellowCenterHandler()
        self.blue_center_handler = BlueCenterHandler()
        self.red_center_handler = RedCenterHandler()
        self.last_centers_handler = LastCentersHandler()

    def _solveCenters(self, cube: Cube) -> Cube:
        cube = self.white_center_handler.handle(cube)
        cube = self.yellow_center_handler.handle(cube)
        cube = self.blue_center_handler.handle(cube)
        cube = self.red_center_handler.handle(cube)
        cube = self.last_centers_handler.handle(cube)
        return cube
    
    def solve(self, cube: Cube) -> Cube:
        cube = self._solveCenters(cube)
        # implement remaining lines
        return cube
