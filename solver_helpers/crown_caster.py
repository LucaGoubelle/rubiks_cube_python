""" crown caster """
from solver_helpers.crown_scanner import Crown

class CrownCaster:
    """ crown caster """

    
    def cast(self, crown: Crown) -> str:
        """ 
        cast crown data to a string of binary number
        1 if yellow, 0 if other color
        @author: LucaGoubelle
        """
        result: str = ""
        for row in crown:
            for elem in row:
                result += "1" if elem=="yellow" else "0"
            result += "_"
        return result
