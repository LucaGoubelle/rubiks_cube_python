
from pyminx.data.models.megaminx import Megaminx


class MegaminxAxisMoves:
    """ megaminx axis moves """
    
    
    def move_y(self, minx: Megaminx) -> Megaminx:
        #TODO: implement this
        return minx
    
    
    def move_y_prime(self, minx: Megaminx) -> Megaminx:
        for _ in range(4):
            minx = MegaminxAxisMoves.move_y(minx)
        return minx
    
    
    def move_xl(self, minx: Megaminx) -> Megaminx:
        #TODO: implement this
        return minx
    
    
    def move_xl_prime(self, minx: Megaminx) -> Megaminx:
        for _ in range(4):
            minx = MegaminxAxisMoves.move_xl(minx)
        return minx
    
    
    def move_xr(self, minx: Megaminx) -> Megaminx:
        #TODO: implement this
        return minx
    
    
    def move_xr_prime(self, minx: Megaminx) -> Megaminx:
        for _ in range(4):
            minx = MegaminxAxisMoves.move_xr(minx)
        return minx
    
    
    def move_z(self, minx: Megaminx) -> Megaminx:
        #TODO: implement this
        return minx
    
    
    def move_z_prime(self, minx: Megaminx) -> Megaminx:
        for _ in range(4):
            minx = MegaminxAxisMoves.move_z(minx)
        return minx
