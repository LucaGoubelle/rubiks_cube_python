import json
from typing import Any
from pyrubik.data.cube import Cube
from pyrubik.exceptions.save_handler_exception import SaveHandlerException

class JSONSaveHandler:
    """ JSON Save Handler """
    
    def __init__(self):
        self.filepath = "res/data/json/"
        
    def load(self, filename: str) -> Cube:
        """ 
        load cube save (.json file)
        @author: LucaGoubelle
        """
        try:
            fullpath: str = self.filepath+filename
            with open(fullpath, "r") as file:
                data = json.load(file)
            return Cube(
                data["back"], data["up"], data["front"], 
                data["left"], data["right"], data["down"]
            )
        except Exception as exc:
            raise SaveHandlerException() from exc
        
    def save(self, filename: str, cube: Cube) -> str:
        """
        save cube to .json file
        @author: LucaGoubelle
        """
        try:
            fullpath: str = self.filepath+filename
            data: dict[str, Any] = cube.__dict__
            with open(fullpath, "w") as file:
                json.dump(data, file, indent=4)
            return "success !"
        except Exception as exc:
                raise SaveHandlerException() from exc
