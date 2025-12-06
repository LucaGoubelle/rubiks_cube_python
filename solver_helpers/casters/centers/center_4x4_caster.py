
from solver_helpers.casters.centers.centers_caster import CentersCaster


class Centers4x4Caster(CentersCaster):
    """ center 4x4 caster """

    def __init__(self):
        self.size = 4

    def _exctract_centers(self, actual_face):
        return [
            [actual_face[1][1], actual_face[1][2]],
            [actual_face[2][1], actual_face[2][2]]
        ]
