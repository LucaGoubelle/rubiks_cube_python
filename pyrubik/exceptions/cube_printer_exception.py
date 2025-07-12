""" cube printer exception """

class CubePrinterException(Exception):
    """ cube printer exception """

    def __init__(self):
        super().__init__("ERR: invalid cube object in input...")
