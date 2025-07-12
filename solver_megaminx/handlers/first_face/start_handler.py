""" start handler """
from pyminx.data.models.megaminx import Megaminx
from pyminx.moves.megaminx.megaminx_mover import MegaminxMover

from minx_solver_helpers.megaminx.megaminx_scanner import MegaminxScanner
from solver_megaminx.processors.center_orient_processor import CenterOrientProcessor

class StartHandler:
    """ start handler """

    
    def __init__(self):
        self.scanner = MegaminxScanner()
        self.processor = CenterOrientProcessor()
        self.mover = MegaminxMover()

    
    def handle(self, minx: Megaminx) -> Megaminx:
        """
        handle the first step, consisting in orienting 
        the puzzle in the good start position
        @author: LucaGoubelle
        """
        center_down: str = self.scanner.scan_center(minx, "down")
        center_down_left: str = self.scanner.scan_center(minx, "downLeft")
        center_down_right: str = self.scanner.scan_center(minx, "downRight")
        data: str = center_down + "_" + center_down_left + "_" + center_down_right
        if data == "white_blue_red":
            return minx # nothing to do
        return self._start_orienting(minx, data)

    
    def _start_orienting(self, minx: Megaminx, data: str) -> Megaminx:
        """
        start orienting depending on 'data' param
        @author: LucaGoubelle
        """
        sequence_moves: str = self.processor.process(data)
        minx = self.mover.multi_moves(minx, sequence_moves)
        return minx
