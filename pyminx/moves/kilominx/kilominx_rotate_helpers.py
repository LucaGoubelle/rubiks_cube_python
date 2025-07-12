""" rotate helpers """
from copy import deepcopy
from pyminx.data.models.kilominx import Face


class KilominxRotateHelpers:
    """ 
    kilominx rotate utils 
    @author: LucaGoubelle
    """

    @staticmethod
    def gen_empty_face() -> Face:
        """
        generate an empty kilominx face
        @author: LucaGoubelle
        """
        return [""] * 5

    
    @staticmethod
    def copy_face(face: Face) -> Face:
        """
        return a deep copy of the provided face param
        @author: LucaGoubelle
        """
        return deepcopy(face)

    
    @staticmethod
    def rotate(face: Face) -> Face:
        """ 
        rotate a face clockwise 
        @author: LucaGoubelle
        """
        new_face: Face = KilominxRotateHelpers.gen_empty_face()

        new_face[0] = face[4]
        new_face[1] = face[0]
        new_face[2] = face[1]
        new_face[3] = face[2]
        new_face[4] = face[3]

        return new_face

    
    @staticmethod
    def rotate_async(face: Face) -> Face:
        """ 
        rotate a face counter-clockwise 
        @author: LucaGoubelle
        """
        new_face: Face = KilominxRotateHelpers.gen_empty_face()

        new_face[0] = face[1]
        new_face[1] = face[2]
        new_face[2] = face[3]
        new_face[3] = face[4]
        new_face[4] = face[0]

        return new_face

    
    @staticmethod
    def rotate_twice(face: Face) -> Face:
        """ 
        rotate a face clockwise twice 
        @author: LucaGoubelle
        """
        for i in range(2):
            face = KilominxRotateHelpers.rotate(face)
        return face

    
    @staticmethod
    def rotate_async_twice(face: Face) -> Face:
        """ 
        rotate a face counter-clockwise twice 
        @author: LucaGoubelle
        """
        for i in range(2):
            face = KilominxRotateHelpers.rotate_async(face)
        return face

    
    @staticmethod
    def transfert(face: Face, new_face: Face) -> Face:
        """
        transfert a face on another face,
        if the face contain empty string,
        the index are ignored (old string remain)
        @author: LucaGoubelle
        """
        for i in range(len(face)):
            face[i] = new_face[i] if new_face[i] != "" else face[i]
        return face
