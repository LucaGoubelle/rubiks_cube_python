""" kilominx axis moves """
from pyminx.data.models.kilominx import Kilominx
from pyminx.moves.kilominx.kilominx_rotate_helpers import KilominxRotateHelpers


class KilominxAxisMoves:
    """ 
    kilominx axis moves 
    @author: LucaGoubelle
    """

    def move_y(self, minx: Kilominx) -> Kilominx:
        """
        rotate all the kilominx on y axis
        @author: LucaGoubelle
        """
        minx.up = KilominxRotateHelpers.rotate(minx.up)
        minx.down = KilominxRotateHelpers.rotate_async(minx.down)

        new_front = KilominxRotateHelpers.copy_face(minx.right)
        new_right = KilominxRotateHelpers.copy_face(minx.back_right)
        new_left = KilominxRotateHelpers.copy_face(minx.front)
        new_back_left = KilominxRotateHelpers.copy_face(minx.left)
        new_back_right = KilominxRotateHelpers.copy_face(minx.back_left)

        new_down_left = KilominxRotateHelpers.copy_face(minx.down_right)
        new_down_right = KilominxRotateHelpers.copy_face(minx.abs_right)
        new_abs_left = KilominxRotateHelpers.copy_face(minx.down_left)
        new_abs_right = KilominxRotateHelpers.copy_face(minx.back)
        new_back = KilominxRotateHelpers.copy_face(minx.abs_left)

        minx.front = KilominxRotateHelpers.transfert(minx.front, new_front)
        minx.right = KilominxRotateHelpers.transfert(minx.right, new_right)
        minx.left = KilominxRotateHelpers.transfert(minx.left, new_left)
        minx.back_left = KilominxRotateHelpers.transfert(minx.back_left, new_back_left)
        minx.back_right = KilominxRotateHelpers.transfert(minx.back_right, new_back_right)

        minx.down_left = KilominxRotateHelpers.transfert(minx.down_left, new_down_left)
        minx.down_right = KilominxRotateHelpers.transfert(minx.down_right, new_down_right)
        minx.abs_left = KilominxRotateHelpers.transfert(minx.abs_left, new_abs_left)
        minx.abs_right = KilominxRotateHelpers.transfert(minx.abs_right, new_abs_right)
        minx.back = KilominxRotateHelpers.transfert(minx.back, new_back)

        return minx

    def move_y_prime(self, minx: Kilominx) -> Kilominx:
        """
        rotate all the kilominx on y axis
        in counter clockwise
        @author: LucaGoubelle
        """
        for i in range(4):
            minx = self.move_y(minx)
        return minx
