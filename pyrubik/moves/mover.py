""" mover class """
from pyrubik.data.cube import Cube
from pyrubik.exceptions.cube_mover_exception import CubeMoverException
from pyrubik.moves.axis_moves import AxisMoves
from pyrubik.moves.std_moves import STDMoves
from pyrubik.moves.wmoves import WMoves

class Mover:
    """ mover """

    def __init__(self):
        self.std_moves = STDMoves()
        self.axis_moves = AxisMoves()
        self.w_moves = WMoves()
    
    def simple_move(self, cube: Cube, mv:str) -> Cube:
        """ simple_move """
        match mv:
            case "U": cube = self.std_moves.move_U(cube)
            case "U'": cube = self.std_moves.move_U_prime(cube)
            case "U2": cube = self.std_moves.move_U2(cube)
            case "Uw": cube = self.w_moves.move_Uw(cube)
            case "Uw'": cube = self.w_moves.move_Uw_prime(cube)
            case "Uw2": cube = self.w_moves.move_Uw2(cube)
            case "Uww": cube = self.w_moves.move_Uw(cube, 3)
            case "Uww'": cube = self.w_moves.move_Uw_prime(cube, 3)
            
            case "D": cube = self.std_moves.move_D(cube)
            case "D'": cube = self.std_moves.move_D_prime(cube)
            case "D2": cube = self.std_moves.move_D2(cube)
            case "Dw": cube = self.w_moves.move_Dw(cube)
            case "Dw'": cube = self.w_moves.move_Dw_prime(cube)
            case "Dw2": cube = self.w_moves.move_Dw2(cube)
            case "Dww": cube = self.w_moves.move_Dw(cube, 3)
            case "Dww'": cube = self.w_moves.move_Dw_prime(cube, 3)
            
            case "L": cube = self.std_moves.move_L(cube)
            case "L'": cube = self.std_moves.move_L_prime(cube)
            case "L2": cube = self.std_moves.move_L2(cube)
            case "Lw": cube = self.w_moves.move_Lw(cube)
            case "Lw'": cube = self.w_moves.move_Lw_prime(cube)
            case "Lw2": cube = self.w_moves.move_Lw2(cube)
            case "Lww": cube = self.w_moves.move_Lw(cube, 3)
            case "Lww'": cube = self.w_moves.move_Lw_prime(cube, 3)
            
            case "R": cube = self.std_moves.move_R(cube)
            case "R'": cube = self.std_moves.move_R_prime(cube)
            case "R2": cube = self.std_moves.move_R2(cube)
            case "Rw": cube = self.w_moves.move_Rw(cube)
            case "Rw'": cube = self.w_moves.move_Rw_prime(cube)
            case "Rw2": cube = self.w_moves.move_Rw2(cube)
            case "Rww": cube = self.w_moves.move_Rw(cube, 3)
            case "Rww'": cube = self.w_moves.move_Rw_prime(cube, 3)
            
            case "F": cube = self.std_moves.move_F(cube)
            case "F'": cube = self.std_moves.move_F_prime(cube)
            case "F2": cube = self.std_moves.move_F2(cube)
            case "Fw": cube = self.w_moves.move_Fw(cube)
            case "Fw'": cube = self.w_moves.move_Fw_prime(cube)
            case "Fw2": cube = self.w_moves.move_Fw2(cube)
            case "Fww": cube = self.w_moves.move_Fw(cube, 3)
            case "Fww'": cube = self.w_moves.move_Fw_prime(cube, 3)

            case "y": cube = self.axis_moves.move_y(cube)
            case "y'": cube = self.axis_moves.move_y_prime(cube)
            case "y2": cube = self.axis_moves.move_y2(cube)

            case "x": cube = self.axis_moves.move_x(cube)
            case "x'": cube = self.axis_moves.move_x_prime(cube)
            case "x2": cube = self.axis_moves.move_x2(cube)

            case "z": cube = self.axis_moves.move_z(cube)
            case "z'": cube = self.axis_moves.move_z_prime(cube)
            case "z2": cube = self.axis_moves.move_z2(cube)
            
        return cube
    
    def multi_moves(self, cube: Cube, mvs:str) -> Cube:
        """ multi moves """
        try:
            move_lst = mvs.split(' ')
            for mv in move_lst:
                cube = self.simple_move(cube, mv)
            return cube
        except Exception as exc:
            raise CubeMoverException() from exc
