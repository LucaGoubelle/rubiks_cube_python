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
            "up_backleft_backright": f"{minx.up[0]}_{minx.back_left[0]}_{minx.back_right[1]}",

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

            "down_downLeft_downRight": f"{minx.down[0]}_{minx.down_left[2]}_{minx.down_right[3]}",
            "down_downLeft_absLeft": f"{minx.down[4]}_{minx.down_left[3]}_{minx.abs_left[2]}",
            "down_downRight_absRight": f"{minx.down[1]}_{minx.down_right[2]}_{minx.abs_right[3]}",
            "down_back_absLeft": f"{minx.down[3]}_{minx.back[2]}_{minx.abs_left[3]}",
            "down_back_absRight": f"{minx.down[2]}_{minx.back[3]}_{minx.abs_right[2]}"
        }
        return dico[orient] if orient in dico else "???"

    def scan_corners(self, minx: Kilominx) -> dict:
        return {
            "up_front_right": self.scan_corner(minx, "up_front_right"),
            "up_front_left": self.scan_corner(minx, "up_front_left"),
            "up_backleft_left": self.scan_corner(minx, "up_backleft_left"),
            "up_backright_right": self.scan_corner(minx, "up_backright_right"),
            "up_backleft_backright": self.scan_corner(minx, "up_backleft_backright"),

            "down_downLeft_downRight": self.scan_corner(minx, "down_downLeft_downRight"),
            "down_downLeft_absLeft": self.scan_corner(minx, "down_downLeft_absLeft"),
            "down_downRight_absRight": self.scan_corner(minx, "down_downRight_absRight"),
            "down_back_absLeft": self.scan_corner(minx, "down_back_absLeft"),
            "down_back_absRight": self.scan_corner(minx, "down_back_absRight")
        }
