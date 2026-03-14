""" center orient processor """
from solvers_minxs.solver_megaminx.processors.processor import Processor

class CenterOrientProcessor(Processor):
    """ center orient processor """

    def __init__(self):
        self.data = {
            "grey_magenta_lime": "z2 xL",
            "grey_beige_magenta": "y z2 xL"
        }
