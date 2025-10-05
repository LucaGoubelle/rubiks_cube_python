""" axis moves """
from copy import deepcopy

from pyrubik.data.cube import Cube, Face
from pyrubik.moves.moves import Moves

class AxisMoves(Moves):
    """ Axis moves """

    def move_y(self, cube: Cube) -> Cube:
        """ move y axis """
        cube.up = self.rh.rotate(cube.up)
        cube.down = self.rh.rotate_async(cube.down)
        
        newFront: Face = deepcopy(cube.right)
        newLeft: Face = deepcopy(cube.front)
        newRight: Face = deepcopy(cube.back)
        newBack: Face = deepcopy(cube.left)
        
        cube.front = self.rh.transfert(cube.front, newFront)
        cube.left = self.rh.transfert(cube.left, newLeft)
        cube.right = self.rh.transfert(cube.right, newRight)
        cube.back = self.rh.transfert(cube.back, newBack)
        
        return cube
    
    def move_y_prime(self, cube: Cube) -> Cube:
        """ move y axis reverse """
        for _ in range(3):
            cube = self.move_y(cube)
        return cube
    
    
    def move_y2(self, cube: Cube) -> Cube:
        """ move y axis twice """
        for _ in range(2):
            cube = self.move_y(cube)
        return cube
    
    
    def move_x(self, cube: Cube) -> Cube:
        """ move y axis """
        cube.right = self.rh.rotate(cube.right)
        cube.left = self.rh.rotate_async(cube.left)
        
        newFront: Face = deepcopy(cube.down)
        newUp: Face = deepcopy(cube.front)
        newBack: Face = self.rh.rotate_twice(deepcopy(cube.up))
        newDown: Face = self.rh.rotate_twice(deepcopy(cube.back))
        
        cube.front = self.rh.transfert(cube.front, newFront)
        cube.up = self.rh.transfert(cube.up, newUp)
        cube.back = self.rh.transfert(cube.back, newBack)
        cube.down = self.rh.transfert(cube.down, newDown)
        
        return cube
    
    def move_x_prime(self, cube: Cube) -> Cube:
        """ move x axis reverse """
        for _ in range(3):
            cube = self.move_x(cube)
        return cube
    

    def move_x2(self, cube: Cube) -> Cube:
        """ move x axis twice """
        for _ in range(2):
            cube = self.move_x(cube)
        return cube
    

    def move_z(self, cube: Cube) -> Cube:
        """ move y axis """
        cube.front = self.rh.rotate(cube.front)
        cube.back = self.rh.rotate_async(cube.back)
        
        newUp: Face = self.rh.rotate(deepcopy(cube.left))
        newRight: Face = self.rh.rotate(deepcopy(cube.up))
        newLeft: Face = self.rh.rotate(deepcopy(cube.down))
        newDown: Face = self.rh.rotate(deepcopy(cube.right))
        
        cube.up = self.rh.transfert(cube.up, newUp)
        cube.right = self.rh.transfert(cube.right, newRight)
        cube.left = self.rh.transfert(cube.left, newLeft)
        cube.down = self.rh.transfert(cube.down, newDown)
        
        return cube
    

    def move_z_prime(self, cube: Cube) -> Cube:
        """ move z axis reverse """
        for _ in range(3):
            cube = self.move_z(cube)
        return cube
    
    def move_z2(self, cube: Cube) -> Cube:
        """ move z axis twice """
        for _ in range(2):
            cube = self.move_z(cube)
        return cube
