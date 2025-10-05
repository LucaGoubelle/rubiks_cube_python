""" w moves """
from pyrubik.data.cube import Cube, Face
from pyrubik.moves.moves import Moves

class WMoves(Moves):
    """ w moves """

    def move_Uw(self, cube: Cube, nb_layer:int = 2) -> Cube:
        """ move Up 2 layers face """
        size: int = len(cube.up)
        cube.up = self.rh.rotate(cube.up)

        new_front: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[j][i] = cube.right[j][i]
                new_left[j][i] = cube.front[j][i]
                new_right[j][i] = cube.back[j][i]
                new_back[j][i] = cube.left[j][i]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.left = self.rh.transfert(cube.left, new_left)
        cube.right = self.rh.transfert(cube.right, new_right)
        cube.back = self.rh.transfert(cube.back, new_back)

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
        cube.down = self.rh.rotate(cube.down)

        new_front: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[size - 1 - j][i] = cube.left[size - 1 - j][i]
                new_left[size - 1 - j][i] = cube.back[size - 1 - j][i]
                new_right[size - 1 - j][i] = cube.front[size - 1 - j][i]
                new_back[size - 1 - j][i] = cube.right[size - 1 - j][i]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.left = self.rh.transfert(cube.left, new_left)
        cube.right = self.rh.transfert(cube.right, new_right)
        cube.back = self.rh.transfert(cube.back, new_back)

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
        cube.left = self.rh.rotate(cube.left)

        new_up: Face = self.rh.gen_empty_face(size)
        new_front: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[i][j] = cube.up[i][j]
                new_down[i][j] = cube.front[i][j]
                new_back[i][j] = cube.down[i][j]
                new_up[i][size - 1 - j] = cube.back[i][size - 1 - j]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.up = self.rh.transfert(cube.up, self.rh.rotate_twice(new_up))
        cube.down = self.rh.transfert(cube.down, new_down)
        cube.back = self.rh.transfert(cube.back, self.rh.rotate_twice(new_back))

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
        cube.right = self.rh.rotate(cube.right)

        new_front: Face = self.rh.gen_empty_face(size)
        new_up: Face = self.rh.gen_empty_face(size)
        new_back: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_front[i][size - 1 - j] = cube.down[i][size - 1 - j]
                new_up[i][size - 1 - j] = cube.front[i][size - 1 - j]
                new_back[i][size - 1 - j] = cube.up[i][size - 1 - j]
                new_down[i][j] = cube.back[i][j]

        cube.front = self.rh.transfert(cube.front, new_front)
        cube.up = self.rh.transfert(cube.up, new_up)
        cube.back = self.rh.transfert(cube.back, self.rh.rotate_twice(new_back))
        cube.down = self.rh.transfert(cube.down, self.rh.rotate_twice(new_down))

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
        cube.front = self.rh.rotate(cube.front)

        new_up: Face = self.rh.gen_empty_face(size)
        new_left: Face = self.rh.gen_empty_face(size)
        new_right: Face = self.rh.gen_empty_face(size)
        new_down: Face = self.rh.gen_empty_face(size)

        for i in range(size):
            for j in range(nb_layer):
                new_up[i][size - 1 - j] = cube.left[i][size - 1 - j]
                new_left[j][i] = cube.down[j][i]
                new_right[size - 1 - j][i] = cube.up[size - 1 - j][i]
                new_down[i][j] = cube.right[i][j]

        cube.up = self.rh.transfert(cube.up, self.rh.rotate(new_up))
        cube.left = self.rh.transfert(cube.left, self.rh.rotate(new_left))
        cube.right = self.rh.transfert(cube.right, self.rh.rotate(new_right))
        cube.down = self.rh.transfert(cube.down, self.rh.rotate(new_down))

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
