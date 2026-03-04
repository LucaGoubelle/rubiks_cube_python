from solver_helpers.cube_algorithms import CubeAlgorithms
from solvers_cubes.solver2x2.processors.processor import Processor

class PLLProcessor(Processor):
    """ PLL Processor """
    
    def __init__(self):
        self.data = {
            # T cases
            "BR_GB_RG_OO" : CubeAlgorithms.T_PERM,
            "RG_0R_GO_BB" : CubeAlgorithms.T_PERM,
            "GO_BG_OB_RR" : CubeAlgorithms.T_PERM,
            "OB_RO_BR_GG" : CubeAlgorithms.T_PERM,

            # Y cases

            "BG_OR_GB_RO" : CubeAlgorithms.Y_PERM,
            "GB_RO_BG_OR" : CubeAlgorithms.Y_PERM,
            "RO_BG_OR_GB" : CubeAlgorithms.Y_PERM
        }
