
from solver_helpers.casters.centers.centers_caster import CentersCaster


class Centers5x5Caster(CentersCaster):
    """ center 5x5 caster """

    def __init__(self):
        self.size = 5

    def _exctract_centers(self, actual_face):
        return [
            [actual_face[1][1], actual_face[1][2], actual_face[1][3]],
            [actual_face[2][1], actual_face[2][2], actual_face[2][3]],
            [actual_face[3][1], actual_face[3][2], actual_face[3][3]]
        ]
