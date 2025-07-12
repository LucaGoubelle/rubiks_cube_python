""" master kilominx builder """
from pyminx.data.models.master_kilominx import MasterKilominx
from pyminx.exceptions.minx_builder_exception import MinxBuilderException


class MasterKilominxBuilder:
    """ 
    master kilominx builder, 
    build a full master kilominx puzzle 
    @author: LucaGoubelle
    """

    def __init__(self):
        self.round1 = 15
        self.round2 = 5

    def build(self):
        try:
            return MasterKilominx(
                [["grey"] * self.round1, ["grey"] * self.round2],
                [["magenta"] * self.round1, ["magenta"] * self.round2],
                [["lime"] * self.round1, ["lime"] * self.round2],
                [["beige"] * self.round1, ["beige"] * self.round2],
                [["blue"] * self.round1, ["blue"] * self.round2],
                [["red"] * self.round1, ["red"] * self.round2],
    
                [["yellow"] * self.round1, ["yellow"] * self.round2],
                [["green"] * self.round1, ["green"] * self.round2],
                [["orange"] * self.round1, ["orange"] * self.round2],
                [["cyan"] * self.round1, ["cyan"] * self.round2],
                [["purple"] * self.round1, ["purple"] * self.round2],
                [["white"] * self.round1, ["white"] * self.round2]
            )
        except Exception as exc:
            raise MinxBuilderException() from exc
