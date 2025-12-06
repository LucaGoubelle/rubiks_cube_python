
from solver_helpers.casters.centers.centers_caster import CentersCaster


class Centers7x7Caster(CentersCaster):
    """ center 7x7 caster """

    def __init__(self):
        self.size = 7

    def _exctract_centers(self, actual_face):
        return [
            [actual_face[1][1], actual_face[1][2], actual_face[1][3], actual_face[1][4]],
            [actual_face[2][1], actual_face[2][2], actual_face[2][3], actual_face[2][4]],
            [actual_face[3][1], actual_face[3][2], actual_face[3][3], actual_face[3][4]],
            [actual_face[4][1], actual_face[4][2], actual_face[4][3], actual_face[4][4]],
            [actual_face[5][1], actual_face[5][2], actual_face[5][3], actual_face[5][4]]
        ]
