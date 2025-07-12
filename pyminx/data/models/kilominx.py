""" megaminx data model """
from typing import List
from pyminx.data.models.minx import Minx

Face = List[str]


class Kilominx(Minx):
    """ 
    kilominx data model, each faces is a list of string (size 5) 
    @author: LucaGoubelle
    """

    def __init__(self,
        up: Face, front: Face, left: Face, right: Face, 
        down_left: Face, down_right: Face,abs_left: Face, abs_right: Face, 
        back_left: Face, back_right: Face, back: Face, down: Face
    ):
        self.up = up
        self.front = front
        self.left = left
        self.right = right
        self.down_left = down_left
        self.down_right = down_right
        self.abs_left = abs_left
        self.abs_right = abs_right
        self.back_left = back_left
        self.back_right = back_right
        self.back = back
        self.down = down
