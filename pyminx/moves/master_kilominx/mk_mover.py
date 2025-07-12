""" mk mover """
from pyminx.data.models.master_kilominx import MasterKilominx
from pyminx.moves.minx_mover import MinxMover
from pyminx.moves.master_kilominx.mk_ulrf_moves import MasterKilominxULRFMoves


class MasterKilominxMover(MinxMover):
    """
    master kilominx mover
    @author: LucaGoubelle
    """

    def __init__(self):
        self.ulrf_moves = MasterKilominxULRFMoves()

    def simple_move(self, minx: MasterKilominx, mv: str) -> MasterKilominx:
        match mv:
            case "U": return self.ulrf_moves.move_U(minx)
            case "U'": return self.ulrf_moves.move_U_prime(minx)
            case _: return minx
