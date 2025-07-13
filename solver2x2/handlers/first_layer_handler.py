""" first layer handler """

from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver2x2.processors.first_face.wgr_processor import WGRProcessor
from solver_helpers.seekers.corner_2_seeker import Corner2Seeker

class FirstLayerHandler:
    """ first layer handler """

    def __init__(self):
        self.mover = Mover()
        self.wgr_proc = WGRProcessor()
        self.seeker = Corner2Seeker()
    
    def handle(self, cube: Cube) -> Cube:
        cube = FirstLayerHandler._insertWGR(cube)
        cube = FirstLayerHandler._insertWGO(cube)
        cube = FirstLayerHandler._insertWBO(cube)
        return cube

    def _insertWGR(self, cube: Cube) -> Cube:
        input_data: str = self.seeker.seek_corner(cube, [
            "white_green_red", "white_red_green",
            "green_white_red", "green_red_white",
            "red_white_green", "red_green_white"
        ])
        sequence: str = self.wgr_proc.process(input_data)
        cube = self.mover.multi_moves(cube, sequence)
        return cube
    
    
    def _insertWGO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertWBO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
