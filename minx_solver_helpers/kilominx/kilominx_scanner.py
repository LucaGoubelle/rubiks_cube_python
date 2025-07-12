""" kilominx scanner """
from pyminx.data.models.kilominx import Kilominx


class KilominxScanner:
    """ kilominx scanner """

    def scan_corner(self, minx: Kilominx, orient: str) -> Kilominx:
        dico: dict = {
            "up_front_right": f"{minx.up[2]}_{minx.front[1]}_{minx.right[0]}",
            "up_front_left": f"{minx.up[3]}_{minx.front[0]}_{minx.left[1]}",
            "up_backleft_left": f"{minx.up[4]}_{minx.back_left[1]}_{minx.left[0]}",
            "up_backright_right": f"{minx.up[1]}_{minx.back_right[0]}_{minx.right[1]}",
            "up_backleft_backright": f"{minx.up[0]}_{minx.back_left[0]}_{minx.back_right[1]}"
        }
        return dico[orient] if orient in dico else "???"

    def scan_corners(self, minx: Kilominx) -> dict:
        return {
            "up_front_right": self.scan_corner(minx, "up_front_right"),
            "up_front_left": self.scan_corner(minx, "up_front_left"),
            "up_backleft_left": self.scan_corner(minx, "up_backleft_left"),
            "up_backright_right": self.scan_corner(minx, "up_backright_right"),
            "up_backleft_backright": self.scan_corner(minx, "up_backleft_backright")
        }
