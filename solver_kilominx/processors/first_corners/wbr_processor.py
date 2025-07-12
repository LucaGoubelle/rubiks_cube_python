""" wbr processor """

class WBRProcessor:
    """ wbr processor """

    def __init__(self):
        self.data = {}

    def process(self, input_data: str) -> str:
        """
        process input information, return sequence of corresponding moves
        @author: LucaGoubelle
        """
        return self.data[input_data] if input_data in self.data else "???"
