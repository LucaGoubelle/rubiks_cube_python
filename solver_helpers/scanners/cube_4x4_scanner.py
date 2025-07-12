""" cube 4x4 scanner """
from typing import Tuple
from pyrubik.data.cube import Cube
from solver_helpers.scanners.cube_3x3_scanner import Cube3x3Scanner


class Cube4x4Scanner(Cube3x3Scanner):
    """ 
    cube 4x4 scanner 
    @author: LucaGoubelle
    """

    
    def scan_center(self, cube: Cube, orient: str, coord: Tuple[int,int]) -> str:
        """ 
        scan a center on 4x4 cube and >
        @author: LucaGoubelle
        """
        hmap: dict = {
            "back": cube.back[coord[0]][coord[1]],
            "up": cube.up[coord[0]][coord[1]],
            "front": cube.front[coord[0]][coord[1]],
            "left": cube.left[coord[0]][coord[1]],
            "right": cube.right[coord[0]][coord[1]],
            "down": cube.down[coord[0]][coord[1]],
        }
        return hmap[orient] if orient in hmap else "???"
    

    def scan_edge(self, cube: Cube, orient: str) -> str:
        """ 
        scan an edge on 4x4 cube
        @author: LucaGoubelle
        """
        hmap: dict = {
            "up_front:left": cube.up[3][1]+"_"+cube.front[0][1],
            "up_front:right": cube.up[3][2]+"_"+cube.front[0][2],
            "up_back:left": "",
            "up_back:right": "",
            "up_left:front": cube.up[2][0]+"_"+cube.left[0][2],
            "up_left:back": cube.up[1][0]+"_"+cube.left[0][1],
            "up_right:front": cube.up[2][3]+"_"+cube.right[0][1],
            "up_right:back": cube.up[1][3]+"_"+cube.right[0][2],

            "front_left:up": cube.front[1][0]+"_"+cube.left[1][3],
            "front_left:down": cube.front[2][0]+"_"+cube.left[2][3],
            "front_right:up": cube.front[1][3]+"_"+cube.right[1][0],
            "front_right:down": cube.front[2][3]+"_"+cube.right[2][0],
            "back_left:up": "",
            "back_left:down": "",
            "back_right:up": "",
            "back_right:down": "",
            
            "down_front:left": cube.down[0][1]+"_"+cube.front[3][1],
            "down_front:right": cube.down[0][2]+"_"+cube.front[3][2],
            "down_back:left": "",
            "down_back:right": "",
            "down_left:front": cube.down[1][0]+"_"+cube.left[3][2],
            "down_left:back": cube.down[2][0]+"_"+cube.left[3][1],
            "down_right:front": cube.down[1][3]+"_"+cube.right[3][1],
            "down_right:back": cube.down[2][3]+"_"+cube.right[3][2],
        }
        return hmap[orient] if orient in hmap else "???"
