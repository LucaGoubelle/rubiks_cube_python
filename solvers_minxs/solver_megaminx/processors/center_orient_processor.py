""" center orient processor """


class CenterOrientProcessor:
    """ center orient processor """

    def __init__(self):
        self.data = {
            "grey_magenta_lime": "z2 xL",
            "grey_beige_magenta": "y z2 xL"
        }

    def process(self, input_data: str) -> str:
        """
        return a processed information about what move to do
        for each cases depending on input_data param
        @author: LucaGoubelle
        """
        return self.data[input_data] if input_data in self.data else "???"
