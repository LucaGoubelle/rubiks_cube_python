from typing import List

class Cube:
    """ Rubik cube model """

    def __init__(self, 
        b: List[List[str]], 
        u: List[List[str]], 
        f: List[List[str]], 
        l: List[List[str]], 
        r: List[List[str]], 
        d: List[List[str]]
    ):
        self.back = b
        self.up = u
        self.front = f
        self.left = l
        self.right = r
        self.down = d
