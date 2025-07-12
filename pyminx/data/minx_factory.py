""" minx factory """
from pyminx.data.models.minx import Minx
from pyminx.data.builders.kilominx_builder import KilominxBuilder
from pyminx.data.builders.megaminx_builder import MegaminxBuilder
from pyminx.data.builders.master_kilominx_builder import MasterKilominxBuilder


class MinxFactory:
    """ minx factory """

    def __init__(self):
        self.kilo_builder = KilominxBuilder()
        self.mega_builder = MegaminxBuilder()
        self.mk_builder = MasterKilominxBuilder()

    def make(self, puzzle_type: str) -> Minx:
        """
        make a puzzle based on the 'puzzle_type' parametter
        @author: LucaGoubelle
        """
        match puzzle_type:
            case "kilominx": return self.kilo_builder.build()
            case "megaminx": return self.mega_builder.build()
            case "master_kilominx": return self.mk_builder.build()
            case _: return self.mega_builder.build()
