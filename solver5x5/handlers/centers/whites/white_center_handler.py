""" white center handler """
from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver5x5.handlers.centers.whites.white_middle_bar_handler import WhiteMiddleBarHandler


class WhiteCenterHandler:
    """ white center handler """

    def __init__(self):
        self.mover = Mover()
        self.middle_bar_handler = WhiteMiddleBarHandler()

    def handle(self, cube: Cube) -> Cube:
        cube = self._do_middle_bar(cube)
        cube = self._do_first_bar(cube)
        cube = self._do_second_bar(cube)
        return cube
    
    def _do_middle_bar(self, cube: Cube) -> Cube:
        return self.middle_bar_handler.handle(cube)

    def _do_first_bar(self, cube: Cube) -> Cube:
        # TODO: implement this
        return cube
    
    def _do_second_bar(self, cube: Cube) -> Cube:
        # TODO: implement this
        return cube
