""" PLL Scanner """
from pyrubik.data.cube import Cube

class PLLScanner:
    """ 
    PLL (Permutation Last Layer) Scanner 
    @author: LucaGoubelle
    """
    
    def __init__(self):
        self.hmap = {
            "blue": "B",
            "red": "R",
            "orange": "O",
            "green": "G",
        }
        
    def scan_PLL(self, cube: Cube) -> str:
        """
        scan the PLL config on the top face,
        return a string with chars colors
        ( B => blue, R => red, G => green, etc...)
        @author: LucaGoubelle
        """
        result: str = ""
        for elem in cube.front[0]:
            result += self.hmap[elem]
        result += "_"
        for elem in cube.right[0]:
            result += self.hmap[elem]
        result += "_"
        for elem in cube.back[0]:
            result += self.hmap[elem]
        result += "_"
        for elem in cube.left[0]:
            result += self.hmap[elem]
        return result
