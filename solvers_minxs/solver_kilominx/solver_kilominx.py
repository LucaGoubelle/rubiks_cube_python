""" solver kilominx """
from pyminx.data.models.kilominx import Kilominx

from solvers_minxs.solver_kilominx.handlers.start_handler import StartHandler
from solvers_minxs.solver_kilominx.handlers.first_corners_handler import FirstCornersHandler
from solvers_minxs.solver_kilominx.handlers.middle_corners_handler import MiddleCornersHandler
from solvers_minxs.solver_kilominx.handlers.last_first_corners_handler import LastFirstCornersHandler
from solvers_minxs.solver_kilominx.handlers.last_corners_handler import LastCornersHandler


class SolverKilominx:
    """ solver kilominx """

    def __init__(self):
        self.start_handler = StartHandler()
        self.first_corners_handler = FirstCornersHandler()
        self.middle_corners_handler = MiddleCornersHandler()
        self.last_first_corners_handler = LastFirstCornersHandler()
        self.last_corners_handler = LastCornersHandler()

    def solve(self, minx: Kilominx) -> Kilominx:
        minx = self.start_handler.handle(minx)
        minx = self.first_corners_handler.handle(minx)
        minx = self.middle_corners_handler.handle(minx)
        minx = self.last_first_corners_handler.handle(minx)
        minx = self.last_corners_handler.handle(minx)
        return minx
