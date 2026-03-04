
class Processor:

    def __init__(self):
        self.data = {}
    
    def process(self, input_data: str) -> str:
        result: str = self.data[input_data] if input_data in self.data else "???"
        return result
