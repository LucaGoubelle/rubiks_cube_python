""" white cross handler """

from pyrubik.data.cube import Cube
from solver3x3.handlers.handler import Handler
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner

class WhiteCrossHandler(Handler):
    """ white cross handler """

    def __init__(self):
        super().__init__()
        self.cube_scanner = Cube3x3Scanner()
    
    
    def _seek_edge(self, cube: Cube, colors1: str, colors2: str) -> str:
        """ get the piece orientation """
        targeted_orient: str = ""
        edges: dict = self.cube_scanner.scan_edges(cube)
        for k, v in edges.items():
            if v==colors1 or v==colors2:
                targeted_orient = k
                break
        return targeted_orient
    
    
    def _processWB(self, cube: Cube, targeted_orient: str) -> Cube:
        """ enum moves case for orientations """
        hmap: dict = {}
        
        hmap["up_front"] = "F2"
        hmap["up_left"] = "U' F2"
        hmap["up_right"] = "U F2"
        hmap["up_back"] = "U2 F2"
            
        hmap["down_front"] = ""
        hmap["down_left"] = "D"
        hmap["down_right"] = "D'"
        hmap["down_back"] = "D2"

        hmap["front_left"] = "F'"
        hmap["front_right"] = "F"
        hmap["back_left"] = "L2 F'"
        hmap["back_right"] = "R2 F"
        
        return self.mover.multi_moves(cube, hmap[targeted_orient]) if targeted_orient in hmap else cube

    
    def _insertWB(self, cube: Cube) -> Cube:
        targeted_orient: str = self._seek_edge(cube, "white_blue", "blue_white")
        cube = self._processWB(cube, targeted_orient)
        # verify orientation in slot
        final_verif: str = self.cube_scanner.scan_edge(cube, "down_front")
        # correct the orientation
        cube = self.mover.multi_moves(cube, "F2 U' R' F") if final_verif=="blue_white" else cube
        return cube
    
    
    def _processWR(self, cube: Cube, targeted_orient: str) -> Cube:
        """ enum moves case for orientations """
        hmap: dict = {}

        hmap["up_front"] = "U' R2"
        hmap["up_left"] = "U2 R2"
        hmap["up_right"] = "R2"
        hmap["up_back"] = "U R2"
        
        hmap["down_left"] = "L2 U2 R2"
        hmap["down_right"] = ""
        hmap["down_back"] = "D' R D R'"

        hmap["front_left"] = "F2 R' F2"
        hmap["front_right"] = "R'"
        hmap["back_left"] = "L U2 R2"
        hmap["back_right"] = "R"

        # do the moves for inserting the piece
        return self.mover.multi_moves(cube, hmap[targeted_orient]) if targeted_orient in hmap else cube
    
    
    def _insertWR(self, cube: Cube) -> Cube:
        targeted_orient: str = self._seek_edge(cube, "white_red", "red_white")
        cube = self._processWR(cube, targeted_orient)
        # verify orientation in slot
        final_verif: str = self.cube_scanner.scan_edge(cube, "down_right")
        # correct the orientation
        cube = self.mover.multi_moves(cube, "D' F' D R'") if final_verif=="red_white" else cube
        return cube
    
    
    def _processWG(self, cube: Cube, targeted_orient: str) -> Cube:
        """ enum moves case for orientations """
        hmap: dict = {}

        hmap["up_front"] = "D2 F2 D2"
        hmap["up_left"] = "D L2 D'"
        hmap["up_right"] = "D' R2 D"
        hmap["up_back"] = "y R2 y'"
        
        hmap["down_left"] = "L D L' D'"
        hmap["down_back"] = ""
        
        hmap["front_left"] = "D L D'"
        hmap["front_right"] = "D' R' D"
        hmap["back_left"] = "y' L y"
        hmap["back_right"] = "y R' y'"

        # do the moves for inserting the piece
        return self.mover.multi_moves(cube, hmap[targeted_orient]) if targeted_orient in hmap else cube
    
    
    def _insertWG(self, cube: Cube) -> Cube:
        targeted_orient: str = self._seek_edge(cube, "white_green", "green_white")
        cube = self._processWG(cube, targeted_orient)
        # verify orientation in slot
        final_verif: str = self.cube_scanner.scan_edge(cube, "down_back")
        # correct the orientation
        cube = self.mover.multi_moves(cube, "y R D' F D y'") if final_verif=="green_white" else cube
        return cube
    
    
    def _processWO(self, cube: Cube, targeted_orient: str) -> Cube:
        """ enum moves case for orientations """
        hmap: dict = {}

        hmap["up_front"] = "U L2"
        hmap["up_left"] = "L2"
        hmap["up_right"] = "U2 L2"
        hmap["up_back"] = "U' L2"

        hmap["down_left"] = ""
        
        hmap["front_left"] = "L"
        hmap["front_right"] = "F2 L F2"
        hmap["back_left"] = "L'"
        hmap["back_right"] = "D2 R D2"

        # do the moves for inserting the piece
        return self.mover.multi_moves(cube, hmap[targeted_orient]) if targeted_orient in hmap else cube
    
    
    def _insertWO(self, cube: Cube) -> Cube:
        targeted_orient: str = self._seek_edge(cube, "white_orange", "orange_white")
        cube = self._processWO(cube, targeted_orient)
        # verify orientation in slot
        final_Verif: str = self.cube_scanner.scan_edge(cube, "down_left")
        # correct the orientation
        cube = self.mover.multi_moves(cube, "L2 D L F' L' D'") if final_Verif=="orange_white" else cube
        return cube

    def handle(self, cube: Cube) -> Cube:
        cube = self._insertWB(cube)
        cube = self._insertWR(cube)
        cube = self._insertWG(cube)
        cube = self._insertWO(cube)
        return cube
