""" minx mover exception """


class MinxMoverException(Exception):
    """ minx mover exception """

    def __init__(self):
        super().__init__("ERR: invalid param minx, mv(s)...")
