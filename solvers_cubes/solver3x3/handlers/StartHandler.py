""" start handler """
from pyrubik.data.cube import Cube
from solvers_cubes.solver3x3.handlers.handler import Handler
from solvers_cubes.solver3x3.processors.start_processor import StartProcessor
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner

class StartHandler(Handler):
    """ Start handler """

    def __init__(self):
        super().__init__()
        self.cube_scanner = Cube3x3Scanner()
        self.proc = StartProcessor()
    
    def start(self, cube: Cube) -> Cube:
        result1: str = self.cube_scanner.scan_center(cube, "up")
        result2: str = self.cube_scanner.scan_center(cube, "front")
        result: str = result1 + "_" + result2
        return self.mover.multi_moves(cube, self.proc.process(result))
