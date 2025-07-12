""" megaminx mover """
from pyminx.data.models.megaminx import Megaminx
from pyminx.moves.minx_mover import MinxMover
from pyminx.moves.megaminx.megaminx_axis_moves import MegaminxAxisMoves
from pyminx.moves.megaminx.megaminx_std_moves import MegaminxSTDMoves
from pyminx.moves.megaminx.megaminx_scramble_moves import MegaminxScrambleMoves


class MegaminxMover(MinxMover):
    """ megaminx mover """
    
    def __init__(self):
        self.std_moves = MegaminxSTDMoves()
        self.axis_moves = MegaminxAxisMoves()
        self.scramble_moves = MegaminxScrambleMoves()

    def simple_move(self, minx: Megaminx, mv: str) -> Megaminx:
        match mv:
            case "U": return self.std_moves.move_U(minx)
            case "U'": return minx
            case "U2": return minx
            
            case "D": return self.std_moves.move_D(minx)
            case "D'": return minx
            case "D2": return minx
            
            case "L": return self.std_moves.move_L(minx)
            case "L'": return minx
            case "L2": return minx
            
            case "R": return self.std_moves.move_R(minx)
            case "R'": return minx
            case "R2": return minx
            
            case "F": return self.std_moves.move_F(minx)
            case "F'": return minx
            case "F2": return minx
            
            case "xl": return self.axis_moves.move_xl(minx)
            case "xr": return self.axis_moves.move_xr(minx)
            
            case "y": return self.axis_moves.move_y(minx)
            
            case "z": return self.axis_moves.move_z(minx)
            
            case "D++": return self.scramble_moves.move_DPP(minx)
            case "D+": return self.scramble_moves.move_DP(minx)
            case "D--": return self.scramble_moves.move_DMM(minx)
            case "D-": return self.scramble_moves.move_DM(minx)
            
            case "R++": return self.scramble_moves.move_RPP(minx)
            case "R+": return self.scramble_moves.move_RP(minx)
            case "R--": return self.scramble_moves.move_RMM(minx)
            case "R-": return self.scramble_moves.move_RM(minx)
            
            case _: return minx
