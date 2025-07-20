""" last layer handler """
from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover

from solver2x2.processors.last_face.oll_processor import OLLProcessor
from solver2x2.processors.last_face.pll_processor import PLLProcessor
from solver_helpers.advanced.oll_scanner import OLLScanner
from solver_helpers.advanced.pll_scanner import PLLScanner


class LastLayerHandler:
    """ last layer handler """
    
    def __init__(self):
        self.mover = Mover()
        self.oll_scanner = OLLScanner()
        self.pll_scanner = PLLScanner()
        self.oll_proc = OLLProcessor()
        self.pll_proc = PLLProcessor()

    
    def _oll(self, cube: Cube) -> Cube:
        input_config: str = self.oll_scanner.scanOLL(cube)
        sequence: str = self.oll_proc.process(input_config)
        cube = self.mover.multi_moves(cube, sequence)
        return cube
    
    
    def _pll(self, cube: Cube) -> Cube:
        input_config: str = self.pll_scanner.scan_PLL(cube)
        sequence: str = self.pll_proc.process(input_config)
        cube = self.mover.multi_moves(cube, sequence)
        return cube
    
    
    def _auf(self, cube: Cube) -> Cube:
        color: str = cube.front[0][0]
        colors_dict = {
            "green": "U2",
            "orange": "U",
            "red": "U'",
        }
        sequence: str = colors_dict[color] if color in colors_dict else "???"
        cube = self.mover.multi_moves(cube, sequence)
        return cube

    
    def handle(self, cube: Cube) -> Cube:
        cube = self._oll(cube)
        cube = self._pll(cube)
        cube = self._auf(cube)
        return cube
