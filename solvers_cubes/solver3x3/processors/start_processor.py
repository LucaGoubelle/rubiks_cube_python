""" start processor """
from solvers_cubes.solver3x3.processors.processor import Processor

class StartProcessor(Processor):
    """ start processor """

    def __init__(self):
        self.data = {
            "yellow_blue": "",
            "yellow_green": "y2",
            "yellow_red": "y'",
            "yellow_orange": "y",
            
            "white_blue": "z2",
            "white_green": "x2",
            "white_red": "y z2",
            "white_orange": "y x2",
            
            "green_white": "x z2",
            "green_yellow": "x",
            "green_red": "z y'",
            "green_orange": "z' y",
            
            "blue_white": "x'",
            "blue_yellow": "x y2",
            "blue_red": "z' y'",
            "blue_orange": "z y",
            
            "red_white": "z x'",
            "red_yellow": "x y",
            "red_blue": "z",
            "red_green": "z x2",
            
            "orange_white": "x' y",
            "orange_yellow": "x y'",
            "orange_blue": "z'",
            "orange_green": "z y2",
        }
