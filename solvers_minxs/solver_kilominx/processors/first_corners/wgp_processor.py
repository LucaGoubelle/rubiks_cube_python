""" wgp processor """


class WGPProcessor:
    """ WGP edge processor """

    def __init__(self):
        self.data = {}

    def process(self, input_data: str) -> str:
        """
        process information in input,
        return the corresponding sequence of move
        @author: LucaGoubelle
        """
        return self.data[input_data] if input_data in self.data else "???"
