from typing import List
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_2x2_scanner import Cube2x2Scanner


class Corner2Seeker:
    """ seeker for corner on 2x2 """

    def __init__(self):
        self.cube_scanner = Cube2x2Scanner()
    
    def seek_corner(self, cube: Cube, posibilities: List[str]) -> str:
        targeted_orient: str = ""
        targeted_colors: str = ""
        corners: dict = self.cube_scanner.scan_corners(cube)
        for k, v in corners.items():
            if v in posibilities:
                targeted_orient = k
                targeted_colors = v
                break
        return targeted_orient+"::"+targeted_colors
