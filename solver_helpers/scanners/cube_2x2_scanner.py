from typing import Dict
from pyrubik.data.cube import Cube


class Cube2x2Scanner:
    """ 
    cube 2x2 scanner 
    @author: LucaGoubelle
    """

    def scan_corner(self, cube: Cube, orient: str) -> str:
        """
        scan a corner on the cube,
        return colors based on 'orient' param
        @author: LucaGoubelle
        """
        last: int = len(cube.front) - 1
        hmap: Dict[str, str] = {
            "up_front_left": f"{cube.up[last][0]}_{cube.front[0][0]}_{cube.left[0][last]}",
            "up_front_right": f"{cube.up[last][last]}_{cube.front[0][last]}_{cube.right[0][0]}",
            "up_back_left": f"{cube.up[0][0]}_{cube.back[0][last]}_{cube.left[0][0]}",
            "up_back_right": f"{cube.up[0][last]}_{cube.back[0][0]}_{cube.right[0][last]}",

            "down_front_right": f"{cube.down[0][last]}_{cube.front[last][last]}_{cube.right[last][0]}",
            "down_front_left": f"{cube.down[0][0]}_{cube.front[last][0]}_{cube.left[last][last]}",
            "down_back_left": f"{cube.down[last][0]}_{cube.back[last][last]}_{cube.left[last][0]}",
            "down_back_right": f"{cube.down[last][last]}_{cube.back[last][0]}_{cube.right[last][last]}"
        }
        return hmap[orient] if orient in hmap else "???"


    def scan_corners(self, cube: Cube) -> Dict[str, str]:
        """
        scan all the corners info to a dictionary of
        orients <=> colors
        @author: LucaGoubelle
        """
        return {
            "up_front_left": self.scan_corner(cube, "up_front_left"),
            "up_front_right": self.scan_corner(cube, "up_front_right"),
            "up_back_left": self.scan_corner(cube, "up_back_left"),
            "up_back_right": self.scan_corner(cube, "up_back_right"),

            "down_front_right": self.scan_corner(cube, "down_front_right"),
            "down_front_left": self.scan_corner(cube, "down_front_left"),
            "down_back_left": self.scan_corner(cube, "down_back_left"),
            "down_back_right": self.scan_corner(cube, "down_back_right")
        }
