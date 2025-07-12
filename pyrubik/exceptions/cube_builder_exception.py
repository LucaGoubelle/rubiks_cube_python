""" cube builder exception """

class CubeBuilderException(Exception):
    """ cube builder exception """

    def __init__(self):
        super().__init__("ERR: invalid size argument...")
