from pyrubik.data.cube import Cube
from pyrubik.exceptions.cube_builder_exception import CubeBuilderException


class CubeBuilder:
    """ build a cube object """

    def build(self, size: int) -> Cube:
        """
        build a full rubiks cube with a specific size
        @author: LucaGoubelle
        """
        try:
            return Cube(
                [["green" for _ in range(size)] for _ in range(size)],
                [["yellow" for _ in range(size)] for _ in range(size)],
                [["blue" for _ in range(size)] for _ in range(size)],
                [["orange" for _ in range(size)] for _ in range(size)],
                [["red" for _ in range(size)] for _ in range(size)],
                [["white" for _ in range(size)] for _ in range(size)]
            )
        except Exception as exc:
            raise CubeBuilderException() from exc
