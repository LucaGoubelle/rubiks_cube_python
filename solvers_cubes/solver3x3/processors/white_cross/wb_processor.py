from solvers_cubes.solver3x3.processors.processor import Processor

class WBProcessor(Processor):
    
    def __init__(self):
        self.data = {}
        self.data["up_front"] = "F2"
        self.data["up_left"] = "U' F2"
        self.data["up_right"] = "U F2"
        self.data["up_back"] = "U2 F2"
            
        self.data["down_front"] = ""
        self.data["down_left"] = "D"
        self.data["down_right"] = "D'"
        self.data["down_back"] = "D2"

        self.data["front_left"] = "F'"
        self.data["front_right"] = "F"
        self.data["back_left"] = "L2 F'"
        self.data["back_right"] = "R2 F"
