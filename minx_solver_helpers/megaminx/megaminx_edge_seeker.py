""" megaminx edge seeker """
from typing import List
from minx_solver_helpers.megaminx.megaminx_scanner import MegaminxScanner
from pyminx.data.models.megaminx import Megaminx


class MegaminxEdgeSeeker:
    """ megaminx corner seeker """

    def __init__(self):
        self.scanner = MegaminxScanner()


    def seek_edge(self, minx: Megaminx, posibilities: List[str]) -> str:
        """
        seek a specific edge, return relatives informations
        @author: LucaGoubelle
        """
        targeted_orient: str = ""
        targeted_colors: str = ""
        edges: dict = self.scanner.scan_edges(minx)
        for k, v in edges.items():
            if v in posibilities:
                targeted_orient = k
                targeted_colors = v
                break
        return targeted_orient+"::"+targeted_colors
