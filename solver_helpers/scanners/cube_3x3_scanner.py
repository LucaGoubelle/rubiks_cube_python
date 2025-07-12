""" cube 3x3 scanner """
from typing import Dict
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_2x2_scanner import Cube2x2Scanner


class Cube3x3Scanner(Cube2x2Scanner):
    """ 
    cube 3x3 scanner
    @author: LucaGoubelle
    """

    def scan_center(self, cube: Cube, orient: str) -> str:
        """ 
        scan a center on the 3x3
        @author: LucaGoubelle
        """
        hmap: Dict[str, str] = {
            "back": cube.back[1][1],
            "up": cube.up[1][1],
            "front": cube.front[1][1],
            "left": cube.left[1][1],
            "right": cube.right[1][1],
            "down": cube.down[1][1]
        }
        return hmap[orient] if orient in hmap else "???"

    def scan_edge(self, cube: Cube, orient: str) -> str:
        """ 
        scan an edge on the 3x3 cube
        @author: LucaGoubelle
        """
        last: int = len(cube.front) - 1
        hmap: Dict[str, str] = {
            "up_front": f"{cube.up[last][1]}_{cube.front[0][1]}",
            "up_right": f"{cube.up[1][last]}_{cube.right[0][1]}",
            "up_left": f"{cube.up[1][0]}_{cube.left[0][1]}",
            "up_back": f"{cube.up[0][1]}_{cube.back[0][1]}",

            "front_left": f"{cube.front[1][0]}_{cube.left[1][last]}",
            "front_right": f"{cube.front[1][last]}_{cube.right[1][0]}",
            "back_left": f"{cube.back[1][last]}_{cube.left[1][0]}",
            "back_right": f"{cube.back[1][0]}_{cube.right[1][last]}",

            "down_front": f"{cube.down[0][1]}_{cube.front[last][1]}",
            "down_left": f"{cube.down[1][0]}_{cube.left[last][1]}",
            "down_right": f"{cube.down[1][last]}_{cube.right[last][1]}",
            "down_back": f"{cube.down[last][1]}_{cube.back[last][1]}"
        }
        return hmap[orient] if orient in hmap else "???"

    def scan_edges(self, cube: Cube) -> Dict[str, str]:
        """
        return a dictionary with all edges infos
        orients <=> colors
        @author: LucaGoubelle
        """
        return {
            "up_front": self.scan_edge(cube, "up_front"),
            "up_right": self.scan_edge(cube, "up_right"),
            "up_left": self.scan_edge(cube, "up_left"),
            "up_back": self.scan_edge(cube, "up_back"),

            "front_left": self.scan_edge(cube, "front_left"),
            "front_right": self.scan_edge(cube, "front_right"),
            "back_left": self.scan_edge(cube, "back_left"),
            "back_right": self.scan_edge(cube, "back_right"),

            "down_front": self.scan_edge(cube, "down_front"),
            "down_left": self.scan_edge(cube, "down_left"),
            "down_right": self.scan_edge(cube, "down_right"),
            "down_back": self.scan_edge(cube, "down_back")
        }
