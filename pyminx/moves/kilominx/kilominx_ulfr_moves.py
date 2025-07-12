""" kilominx ulfr moves """
from pyminx.data.models.kilominx import Kilominx
from pyminx.moves.kilominx.kilominx_rotate_helpers import KilominxRotateHelpers


class KilominxULRFMoves:
    """ 
    kilominx ulrf moves 
    provide moves for:
    - U => up face
    - L => left face
    - R => right face
    - F => front face
    @author: LucaGoubelle
    """

    def move_U(self, minx: Kilominx) -> Kilominx:
        minx.up = KilominxRotateHelpers.rotate(minx.up)

        new_front = [minx.right[0], minx.right[1], "", "", ""]
        new_right = [minx.back_right[0], minx.back_right[1], "", "", ""]
        new_left = [minx.front[0], minx.front[1], "", "", ""]
        new_back_left = [minx.left[0], minx.left[1], "", "", ""]
        new_back_right = [minx.back_left[0], minx.back_left[1], "", "", ""]

        minx.front = KilominxRotateHelpers.transfert(minx.front, new_front)
        minx.right = KilominxRotateHelpers.transfert(minx.right, new_right)
        minx.left = KilominxRotateHelpers.transfert(minx.left, new_left)
        minx.back_left = KilominxRotateHelpers.transfert(minx.back_left, new_back_left)
        minx.back_right = KilominxRotateHelpers.transfert(minx.back_right, new_back_right)

        return minx

    def move_U_prime(self, minx: Kilominx) -> Kilominx:
        for i in range(4):
            minx = self.move_U(minx)
        return minx

    def move_L(self, minx: Kilominx) -> Kilominx:
        minx.left = KilominxRotateHelpers.rotate(minx.left)

        new_up = ["", "", "", minx.back_left[1], minx.back_left[2]]
        new_front = [minx.up[4], "", "", "", minx.up[3]]
        new_down_left = [minx.front[0], "", "", "", minx.front[4]]
        new_abs_left = [minx.down_left[4], minx.down_left[0], "", "", ""]
        new_back_left = ["", minx.abs_left[0], minx.abs_left[1], "", ""]

        minx.up = KilominxRotateHelpers.transfert(minx.up, new_up)
        minx.front = KilominxRotateHelpers.transfert(minx.front, new_front)
        minx.down_left = KilominxRotateHelpers.transfert(minx.down_left, new_down_left)
        minx.abs_left = KilominxRotateHelpers.transfert(minx.abs_left, new_abs_left)
        minx.back_left = KilominxRotateHelpers.transfert(minx.back_left, new_back_left)

        return minx

    def move_L_prime(self, minx: Kilominx) -> Kilominx:
        for i in range(4):
            minx = self.move_L(minx)
        return minx

    def move_R(self, minx: Kilominx) -> Kilominx:
        minx.right = KilominxRotateHelpers.rotate(minx.right)

        new_up = ["", minx.front[1], minx.front[2], "", ""]
        new_front = ["", minx.down_right[0], minx.down_right[1], "", ""]
        new_down_right = [minx.abs_right[4], minx.abs_right[0], "", "", ""]
        new_back_right = [minx.up[2], "", "", "", minx.up[1]]
        new_abs_right = [minx.back_right[0], "", "", "", minx.back_right[4]]

        minx.up = KilominxRotateHelpers.transfert(minx.up, new_up)
        minx.front = KilominxRotateHelpers.transfert(minx.front, new_front)
        minx.down_right = KilominxRotateHelpers.transfert(minx.down_right, new_down_right)
        minx.back_right = KilominxRotateHelpers.transfert(minx.back_right, new_back_right)
        minx.abs_right = KilominxRotateHelpers.transfert(minx.abs_right, new_abs_right)

        return minx

    def move_R_prime(self, minx: Kilominx) -> Kilominx:
        for i in range(4):
            minx = self.move_R(minx)
        return minx

    def move_F(self, minx: Kilominx) -> Kilominx:
        minx.front = KilominxRotateHelpers.rotate(minx.front)

        new_up = ["", "", minx.left[1], minx.left[2], ""]
        new_left = ["", minx.down_left[0], minx.down_left[1], "", ""]
        new_right = [minx.up[3], "", "", "", minx.up[2]]
        new_down_left = [minx.down_right[4], minx.down_right[0], "", "", ""]
        new_down_right = [minx.right[0], "", "", "", minx.right[4]]

        minx.up = KilominxRotateHelpers.transfert(minx.up, new_up)
        minx.left = KilominxRotateHelpers.transfert(minx.left, new_left)
        minx.right = KilominxRotateHelpers.transfert(minx.right, new_right)
        minx.down_left = KilominxRotateHelpers.transfert(minx.down_left, new_down_left)
        minx.down_right = KilominxRotateHelpers.transfert(minx.down_right, new_down_right)

        return minx

    def move_F_prime(self, minx: Kilominx) -> Kilominx:
        for i in range(4):
            minx = self.move_F(minx)
        return minx
