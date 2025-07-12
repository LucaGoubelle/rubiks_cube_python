""" megaminx scanner """
from pyminx.data.models.megaminx import Megaminx


class MegaminxScanner:
    """ megaminx scanner """

    def scan_center(self, minx: Megaminx, orient: str) -> str:
        """ 
        scan a center of megaminx depending on 'orient' param
        @author: LucaGoubelle
        """
        dico: dict = {
            "up": minx.up[1][0],
            "front": minx.front[1][0],
            "right": minx.right[1][0],
            "left": minx.left[1][0],
            "down_left": minx.down_left[1][0],
            "down_right": minx.down_right[1][0],
            "abs_left": minx.abs_left[1][0],
            "abs_right": minx.abs_right[1][0],
            "back_left": minx.back_left[1][0],
            "back_right": minx.back_right[1][0],
            "back": minx.back[1][0],
            "down": minx.down[1][0]
        }
        return dico[orient] if orient in dico else "???"

    
    def scan_edge(self, minx: Megaminx, orient: str) -> str:
        """ 
        scan an edge of megaminx depending on 'orient' param
        @author: LucaGoubelle
        """
        dico: dict = {
            "up_front": minx.up[0][5]+"_"+minx.front[0][1],
            "up_right": f"{minx.up[0][3]}_{minx.right[0][1]}",
            "up_left": f"{minx.up[0][7]}_{minx.left[0][1]}",
            "up_backleft": f"{minx.up[0][9]}_{minx.back_left[0][1]}",
            "up_backright": f"{minx.up[0][1]}_{minx.back_right[0][1]}"
        }
        # todo: implement other dict case
        return dico[orient] if orient in dico else "???"

    
    def scan_corner(self, minx: Megaminx, orient: str) -> str:
        """ 
        scan a corner of megaminx depending on 'orient' param
        @author: LucaGoubelle
        """
        dico: dict = {
            "up_front_right": f"{minx.up[0][4]}_{minx.front[0][2]}_{minx.right[0][0]}",
            "up_front_left": f"{minx.up[0][6]}_{minx.front[0][0]}_{minx.left[0][2]}"
        }
        # todo: implement other dict case
        return dico[orient] if orient in dico else "???"

    
    def scan_edges(self, minx: Megaminx) -> dict:
        """ 
        scan all edges in megaminx, return a dict of orient => colors
        @author: LucaGoubelle
        """
        return {
            "up_front": self.scan_edge(minx, "up_front"),
            "up_right": self.scan_edge(minx, "up_right"),
            "up_left": self.scan_edge(minx, "up_left"),
            "up_backLeft": self.scan_edge(minx, "up_backLeft"),
            "up_backRight": self.scan_edge(minx, "up_backRight")
        }

    
    def scan_corners(self, minx: Megaminx) -> dict:
        """ 
        scan all corners in megaminx, return a dict of orient => colors
        @author: LucaGoubelle
        """
        return {
            "up_front_left": self.scan_corner(minx, "up_front_left"),
            "up_front_right": self.scan_corner(minx, "up_front_right")
        }
