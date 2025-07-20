
class WGOProcessor:
    """ white green orange processor """

    def __init__(self):
        self.data = {
            "up_front_left::white_green_orange" : "L2",
            "up_front_left::orange_white_green" : "U L U L'",
            "up_front_left::green_orange_white" : "U L'",

            "up_front_right::white_orange_green" : "U L2",
            "up_front_right::green_white_orange" : "U2 L'",
            "up_front_right::orange_green_white" : "U2 L U L'",
            
            "up_back_right::white_green_orange" : "U2 L2",
            "up_back_right::orange_white_green" : "U' L U L'",
            "up_back_right::green_orange_white" : "U' L'",
            
            "up_back_left::white_orange_green" : "U' L2",
            "up_back_right::green_white_orange" : "L'",
            "up_back_right::orange_green_white" : "L U L'",

            "down_front_left::white_orange_green" : "L2 U' L2",
            "down_front_left::green_white_orange" : "L",
            "down_front_left::orange_green_white" : "L' U L'",

            "down_back_left::orange_white_green" : "L U' L2",
            "down_back_left::green_orange_white" : "L2 U L'"
        }

    def process(self, input_data: str) -> str:
        result: str = self.data[input_data] if input_data in self.data else "???"
        return result
