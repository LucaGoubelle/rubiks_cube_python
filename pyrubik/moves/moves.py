""" standard moves """
from pyrubik.data.cube import Cube
from pyrubik.moves.helpers.move_helpers import MoveHelpers, Face

class STDMoves:
    """ standard moves """
    
    
    def move_U(self, cube: Cube) -> Cube:
        """ move Up face """
        size: int = len(cube.up)
        cube.up = MoveHelpers.rotate(cube.up)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            new_front[0][i] = cube.right[0][i]
            new_left[0][i] = cube.front[0][i]
            new_right[0][i] = cube.back[0][i]
            new_back[0][i] = cube.left[0][i]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.left = MoveHelpers.transfert(cube.left, new_left)
        cube.right = MoveHelpers.transfert(cube.right, new_right)
        cube.back = MoveHelpers.transfert(cube.back, new_back)

        return cube

    
    def move_U_prime(self, cube: Cube) -> Cube:
        """ move Up face other way """
        for _ in range(3):
            cube = self.move_U(cube)
        return cube

    
    def move_U2(self, cube: Cube) -> Cube:
        """ move Up face twice """
        for _ in range(2):
            cube = self.move_U(cube)
        return cube
    
    
    def move_D(self, cube: Cube) -> Cube:
        """ move Down face """
        size: int = len(cube.up)
        cube.down = MoveHelpers.rotate(cube.down)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            new_front[size-1][i] = cube.left[size-1][i]
            new_left[size-1][i] = cube.back[size-1][i]
            new_right[size-1][i] = cube.front[size-1][i]
            new_back[size-1][i] = cube.right[size-1][i]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.left = MoveHelpers.transfert(cube.left, new_left)
        cube.right = MoveHelpers.transfert(cube.right, new_right)
        cube.back = MoveHelpers.transfert(cube.back, new_back)

        return cube

    
    def move_D_prime(self, cube: Cube) -> Cube:
        """ move Down face other way """
        for _ in range(3):
            cube = self.move_D(cube)
        return cube

    
    def move_D2(self, cube: Cube) -> Cube:
        """ move Down face twice """
        for _ in range(2):
            cube = self.move_D(cube)
        return cube
    
    
    def move_L(self, cube: Cube) -> Cube:
        """ move Left face """
        size: int = len(cube.left)
        cube.left = MoveHelpers.rotate(cube.left)

        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            new_front[i][0] = cube.up[i][0]
            new_down[i][0] = cube.front[i][0]
            new_back[i][0] = cube.down[i][0]
            new_up[i][size-1] = cube.back[i][size-1]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.up = MoveHelpers.transfert(cube.up, MoveHelpers.rotate_twice(new_up))
        cube.down = MoveHelpers.transfert(cube.down, new_down)
        cube.back = MoveHelpers.transfert(cube.back, MoveHelpers.rotate_twice(new_back))

        return cube

    
    def move_L_prime(self, cube: Cube) -> Cube:
        """ move Left face other way """
        for _ in range(3):
            cube = self.move_L(cube)
        return cube

    
    def move_L2(self, cube: Cube):
        """ move Left face twice """
        for _ in range(2):
            cube = self.move_L(cube)
        return cube
    
    
    def move_R(self, cube: Cube) -> Cube:
        """ move Right face """
        size: int = len(cube.right)
        cube.right = MoveHelpers.rotate(cube.right)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            new_front[i][size-1] = cube.down[i][size-1]
            new_up[i][size-1] = cube.front[i][size-1]
            new_back[i][size-1] = cube.up[i][size-1]
            new_down[i][0] = cube.back[i][0]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.up = MoveHelpers.transfert(cube.up, new_up)
        cube.back = MoveHelpers.transfert(cube.back, MoveHelpers.rotate_twice(new_back))
        cube.down = MoveHelpers.transfert(cube.down, MoveHelpers.rotate_twice(new_down))

        return cube

    
    def move_R_prime(self, cube: Cube) -> Cube:
        """ move Right face other way """
        for _ in range(3):
            cube = self.move_R(cube)
        return cube

    
    def move_R2(self, cube: Cube) -> Cube:
        """ move Right face twice """
        for _ in range(2):
            cube = self.move_R(cube)
        return cube
    
    
    def move_F(self, cube: Cube) -> Cube:
        """ move Front face """
        size: int = len(cube.front)
        cube.front = MoveHelpers.rotate(cube.front)

        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            new_up[i][size-1] = cube.left[i][size-1]
            new_left[0][i] = cube.down[0][i]
            new_right[size-1][i] = cube.up[size-1][i]
            new_down[i][0] = cube.right[i][0]

        cube.up = MoveHelpers.transfert(cube.up, MoveHelpers.rotate(new_up))
        cube.left = MoveHelpers.transfert(cube.left, MoveHelpers.rotate(new_left))
        cube.right = MoveHelpers.transfert(cube.right, MoveHelpers.rotate(new_right))
        cube.down = MoveHelpers.transfert(cube.down, MoveHelpers.rotate(new_down))

        return cube

    
    def move_F_prime(self, cube: Cube) -> Cube:
        """ move Front face other way """
        for _ in range(3):
            cube = self.move_F(cube)
        return cube

    
    def move_F2(self, cube: Cube) -> Cube:
        """ move Front face twice """
        for _ in range(2):
            cube = self.move_F(cube)
        return cube
