""" F2L scanner """
from pyrubik.data.cube import Cube

# notice: this only work for 3x3 cube only
class F2LScanner:
    """ F2L scanner """
    
    def scan_pair_left(self, cube: Cube) -> str:
        """ scan pair left """
        return f"{cube.up[2][1]}_{cube.front[0][1]}::{cube.up[2][2]}_{cube.front[0][2]}_{cube.right[0][0]}"
    
    def scan_pair_right(self, cube: Cube) -> str:
        """ scan pair right """
        return f"{cube.up[1][2]}_{cube.right[0][1]}::{cube.up[2][2]}_{cube.right[0][0]}_{cube.front[0][2]}"

    def scan_in(self, cube: Cube) -> str:
        """ scan in """
        return f"{cube.front[1][2]}_{cube.right[1][0]}::{cube.front[2][2]}_{cube.right[2][0]}_{cube.down[0][2]}"
    
    def scan_half_in(self, cube: Cube) -> str:
        """ scan half in """
        return f"{cube.front[1][2]}_{cube.right[1][0]}::{cube.front[0][2]}_{cube.right[0][0]}_{cube.up[2][2]}"
