""" rotate helpers """
from copy import deepcopy


class RotateHelpers:
    """
    rotate utils
    @author: LucaGoubelle
    """
    
    @staticmethod
    def copy_face(face):
        """
        return a deep copy of the provided face param
        @author: LucaGoubelle
        """
        return deepcopy(face)
