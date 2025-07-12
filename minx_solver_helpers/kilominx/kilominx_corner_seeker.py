""" kilominx corner seeker """
from typing import List
from minx_solver_helpers.kilominx.kilominx_scanner import KilominxScanner
from pyminx.data.models.kilominx import Kilominx


class KilominxCornerSeeker:
    """ kilominx corner seeker """

    
    def __init__(self):
        self.scanner = KilominxScanner()

    
    def seek_corner(self, minx: Kilominx, posibilities: List[str]) -> str:
        """
        seek a specific corner, return relatives informations
        @author: LucaGoubelle
        """
        targeted_orient: str = ""
        targeted_colors: str = ""
        corners: dict = self.scanner.scan_corners(minx)
        for k, v in corners.items():
            if v in posibilities:
                targeted_orient = k
                targeted_colors = v
                break
        return targeted_orient+"::"+targeted_colors
