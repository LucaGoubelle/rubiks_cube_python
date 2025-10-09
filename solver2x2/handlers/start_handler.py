""" start handler """

from pyrubik.data.cube import Cube

from solver_helpers.scanners.cube_2x2_scanner import Cube2x2Scanner
from solver_helpers.seekers.corner_2_seeker import Corner2Seeker

from solver2x2.processors.first_face.wbr_processor import WBRProcessor
from solver2x2.handlers.handler import Handler


class StartHandler(Handler):
    """ Start handler """

    def __init__(self):
        super().__init__()
        self.cube_scanner = Cube2x2Scanner()
        self.seeker = Corner2Seeker()
        self.wbr_proc = WBRProcessor()
    
    def handle(self, cube: Cube) -> Cube:
        """ start solve """
        preresult: str = self.cube_scanner.scan_corner(cube, "down_front_right")
        if preresult == "white_blue_red":
            return cube # nothing to do
        return self._handle_first_corner(cube)
    
    def _handle_first_corner(self, cube: Cube) -> Cube:
        """
        handle first corner
        """
        input_data: str = self.seeker.seek_corner(cube, [
            "white_blue_red","white_red_blue",
            "blue_white_red","blue_red_white",
            "red_white_blue","red_blue_white"
        ])
        sequence: str = self.wbr_proc.process(input_data)
        cube = self.mover.multi_moves(cube, sequence)
        return cube
