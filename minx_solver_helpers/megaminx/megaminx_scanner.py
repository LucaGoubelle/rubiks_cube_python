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
            "up_backLeft": f"{minx.up[0][9]}_{minx.back_left[0][1]}",
            "up_backRight": f"{minx.up[0][1]}_{minx.back_right[0][1]}",

            "down_downLeft": f"{minx.down[0][9]}_{minx.down_left[0][5]}",
            "down_downRight": f"{minx.down[0][1]}_{minx.downRight[0][5]}",
            "down_absLeft": f"{minx.down[0][7]}_{minx.abs_left[0][5]}",
            "down_absRight": f"{minx.down[0][3]}_{minx.abs_right[0][5]}",
            "down_back": f"{minx.down[0][5]}_{minx.back[0][5]}"
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
            "up_front_left": f"{minx.up[0][6]}_{minx.front[0][0]}_{minx.left[0][2]}",
            "up_backLeft_left": f"{minx.up[0][8]}_{minx.back_left[0][2]}_{minx.left[0][0]}",
            "up_backRight_right": f"{minx.up[0][2]}_{minx.back_right[0][0]}_{minx.right[0][2]}",
            "up_backLeft_backRight": f"{minx.up[0][0]}_{minx.back_left[0][0]}_{minx.back_right[0][2]}",

            "front_downLeft_downRight": "???_???_???",
            "left_downLeft_absLeft": "???_???_???",
            "right_downRight_absRight": "???_???_???",
            "backLeft_back_absLeft": "???_???_???",
            "backRight_back_absRight": "???_???_???",

            "front_downLeft_left": "???_???_???",
            "front_downRight_right": "???_???_???",
            "backRight_absRight_right": "???_???_???",
            "backLeft_absLeft_left": "???_???_???",
            "back_backLeft_backRight": "???_???_???",

            "down_downLeft_downRight": "???_???_???",
            "down_downLeft_absLeft": "???_???_???",
            "down_downRight_absRight": "???_???_???",
            "down_back_absLeft": "???_???_???",
            "down_back_absRight": "???_???_???"
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
            "up_backRight": self.scan_edge(minx, "up_backRight"),

            "down_downLeft": self.scan_edge(minx, "down_downLeft"),
            "down_downRight": self.scan_edge(minx, "down_downRight"),
            "down_absLeft": self.scan_edge(minx, "down_absLeft"),
            "down_absRight": self.scan_edge(minx, "down_absRight"),
            "down_back": self.scan_edge(minx, "down_back")
        }

    
    def scan_corners(self, minx: Megaminx) -> dict:
        """ 
        scan all corners in megaminx, return a dict of orient => colors
        @author: LucaGoubelle
        """
        return {
            "up_front_left": self.scan_corner(minx, "up_front_left"),
            "up_front_right": self.scan_corner(minx, "up_front_right"),
            "up_backLeft_left": self.scan_corner(minx, "up_backLeft_left"),
            "up_backRight_right": self.scan_corner(minx, "up_backRight_right"),
            "up_backLeft_backRight": self.scan_corner(minx, "up_backLeft_backRight")
        }
