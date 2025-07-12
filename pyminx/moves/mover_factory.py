""" mover factory """
from pyminx.moves.minx_mover import MinxMover
from pyminx.moves.kilominx.kilominx_mover import KilominxMover
from pyminx.moves.megaminx.megaminx_mover import MegaminxMover
from pyminx.moves.master_kilominx.mk_mover import MasterKilominxMover


class MoverFactory:
    """ 
    mover factory
    @author: LucaGoubelle
    """
    
    def make(self, puzzle_type: str) -> MinxMover:
        """
        make a mover object depending on puzzle_type argument
        @author: LucaGoubelle
        """
        match puzzle_type:
            case "kilominx": return KilominxMover()
            case "megaminx": return MegaminxMover()
            case "masterKilominx": return MasterKilominxMover()
            case _: return MegaminxMover()
