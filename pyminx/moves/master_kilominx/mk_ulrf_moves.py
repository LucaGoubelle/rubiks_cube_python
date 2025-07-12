""" mk ulrf moves """


class MasterKilominxULRFMoves:
    """
    mk ulrf moves
    """

    def move_U(self, minx):
        # todo : implement this
        return minx

    def move_U_prime(self, minx):
        for i in range(4):
            minx = self.move_U(minx)
        return minx
