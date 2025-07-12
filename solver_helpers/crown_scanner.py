""" crown scanner """
from typing import List
from pyrubik.data.cube import Cube

Crown = List[List[str]]
Row = List[str]

class CrownScanner:
    """ crown scanner """
    
    
    def scan_crown(self, cube: Cube) -> Crown:
        """ 
        scan up crown of the cube, 
        return a crown (list of list of string)
        @author: LucaGoubelle
        """
        # to test
        crown: Crown = []
        crown.append(self._scan_back_of_Crown(cube))
        for i in range(len(cube.up)):
            crown.append(self._scan_up_of_Crown(cube, i))
        crown.append(self._scan_front_of_Crown(cube))
        return crown

    
    def _scan_back_of_Crown(self, cube: Cube) -> Row:
        """ scan back of crown """
        size: int = len(cube.up)
        row: list = []
        for i in range(size-1,-1,-1):
            row.append(cube.back[0][i])
        return row
    
    
    def _scan_front_of_Crown(self, cube: Cube) -> Row:
        size: int = len(cube.up)
        row: list = []
        for i in range(size):
            row.append(cube.front[0][i])
        return row
    
    
    def _scan_up_of_Crown(self, cube: Cube, index: int) -> Row:
        last: int = len(cube.up) -1
        row: list = []
        row.append(cube.left[0][index])
        for i in range(last+1):
            row.append(cube.up[index][i])
        row.append(cube.right[0][last-index])
        return row
