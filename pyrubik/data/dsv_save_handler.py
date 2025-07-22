from typing import List
from pyrubik.data.cube import Cube


class DSVSaveHandler:
    """ DSV Save Handler """

    def __init__(self):
        self.filepath = "res/data/"
        self.delimiter = ";"
    
    def load(self, filename: str) -> Cube:
        """ 
        load cube save (.dsv file)
        @author: LucaGoubelle
        """
        fullpath: str = self.filepath+filename
        with open(fullpath, "r") as file:
            data: List[str] = file.readlines()
            file.close()
        
        fulldata: List[List[str]] = []
        for i in range(len(data)):
            fulldata.append(data[i].split(self.delimiter))
        
        back: List[List[str]] = [fulldata[0],fulldata[1],fulldata[2]]
        up: List[List[str]] = [fulldata[3],fulldata[4],fulldata[5]]
        front: List[List[str]] = [fulldata[6],fulldata[7],fulldata[8]]
        left: List[List[str]] = [fulldata[9],fulldata[10],fulldata[11]]
        right: List[List[str]] = [fulldata[12],fulldata[13],fulldata[14]]
        down: List[List[str]] = [fulldata[15],fulldata[16],fulldata[17]]
        return Cube(back,up,front,left,right,down)
    
    def save(self, filename: str, cube: Cube) -> None:
        """
        save cube to .dsv file
        @author: LucaGoubelle
        """
        fullpath: str = self.filepath+filename

        back: List[str] = [self.delimiter.join(line) for line in cube.back]
        up: List[str] = [self.delimiter.join(line) for line in cube.up]
        front: List[str] = [self.delimiter.join(line) for line in cube.front]
        left: List[str] = [self.delimiter.join(line) for line in cube.left]
        right: List[str] = [self.delimiter.join(line) for line in cube.right]
        down: List[str] = [self.delimiter.join(line) for line in cube.down]

        with open(fullpath, "w") as file:
            file.writelines(back)
            file.writelines(up)
            file.writelines(front)
            file.writelines(left)
            file.writelines(right)
            file.writelines(down)
            file.close()
