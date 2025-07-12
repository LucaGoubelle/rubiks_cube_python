""" abs class for minx puzzles mover """
from pyminx.data.models.minx import Minx
from pyminx.exceptions.minx_mover_exception import MinxMoverException


class MinxMover:
    """
    abstract class for minx's puzzles mover
    @author: LucaGoubelle
    """

    def simple_move(self, minx: Minx, mv: str) -> Minx:
        """
        move the puzzle with a specific axis in param (mv)
        return the puzzle by default if no match
        @author: LucaGoubelle
        """
        raise NotImplementedError()

    def multi_moves(self, minx: Minx, mvs: str) -> Minx:
        """
        move the puzzle multiple times with a specific sequence (string mvs)
        return the altered puzzle
        @author: LucaGoubelle
        """
        try:
            mv_lst = mvs.split(" ")
            for mv in mv_lst:
                minx = self.simple_move(minx, mv)
            return minx
        except Exception as exc:
            raise MinxMoverException() from exc
