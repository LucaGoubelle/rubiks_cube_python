""" megaminx builder """
from pyminx.data.models.megaminx import Megaminx
from pyminx.exceptions.minx_builder_exception import MinxBuilderException


class MegaminxBuilder:
    """ 
    megaminx builder, 
    build a full megaminx puzzle 
    @author: LucaGoubelle
    """
    
    def __init__(self):
        self.round1 = 10
    
    def build(self) -> Megaminx:
        try:
            return Megaminx(
                [["grey"] * self.round1, ["grey"]],
                [["magenta"] * self.round1, ["magenta"]],
                [["lime"] * self.round1, ["lime"]],
                [["beige"] * self.round1, ["beige"]],
                [["blue"] * self.round1, ["blue"]],
                [["red"] * self.round1, ["red"]],
                [["yellow"] * self.round1, ["yellow"]],
                [["green"] * self.round1, ["green"]],
                [["orange"] * self.round1, ["orange"]],
                [["cyan"] * self.round1, ["cyan"]],
                [["purple"] * self.round1, ["purple"]],
                [["white"] * self.round1, ["white"]]
            )
        except Exception as exc:
            raise MinxBuilderException() from exc
