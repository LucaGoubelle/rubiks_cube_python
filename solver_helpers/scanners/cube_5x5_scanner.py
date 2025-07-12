""" cube 5x5 scanner """
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_4x4_scanner import Cube4x4Scanner

class Cube5x5Scanner(Cube4x4Scanner):
    """ 
    Cube 5x5 scanner 
    @author: LucaGoubelle
    """

    def scan_edge(self, cube: Cube, orient: str) -> str:
        """
        scan an edge on 5x5
        @author: LucaGoubelle
        """
        hmap: dict = {
            "up_front:left": "",
            "up_front:right": "",
            "up_front": "",
            "up_back:left": "",
            "up_back:right": "",
            "up_back": "",
            "up_right:front": "",
            "up_right:back": "",
            "up_right": "",
            "up_left:front": "",
            "up_left:back": "",
            "up_left": "",

            "front_left:up": "",
            "front_left:down": "",
            "front_left": "",
            "front_right:up": "",
            "front_right:down": "",
            "front_right": "",
            "back_left:up": "",
            "back_left:down": "",
            "back_left": "",
            "back_right:up": "",
            "back_right:down": "",
            "back_right": "",

            "down_front:left": "",
            "down_front:right": "",
            "down_front": "",
            "down_back:left": "",
            "down_back:right": "",
            "down_back": "",
            "down_right:front": "",
            "down_right:back": "",
            "down_right": "",
            "down_left:front": "",
            "down_left:back": "",
            "down_left": "",
        }
        return hmap[orient] if orient in hmap else "???"
