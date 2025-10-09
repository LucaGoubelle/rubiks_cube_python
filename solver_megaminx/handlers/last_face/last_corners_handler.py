""" last corners handler """
from pyminx.data.models.megaminx import Megaminx
from solver_megaminx.handlers.handler import Handler

class LastCornersHandler(Handler):
    """last corners Handler"""
    
    def __init__(self):
        super().__init__()
    
    def handle(self, minx: Megaminx) -> Megaminx:
        # implement this
        return minx
