""" prisms handler """
from pyminx.data.models.megaminx import Megaminx
from solver_megaminx.handlers.handler import Handler

from solver_megaminx.handlers.prisms.beige_prism_handler import BeigePrismHandler
from solver_megaminx.handlers.prisms.cyan_prism_handler import CyanPrismHandler
from solver_megaminx.handlers.prisms.lime_prism_handler import LimePrismHandler
from solver_megaminx.handlers.prisms.magenta_prism_handler import MagentaPrismHandler
from solver_megaminx.handlers.prisms.orange_prism_handler import OrangePrismHandler

class PrismsHandler(Handler):
    """ prisms handler """
    
    def __init__(self):
        super().__init__()
    
    def handle(self, minx: Megaminx) -> Megaminx:
        minx = MagentaPrismHandler.handle(minx)
        minx = LimePrismHandler.handle(minx)
        minx = BeigePrismHandler.handle(minx)
        minx = OrangePrismHandler.handle(minx)
        minx = CyanPrismHandler.handle(minx)
        return minx
