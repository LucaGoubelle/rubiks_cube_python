from typing import List

Face = List[List[str]]

class Cube:
    """ Rubik cube model """

    def __init__(self, 
        b: Face, 
        u: Face, 
        f: Face, 
        l: Face, 
        r: Face, 
        d: Face
    ):
        self.back = b
        self.up = u
        self.front = f
        self.left = l
        self.right = r
        self.down = d
