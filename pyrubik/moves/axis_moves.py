""" axis moves """
from copy import deepcopy

from pyrubik.data.cube import Cube
from pyrubik.moves.helpers.move_helpers import MoveHelpers, Face

class AxisMoves:
    """ Axis moves """

    def move_y(self, cube: Cube) -> Cube:
        """ move y axis """
        cube.up = MoveHelpers.rotate(cube.up)
        cube.down = MoveHelpers.rotate_async(cube.down)
        
        newFront: Face = deepcopy(cube.right)
        newLeft: Face = deepcopy(cube.front)
        newRight: Face = deepcopy(cube.back)
        newBack: Face = deepcopy(cube.left)
        
        cube.front = MoveHelpers.transfert(cube.front, newFront)
        cube.left = MoveHelpers.transfert(cube.left, newLeft)
        cube.right = MoveHelpers.transfert(cube.right, newRight)
        cube.back = MoveHelpers.transfert(cube.back, newBack)
        
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
        cube.right = MoveHelpers.rotate(cube.right)
        cube.left = MoveHelpers.rotate_async(cube.left)
        
        newFront: Face = deepcopy(cube.down)
        newUp: Face = deepcopy(cube.front)
        newBack: Face = MoveHelpers.rotate_twice(deepcopy(cube.up))
        newDown: Face = MoveHelpers.rotate_twice(deepcopy(cube.back))
        
        cube.front = MoveHelpers.transfert(cube.front, newFront)
        cube.up = MoveHelpers.transfert(cube.up, newUp)
        cube.back = MoveHelpers.transfert(cube.back, newBack)
        cube.down = MoveHelpers.transfert(cube.down, newDown)
        
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
        cube.front = MoveHelpers.rotate(cube.front)
        cube.back = MoveHelpers.rotate_async(cube.back)
        
        newUp: Face = MoveHelpers.rotate(deepcopy(cube.left))
        newRight: Face = MoveHelpers.rotate(deepcopy(cube.up))
        newLeft: Face = MoveHelpers.rotate(deepcopy(cube.down))
        newDown: Face = MoveHelpers.rotate(deepcopy(cube.right))
        
        cube.up = MoveHelpers.transfert(cube.up, newUp)
        cube.right = MoveHelpers.transfert(cube.right, newRight)
        cube.left = MoveHelpers.transfert(cube.left, newLeft)
        cube.down = MoveHelpers.transfert(cube.down, newDown)
        
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
