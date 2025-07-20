from solver_helpers.cube_algorithms import CubeAlgorithms


class PLLProcessor:
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
        
    def process(self, input_data: str) -> str:
        result: str = self.data[input_data] if input_data in self.data else "???"
        return result
