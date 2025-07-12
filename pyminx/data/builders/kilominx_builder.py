""" kilominx builder"""
from pyminx.data.models.kilominx import Kilominx
from pyminx.exceptions.minx_builder_exception import MinxBuilderException


class KilominxBuilder:
    """ 
    kilominx builder, 
    build a full kilominx puzzle 
    @author: LucaGoubelle
    """

    def __init__(self):
        self.round1 = 5

    def build(self) -> Kilominx:
        try:
            return Kilominx(
                ["grey"] * self.round1,
                ["magenta"] * self.round1,
                ["lime"] * self.round1,
                ["beige"] * self.round1,
                ["blue"] * self.round1,
                ["red"] * self.round1,
    
                ["yellow"] * self.round1,
                ["green"] * self.round1,
                ["orange"] * self.round1,
                ["cyan"] * self.round1,
                ["purple"] * self.round1,
                ["white"] * self.round1
            )
        except Exception as exc:
            raise MinxBuilderException() from exc
