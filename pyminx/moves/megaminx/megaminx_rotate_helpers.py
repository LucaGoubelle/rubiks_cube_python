from copy import deepcopy
from pyminx.data.models.megaminx import Face


class MegaminxRotateHelper:
    """
    megaminx rotate helper
    @author: LucaGoubelle
    """
    
    @staticmethod
    def gen_empty_face() -> Face:
        """
        generate an empty megaminx face
        @author: LucaGoubelle
        """
        return [[""] * 10, [""]]
    
    @staticmethod
    def copy_face(face: Face) -> Face:
        """
        return a deep copy of a provided face in param
        @author: LucaGoubelle
        """
        return deepcopy(face)
    
    @staticmethod
    def rotate(face: Face) -> Face:
        """
        rotate a face clockwise
        @author: LucaGoubelle
        """
        new_face: Face = MegaminxRotateHelper.gen_empty_face()
        
        new_face[0][0] = face[0][8]
        new_face[0][1] = face[0][9]
        new_face[0][2] = face[0][0]
        new_face[0][3] = face[0][1]
        new_face[0][4] = face[0][2]
        new_face[0][5] = face[0][3]
        new_face[0][6] = face[0][4]
        new_face[0][7] = face[0][5]
        new_face[0][8] = face[0][6]
        new_face[0][9] = face[0][7]
        
        new_face[1][0] = face[1][0]
        
        return new_face
    
    @staticmethod
    def rotate_async(face: Face) -> Face:
        """
        rotate a face counter-clockwise
        @author: LucaGoubelle
        """
        new_face: Face = MegaminxRotateHelper.gen_empty_face()
        
        new_face[0][0] = face[0][2]
        new_face[0][1] = face[0][3]
        new_face[0][2] = face[0][4]
        new_face[0][3] = face[0][5]
        new_face[0][4] = face[0][6]
        new_face[0][5] = face[0][7]
        new_face[0][6] = face[0][8]
        new_face[0][7] = face[0][9]
        new_face[0][8] = face[0][0]
        new_face[0][9] = face[0][1]
        
        new_face[1][0] = face[1][0]
        
        return new_face
    
    @staticmethod
    def rotate_twice(face: Face) -> Face:
        """

        @author: LucaGoubelle
        """
        for _ in range(2):
            face = MegaminxRotateHelper.rotate(face)
        return face
    
    @staticmethod
    def rotate_twice_async(face: Face) -> Face:
        """

        @author: LucaGoubelle
        """
        for _ in range(2):
            face = MegaminxRotateHelper.rotate_async(face)
        return face
    
    @staticmethod
    def rotate_three(face: Face) -> Face:
        """

        @author: LucaGoubelle
        """
        for _ in range(3):
            face = MegaminxRotateHelper.rotate(face)
        return face
    
    @staticmethod
    def rotate_three_async(face: Face) -> Face:
        """

        @author: LucaGoubelle
        """
        for _ in range(3):
            face = MegaminxRotateHelper.rotate_async(face)
        return face
    
    @staticmethod
    def transfert(face: Face, new_face: Face) -> Face:
        """
        transfert a face on another face
        @author: LucaGoubelle
        """
        size_round1: int = len(face[0])
        for i in range(size_round1):
            face[0][i] = new_face[0][i] if new_face[0][i] else face[0][i]
        face[1][0] = new_face[1][0] if new_face[1][0] else face[1][0]
        return face
