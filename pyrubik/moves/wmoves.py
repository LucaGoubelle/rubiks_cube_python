""" w moves """
from pyrubik.data.cube import Cube
from pyrubik.moves.helpers.move_helpers import MoveHelpers, Face

class WMoves:
    """ w moves """

    def move_Uw(self, cube: Cube, nb_layer:int = 2) -> Cube:
        """ move Up 2 layers face """
        size: int = len(cube.up)
        cube.up = MoveHelpers.rotate(cube.up)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[j][i] = cube.right[j][i]
                new_left[j][i] = cube.front[j][i]
                new_right[j][i] = cube.back[j][i]
                new_back[j][i] = cube.left[j][i]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.left = MoveHelpers.transfert(cube.left, new_left)
        cube.right = MoveHelpers.transfert(cube.right, new_right)
        cube.back = MoveHelpers.transfert(cube.back, new_back)

        return cube

    
    def move_Uw_prime(self, cube: Cube, nb_layer:int = 2) -> Cube:
        """ move Up face 2 layer other way """
        for _ in range(3):
            cube = self.move_Uw(cube, nb_layer)
        return cube

    
    def move_Uw2(self, cube: Cube, nb_layer:int = 2) -> Cube:
        """ move Up face 2 layer twice """
        for _ in range(2):
            cube = self.move_Uw(cube, nb_layer)
        return cube

    
    def move_Dw(self, cube: Cube, nb_layer:int = 2) -> Cube:
        """ move Down face 2 layers """
        size: int = len(cube.up)
        cube.down = MoveHelpers.rotate(cube.down)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[size - 1 - j][i] = cube.left[size - 1 - j][i]
                new_left[size - 1 - j][i] = cube.back[size - 1 - j][i]
                new_right[size - 1 - j][i] = cube.front[size - 1 - j][i]
                new_back[size - 1 - j][i] = cube.right[size - 1 - j][i]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.left = MoveHelpers.transfert(cube.left, new_left)
        cube.right = MoveHelpers.transfert(cube.right, new_right)
        cube.back = MoveHelpers.transfert(cube.back, new_back)

        return cube

    
    def move_Dw_prime(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Down face 2 layers twice """
        for _ in range(3):
            cube = self.move_Dw(cube, nb_layer)
        return cube

    
    def move_Dw2(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Down face 2 layers twice """
        for _ in range(2):
            cube = self.move_Dw(cube, nb_layer)
        return cube

    
    def move_Lw(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Left face 2 layers """
        size: int = len(cube.left)
        cube.left = MoveHelpers.rotate(cube.left)

        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[i][j] = cube.up[i][j]
                new_down[i][j] = cube.front[i][j]
                new_back[i][j] = cube.down[i][j]
                new_up[i][size - 1 - j] = cube.back[i][size - 1 - j]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.up = MoveHelpers.transfert(cube.up, MoveHelpers.rotate_twice(new_up))
        cube.down = MoveHelpers.transfert(cube.down, new_down)
        cube.back = MoveHelpers.transfert(cube.back, MoveHelpers.rotate_twice(new_back))

        return cube

    
    def move_Lw_prime(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Left face 2 layers other way """
        for _ in range(3):
            cube = self.move_Lw(cube, nb_layer)
        return cube

    
    def move_Lw2(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Left face 2 layers twice """
        for _ in range(2):
            cube = self.move_Lw(cube, nb_layer)
        return cube


    
    def move_Rw(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Right face 2 layers """
        size: int = len(cube.right)
        cube.right = MoveHelpers.rotate(cube.right)

        new_front: Face = MoveHelpers.gen_empty_face(size)
        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_back: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[i][size - 1 - j] = cube.down[i][size - 1 - j]
                new_up[i][size - 1 - j] = cube.front[i][size - 1 - j]
                new_back[i][size - 1 - j] = cube.up[i][size - 1 - j]
                new_down[i][j] = cube.back[i][j]

        cube.front = MoveHelpers.transfert(cube.front, new_front)
        cube.up = MoveHelpers.transfert(cube.up, new_up)
        cube.back = MoveHelpers.transfert(cube.back, MoveHelpers.rotate_twice(new_back))
        cube.down = MoveHelpers.transfert(cube.down, MoveHelpers.rotate_twice(new_down))

        return cube

    
    def move_Rw_prime(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Right face 2 layers other way """
        for _ in range(3):
            cube = self.move_Rw(cube, nb_layer)
        return cube

    
    def move_Rw2(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Right face 2 layers twice """
        for _ in range(2):
            cube = self.move_Rw(cube, nb_layer)
        return cube

    
    def move_Fw(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Front face twice """
        size: int = len(cube.front)
        cube.front = MoveHelpers.rotate(cube.front)

        new_up: Face = MoveHelpers.gen_empty_face(size)
        new_left: Face = MoveHelpers.gen_empty_face(size)
        new_right: Face = MoveHelpers.gen_empty_face(size)
        new_down: Face = MoveHelpers.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_up[i][size - 1 - j] = cube.left[i][size - 1 - j]
                new_left[j][i] = cube.down[j][i]
                new_right[size - 1 - j][i] = cube.up[size - 1 - j][i]
                new_down[i][j] = cube.right[i][j]

        cube.up = MoveHelpers.transfert(cube.up, MoveHelpers.rotate(new_up))
        cube.left = MoveHelpers.transfert(cube.left, MoveHelpers.rotate(new_left))
        cube.right = MoveHelpers.transfert(cube.right, MoveHelpers.rotate(new_right))
        cube.down = MoveHelpers.transfert(cube.down, MoveHelpers.rotate(new_down))

        return cube

    
    def move_Fw_prime(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Front face 2 layers other way """
        for _ in range(3):
            cube = self.move_Fw(cube, nb_layer)
        return cube

    
    def move_Fw2(self, cube: Cube, nb_layer:int=2) -> Cube:
        """ move Front face 2 layers twice """
        for _ in range(2):
            cube = self.move_Fw(cube, nb_layer)
        return cube
