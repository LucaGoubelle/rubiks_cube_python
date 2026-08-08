""" mk rotate helpers """
from pyminx.data.models.master_kilominx import Face
from pyminx.moves.rotate_helpers import RotateHelpers

class MasterKilominxRotateHelpers(RotateHelpers):
    """
    master kilominx rotate helpers
    @author: LucaGoubelle
    """

    @staticmethod
    def gen_empty_face() -> Face:
        """
        generate an empty master-kilominx face
        @author: LucaGoubelle
        """
        return [[""] * 15, [""] * 5]

    # todo: implement rotate + async

    @staticmethod
    def transfert(face: Face, new_face: Face) -> Face:
        """
        transfert a face on another face,
        element of newFace are ignored if empty string
        @author: LucaGoubelle
        """
        for i in range(len(face[0])):
            face[0][i] = new_face[0][i] if new_face[0][i] != "" else face[0][i]
        for j in range(len(face[1])):
            face[1][j] = new_face[1][j] if new_face[1][j] != "" else face[1][j]
        return face
