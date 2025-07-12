""" edge 3 seeker """
from typing import List
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner


class Edge3Seeker:
    """ 
    seek edge on 3x3 
    """

    def __init__(self):
        self.scanner = Cube3x3Scanner()
    
    def seek_edge(self, cube: Cube, posibilities: List[str]) -> str:
        """
        seek an edge based on posibilities param, 
        return edge's infos
        @author: LucaGoubelle
        """
        targeted_orient: str = ""
        targeted_color: str = ""
        edges: dict = self.scanner.scan_edges(cube)
        for k, v in edges.items():
            if v in posibilities:
                targeted_orient = k
                targeted_color = v
                break
        return targeted_orient+"::"+targeted_color
