""" OLL Scanner """
from pyrubik.data.cube import Cube
from solver_helpers.crown_scanner import CrownScanner
from solver_helpers.crown_caster import CrownCaster

class OLLScanner:
    """ 
    scanner for OLL (Orienting Last Layer) step 
    @author: LucaGoubelle
    """

    def __init__(self):
        self.caster = CrownCaster()
        self.scanner = CrownScanner()
    
    def scanOLL(self, cube: Cube) -> str:
        """
        scan the OLL config, return a string of binary numbers 
        based on "yellow" color or not
        @author: LucaGoubelle
        """
        crown = self.scanner.scan_crown(cube)
        result: str = self.caster.cast(crown)
        return result
