from typing import List
from copy import deepcopy

Face = List[List[str]]


class MoveHelpers:
    """ move helpers """

    def gen_empty_face(self, size: int) -> Face:
        """ generate an empty face """
        return [
            ["" for _ in range(size)] for _ in range(size)
        ]
        
    def copy_face(self, face: Face) -> Face:
        """ copy face """
        return deepcopy(face)

    def rotate(self, face: Face) -> Face:
        """ rotate a face """
        size: int = len(face)
        new_face: Face = self.gen_empty_face(size)
        for i in range(size):
            cnt: int = size - 1
            for j in range(size):
                new_face[i][j] = face[cnt][i]
                cnt -= 1
        return new_face

    def rotate_async(self, face: Face) -> Face:
        """ rotate a face other way """
        for _ in range(3):
            face = self.rotate(face)
        return face

    def rotate_twice(self, face: Face) -> Face:
        """ rotate a face twice """
        for _ in range(2):
            face = self.rotate(face)
        return face

    def transfert(self, face: Face, new_face: Face) -> Face:
        """ transfert a new_face on a face"""
        size: int = len(face)
        for i in range(size):
            for j in range(size):
                face[i][j] = new_face[i][j] if new_face[i][j] else face[i][j]
        return face
