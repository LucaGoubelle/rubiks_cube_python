""" start handler """
from typing import Dict

from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner


class StartHandler:
    """ Start handler """

    def __init__(self):
        self.mover = Mover()
        self.cube_scanner = Cube3x3Scanner()
    
    def start(self, cube: Cube) -> Cube:
        result1: str = self.cube_scanner.scan_center(cube, "up")
        result2: str = self.cube_scanner.scan_center(cube, "front")
        result: str = result1 + "_" + result2
        hmap: Dict[str,str] = {
            "yellow_blue": "",
            "yellow_green": "y2",
            "yellow_red": "y'",
            "yellow_orange": "y",
            
            "white_blue": "z2",
            "white_green": "x2",
            "white_red": "y z2",
            "white_orange": "y x2",
            
            "green_white": "x z2",
            "green_yellow": "x",
            "green_red": "z y'",
            "green_orange": "z' y",
            
            "blue_white": "x'",
            "blue_yellow": "x y2",
            "blue_red": "z' y'",
            "blue_orange": "z y",
            
            "red_white": "z x'",
            "red_yellow": "x y",
            "red_blue": "z",
            "red_green": "z x2",
            
            "orange_white": "x' y",
            "orange_yellow": "x y'",
            "orange_blue": "z'",
            "orange_green": "z y2",
        }
        return self.mover.multi_moves(cube, hmap[result]) if result in hmap else cube
