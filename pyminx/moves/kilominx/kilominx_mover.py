""" kilominx mover """
from pyminx.data.models.kilominx import Kilominx
from pyminx.moves.minx_mover import MinxMover
from pyminx.moves.kilominx.kilominx_axis_moves import KilominxAxisMoves
from pyminx.moves.kilominx.kilominx_ulfr_moves import KilominxULRFMoves


class KilominxMover(MinxMover):
    """ 
    kilominx mover object,
    provide moving puzzle methods
    @author: LucaGoubelle
    """

    def __init__(self):
        self.ulrf_moves = KilominxULRFMoves()
        self.axis_moves = KilominxAxisMoves()

    def simple_move(self, minx: Kilominx, mv: str) -> Kilominx:
        match mv:
            case "U": return self.ulrf_moves.move_U(minx)
            case "U'": return self.ulrf_moves.move_U_prime(minx)
            case "L": return self.ulrf_moves.move_L(minx)
            case "L'": return self.ulrf_moves.move_L_prime(minx)
            case "R": return self.ulrf_moves.move_R(minx)
            case "R'": return self.ulrf_moves.move_R_prime(minx)
            case "F": return self.ulrf_moves.move_F(minx)
            case "F'": return self.ulrf_moves.move_F_prime(minx)
            case "y": return self.axis_moves.move_y(minx)
            case "y'": return self.axis_moves.move_y_prime(minx)
            case _: return minx
