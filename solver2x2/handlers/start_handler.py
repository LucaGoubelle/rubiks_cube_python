""" start handler """

from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver_helpers.scanners.cube_2x2_scanner import Cube2x2Scanner


class StartHandler:
    """ Start handler """

    def __init__(self):
        self.cube_scanner = Cube2x2Scanner()

    
    def _analyse_up_front_right(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "up_front_right")
        hmap: dict = {
            "white_red_blue":"U' R2",
            "blue_white_red":"R'",
            "red_blue_white":"F"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_up_front_left(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "up_front_left")
        hmap: dict = {
            "white_blue_red":"F2",
            "red_white_blue":"U' F",
            "blue_red_white":"U' R'"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_up_back_right(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "up_back_right")
        hmap: dict = {
            "white_blue_red":"R2",
            "red_white_blue":"U F",
            "blue_red_white":"U R'"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_up_back_left(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "up_back_left")
        hmap: dict = {
            "white_red_blue":"U R2",
            "blue_white_red":"U2 R'",
            "red_blue_white":"U2 F"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_down_back_right(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "down_back_right")
        hmap: dict = {
            "white_red_blue": "D'",
            "blue_white_red": "R",
            "red_blue_white": "R2 F"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_down_back_left(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "down_back_left")
        hmap: dict = {
            "white_blue_red": "D2",
            "red_white_blue": "L' D",
            "blue_red_white": "L' F'"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube
    
    
    def _analyse_down_front_left(self, cube: Cube) -> Cube:
        result: str = self.cube_scanner.scan_corner(cube, "down_front_left")
        hmap: dict = {
            "white_red_blue": "D",
            "blue_white_red": "L D2",
            "red_blue_white": "F'"
        }
        mover = Mover()
        return mover.multi_moves(hmap[result]) if result in hmap else cube

    
    def _analyse_up(self, cube: Cube) -> Cube:
        """ analyse up layer """
        cube = StartHandler._analyse_up_front_right(cube)
        cube = StartHandler._analyse_up_front_left(cube)
        cube = StartHandler._analyse_up_back_left(cube)
        cube = StartHandler._analyse_up_back_right(cube)
        return cube
    
    
    def _analyse_down(self, cube: Cube) -> Cube:
        """ analyse down layer """
        cube = StartHandler._analyse_down_front_left(cube)
        cube = StartHandler._analyse_down_back_left(cube)
        cube = StartHandler._analyse_down_back_right(cube)
        return cube


    
    def start(self, cube: Cube) -> Cube:
        """ start solve """
        preresult: str = self.cube_scanner.scan_corner(cube, "down_front_right")
        hmap: dict = {
            "white_blue_red":"",
            "red_white_blue":"R' D'",
            "blue_red_white":"D R"
        }
        mover = Mover()
        if preresult in hmap:
            cube = mover.multi_moves(cube, hmap[preresult])
            return cube
        cube = StartHandler._analyse_up(cube)
        cube = StartHandler._analyse_down(cube)
        return cube
