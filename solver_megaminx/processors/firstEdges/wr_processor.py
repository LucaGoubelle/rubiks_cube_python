""" wr edge processor """


class WRProcessor:
    """ wr edge processor """

    def __init__(self):
        self.data = {}

    def process(self, input_data: str) -> str:
        """
        return a processed information about what move to do
        for each cases depending on input_data param
        @author: LucaGoubelle
        """
        return self.data[input_data] if input_data in self.data else "???"
