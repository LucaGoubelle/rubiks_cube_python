from typing import List

Face = List[List[str]]


class MoveHelpers:
    """ move helpers """

    @staticmethod
    def gen_empty_face(size: int) -> Face:
        """ generate an empty face """
        return [
            ["" for _ in range(size)] for _ in range(size)
        ]

    @staticmethod
    def rotate(face: Face) -> Face:
        """ rotate a face """
        size: int = len(face)
        new_face: Face = MoveHelpers.gen_empty_face(size)
        for i in range(size):
            cnt: int = size - 1
            for j in range(size):
                new_face[i][j] = face[cnt][i]
                cnt -= 1
        return new_face

    @staticmethod
    def rotate_async(face: Face) -> Face:
        """ rotate a face other way """
        for _ in range(3):
            face = MoveHelpers.rotate(face)
        return face

    @staticmethod
    def rotate_twice(face: Face) -> Face:
        """ rotate a face twice """
        for _ in range(2):
            face = MoveHelpers.rotate(face)
        return face

    @staticmethod
    def transfert(face: Face, new_face: Face) -> Face:
        """ transfert a new_face on a face"""
        size: int = len(face)
        for i in range(size):
            for j in range(size):
                face[i][j] = new_face[i][j] if new_face[i][j] else face[i][j]
        return face
