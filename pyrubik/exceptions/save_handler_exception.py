""" save handler exception """

class SaveHandlerException(Exception):
    """ save handler exception """

    def __init__(self):
        super().__init__("ERR: invalid path or in/out data...")
