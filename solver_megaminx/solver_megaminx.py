""" solver megaminx """
from pyminx.data.models.megaminx import Megaminx

from solver_megaminx.handlers.first_face.first_corners_handler import FirstCornersHandler
from solver_megaminx.handlers.first_face.start_handler import StartHandler
from solver_megaminx.handlers.first_face.white_star_handler import WhiteStarHandler

from solver_megaminx.handlers.last_face.grey_star_handler import GreyStarHandler
from solver_megaminx.handlers.last_face.last_corners_handler import LastCornersHandler

from solver_megaminx.handlers.last_first_layer_handler import LastFirstLayerHandler
from solver_megaminx.handlers.middle_corners_handler import MiddleCornersHandler
from solver_megaminx.handlers.prisms_handler import PrismsHandler
from solver_megaminx.handlers.second_layer_handler import SecondLayerHandler


class SolverMegaminx:
    """ solver megaminx """

    def __init__(self):
        self.start_handler = StartHandler()
        self.white_star_handler = WhiteStarHandler()
        self.first_corners_handler = FirstCornersHandler()

        self.second_layer_handler = SecondLayerHandler()
        self.prisms_handler = PrismsHandler()

        self.middle_corners_handler = MiddleCornersHandler()
        self.last_first_layer_handler = LastFirstLayerHandler()

        self.grey_star_handler = GreyStarHandler()
        self.last_corners_handler = LastCornersHandler()


    def solve(self, minx: Megaminx) -> Megaminx:
        """
        solve the megaminx, return altered megaminx
        @author LucaGoubelle
        """
        minx = self._solve_first_face(minx)
        minx = self._solve_second_step(minx)
        minx = self._solve_third_step(minx)
        minx = self._solve_last_face(minx)
        return minx

    
    def _solve_first_face(self, minx: Megaminx) -> Megaminx:
        minx = self.start_handler.handle(minx)
        minx = self.white_star_handler.handle(minx)
        minx = self.first_corners_handler.handle(minx)
        return minx

    
    def _solve_second_step(self, minx: Megaminx) -> Megaminx:
        minx = self.second_layer_handler.handle(minx)
        minx = self.prisms_handler.handle(minx)
        return minx

    
    def _solve_third_step(self, minx: Megaminx) -> Megaminx:
        minx = self.middle_corners_handler.handle(minx)
        minx = self.last_first_layer_handler.handle(minx)
        return minx

    
    def _solve_last_face(self, minx: Megaminx) -> Megaminx:
       minx = self.grey_star_handler.handle(minx)
       minx = self.last_corners_handler.handle(minx)
       return minx
