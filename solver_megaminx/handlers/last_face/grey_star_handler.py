""" grey star handler """
from pyminx.data.models.megaminx import Megaminx
from solver_megaminx.handlers.handler import Handler

class GreyStarHandler(Handler):
    """Grey Star Handler"""
    
    def __init__(self):
        super().__init__()
    
    def handle(self, minx: Megaminx) -> Megaminx:
        # implement this
        return minx
