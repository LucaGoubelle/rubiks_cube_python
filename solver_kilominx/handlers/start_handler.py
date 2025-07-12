""" start handler """
from pyminx.data.models.kilominx import Kilominx
from pyminx.moves.kilominx.kilominx_mover import KilominxMover
from minx_solver_helpers.kilominx.kilominx_scanner import KilominxScanner
from minx_solver_helpers.kilominx.kilominx_corner_seeker import KilominxCornerSeeker
from solver_kilominx.processors.first_corners.wbr_processor import WBRProcessor


class StartHandler:
    """ start handler """

    def __init__(self):
        self.scanner = KilominxScanner()
        self.mover = KilominxMover()
        self.seeker = KilominxCornerSeeker()
        self.processor = WBRProcessor()

    def handle(self, minx: Kilominx) -> Kilominx:
        """ handle start """
        data: str = self.scanner.scan_corner(minx, "down_downLeft_downRight")
        if data == "white_blue_red":
            return minx # nothing to do
        return self._start_first_corner(minx)


    def _start_first_corner(self, minx: Kilominx) -> Kilominx:
        """
        start with finding the first corner to put (white blue red)
        then grab it to the bottom place 
        @author: LucaGoubelle
        """
        posibilities: list = [
            "white_blue_red", "white_red°blue",
            "blue_red_white", "blue_white_red",
            "red_white_blue", "red_blue_white"
        ]
        corner_info: str = self.seeker.seek_corner(minx, posibilities)
        sequence: str = self.processor.process(corner_info)
        minx = self.mover.multi_moves(minx, sequence)
        return minx
