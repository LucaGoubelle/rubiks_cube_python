from pyrubik.data.cube import Cube


class Center5Seeker:
    """ center 5 seeker """
    
    def seek_center_edge(self, cube: Cube, face: str, color: str):
        hmap_front = {}
        hmap_front["front::up"] = cube.front[1][2]
        hmap_front["front::down"] = cube.front[3][2]
        hmap_front["front::right"] = cube.front[2][3]
        hmap_front["front::left"] = cube.front[2][1]

        hmap_up = {}
        hmap_up["up::front"] = cube.up[3][2]
        hmap_up["up::left"] = cube.up[2][1]
        hmap_up["up::right"] = cube.up[2][3]
        hmap_up["up::back"] = cube.up[1][2]

        hmap_back = {}
        hmap_back["back::up"] = cube.back[1][2]
        hmap_back["back::down"] = cube.back[3][2]
        hmap_back["back::right"] = cube.back[2][1]
        hmap_back["back::left"] = cube.back[2][3]

        hmap_down = {}
        hmap_down["down::front"] = cube.down[1][2]
        hmap_down["down::back"] = cube.down[3][2]
        hmap_down["down::left"] = cube.down[2][1]
        hmap_down["down::right"] = cube.down[2][3]
        
        if face=="front":
            for k,v in hmap_front.items():
                if(v==color): return k
        elif face=="up":
            for k,v in hmap_up.items():
                if(v == color): return k
        elif face=="back" :
            for k,v in hmap_back.items():
                if(v == color): return k
        elif face=="down" :
            for k,v in hmap_down.items():
                if(v == color): return k
        return "???"
    
    def seek_center_corner(self, cube: Cube, face: str, color: str):
        hmapFront = {}
        hmapFront["front::up::right"] = cube.front[1][3]
        hmapFront["front::up::left"] = cube.front[1][1]
        hmapFront["front::down::right"] = cube.front[3][3]
        hmapFront["front::down::left"] = cube.front[3][1]

        hmapUp = {}
        hmapUp["up::front::left"] = cube.up[3][1]
        hmapUp["up::front::right"] = cube.up[3][3]
        hmapUp["up::back::left"] = cube.up[1][1]
        hmapUp["up::back::right"] = cube.up[1][3]

        hmapBack = {}
        hmapBack["back::up::right"] = cube.back[1][1]
        hmapBack["back::up::left"] = cube.back[1][3]
        hmapBack["back::down::right"] = cube.back[3][1]
        hmapBack["back::down::left"] = cube.back[3][3]

        hmapDown = {}
        hmapDown["down::front::left"] = cube.down[1][1]
        hmapDown["down::front::right"] = cube.down[1][3]
        hmapDown["down::back::left"] = cube.down[3][1]
        hmapDown["down::back::right"] = cube.down[3][3]

        if face=="front":
            for k,v in hmapFront.items():
                if(v==color): return k
        elif face=="up":
            for k,v in hmapUp.items():
                if(v == color): return k
        elif face=="back":
            for k,v in hmapBack.items():
                if(v == color): return k
        elif face=="down":
            for k,v in hmapDown.items():
                if(v == color): return k
        return "???"
