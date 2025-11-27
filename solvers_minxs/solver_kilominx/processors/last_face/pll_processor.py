
class PLLProcessor:
    """ PLLs processor """

    def __init__(self):
        self.data = {}

    def process(self, input_data: str) -> str:
        return self.data[input_data] if input_data in self.data else "???"
