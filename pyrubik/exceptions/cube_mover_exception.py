""" cube mover exception """

class CubeMoverException(Exception):
    """ cube mover exception """


    def __init__(self):
        super().__init__("ERR: invalid param cube, mv(s)...")
