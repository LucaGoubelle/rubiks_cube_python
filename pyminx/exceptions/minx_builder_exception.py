""" minx builder exception """

class MinxBuilderException(Exception):
    """ minx builder exception """

    def __init__(self):
        super().__init__("ERR: Something went wrong in MinxBuilder...")
