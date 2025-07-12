""" corner 3 seeker """
from typing import List
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner


class Corner3Seeker:
    """ 
    seeker for corner on 2x2 
    """

    def __init__(self):
        self.scanner = Cube3x3Scanner()
    
    def seek_corner(self, cube: Cube, posibilities: List[str]) -> str:
        """
        seek a corner based on posibilities param, 
        return corner's infos
        @author: LucaGoubelle
        """
        targeted_orient: str = ""
        targeted_colors: str = ""
        corners: dict = self.scanner.scan_corners(cube)
        for k, v in corners.items():
            if v in posibilities:
                targeted_orient = k
                targeted_colors = v
                break
        return targeted_orient+"::"+targeted_colors
