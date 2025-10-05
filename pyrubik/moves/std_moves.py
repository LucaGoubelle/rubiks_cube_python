""" standard moves """
from pyrubik.data.cube import Cube, Face
from pyrubik.moves.moves import Moves

class STDMoves(Moves):
    """ standard moves """
    
    
    def move_U(self, cube: Cube) -> Cube:
        """ move Up face """
        size: int = len(cube.up)
        cube.up = self.rh.rotate(cube.up)

        new_front: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            new_front[0][i] = cube.right[0][i]
            new_left[0][i] = cube.front[0][i]
            new_right[0][i] = cube.back[0][i]
            new_back[0][i] = cube.left[0][i]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.left = self.rh.transfert(cube.left, new_left)
        cube.right = self.rh.transfert(cube.right, new_right)
        cube.back = self.rh.transfert(cube.back, new_back)

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
        cube.down = self.rh.rotate(cube.down)

        new_front: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            new_front[size-1][i] = cube.left[size-1][i]
            new_left[size-1][i] = cube.back[size-1][i]
            new_right[size-1][i] = cube.front[size-1][i]
            new_back[size-1][i] = cube.right[size-1][i]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.left = self.rh.transfert(cube.left, new_left)
        cube.right = self.rh.transfert(cube.right, new_right)
        cube.back = self.rh.transfert(cube.back, new_back)

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
        cube.left = self.rh.rotate(cube.left)

        new_up: Face = self.rh.gen_empty_face(size)
        new_front: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            new_front[i][0] = cube.up[i][0]
            new_down[i][0] = cube.front[i][0]
            new_back[i][0] = cube.down[i][0]
            new_up[i][size-1] = cube.back[i][size-1]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.up = self.rh.transfert(cube.up, self.rh.rotate_twice(new_up))
        cube.down = self.rh.transfert(cube.down, new_down)
        cube.back = self.rh.transfert(cube.back, self.rh.rotate_twice(new_back))

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
        cube.right = self.rh.rotate(cube.right)

        new_front: Face = self.rh.gen_empty_face(size)
        new_up: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            new_front[i][size-1] = cube.down[i][size-1]
            new_up[i][size-1] = cube.front[i][size-1]
            new_back[i][size-1] = cube.up[i][size-1]
            new_down[i][0] = cube.back[i][0]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.up = self.rh.transfert(cube.up, new_up)
        cube.back = self.rh.transfert(cube.back, self.rh.rotate_twice(new_back))
        cube.down = self.rh.transfert(cube.down, self.rh.rotate_twice(new_down))

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
        cube.front = self.rh.rotate(cube.front)

        new_up: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            new_up[i][size-1] = cube.left[i][size-1]
            new_left[0][i] = cube.down[0][i]
            new_right[size-1][i] = cube.up[size-1][i]
            new_down[i][0] = cube.right[i][0]

        cube.up = self.rh.transfert(cube.up, self.rh.rotate(new_up))
        cube.left = self.rh.transfert(cube.left, self.rh.rotate(new_left))
        cube.right = self.rh.transfert(cube.right, self.rh.rotate(new_right))
        cube.down = self.rh.transfert(cube.down, self.rh.rotate(new_down))

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
