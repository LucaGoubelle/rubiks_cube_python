""" draw megaminx """
from PIL import Image, ImageDraw


class MegaminxDrawer:
    """
    megaminx drawer
    @author: LucaGoubelle
    """

    def draw(self, minx):
        """
        draw a megaminx on PNG image
        @author: LucaGoubelle
        """
        img = Image.new("RGB", (800, 600), "#323232")
        img1 = ImageDraw.Draw(img)
        self._draw_body(img1)
        self._draw_up(img1, minx.up)
        self._draw_front(img1, minx.front)
        self._draw_left(img1, minx.left)
        self._draw_right(img1, minx.right)
        self._draw_down_left(img1, minx.down_left)
        self._draw_down_right(img1, minx.down_right)
        img.show()

    def _draw_body(self, img1: ImageDraw):
        img1.polygon([
            (123, 20), (193, 35), (230, 94), (237, 164), (192, 219),
            (129, 246), (61, 222), (17, 169), (19, 97), (57, 37)
        ], fill="black")

    def _draw_up(self, img1, face):
        img1.polygon([[123,21], [146,26], [125,31], [102,26]], fill=face[0][0])
        img1.polygon([[151,26], [159,29], [152,38], [130,32]], fill=face[0][1])
        img1.polygon([[166,29], [190,35], [183,45], [158,39]], fill=face[0][2])
        img1.polygon([[157,41], [182,47], [180,50], [150,50]], fill=face[0][3])
        img1.polygon([[148,53], [178,53], [172,63], [141,63]], fill=face[0][4])

        img1.polygon([[113,53], [141,53], [133,64], [123,64]], fill=face[0][5])
        img1.polygon([[76,54], [106,54], [116,64], [85,65]], fill=face[0][6])
        img1.polygon([[94,42], [103,51], [74,52], [71,48]], fill=face[0][7])
        img1.polygon([[83,31], [92,40], [69,46], [60,37]], fill=face[0][8])
        img1.polygon([[97,27], [119,33], [98,38], [89,29]], fill=face[0][9])

        img1.polygon([[125,33], [151,39], [143,51], [110,51], [100,40]], fill=face[1][0])

    def _draw_front(self, img1, face):
        img1.polygon([[85,69], [117,69], [107,99], [76,99]], fill=face[0][0])
        img1.polygon([[124,68], [133,68], [144,98], [114,98]], fill=face[0][1])
        img1.polygon([[140,68], [172,68], [182,98], [150,98]], fill=face[0][2])
        img1.polygon([[153,104], [185,104], [188,113], [163,132]], fill=face[0][3])
        img1.polygon([[190,120], [201,150], [175,169], [165,139]], fill=face[0][4])

        img1.polygon([[159,143], [170,173], [162,179], [136,161]], fill=face[0][5])
        img1.polygon([[131,165], [157,184], [131,203], [105,185]], fill=face[0][6])
        img1.polygon([[125,161], [100,181], [91,175], [101,144]], fill=face[0][7])
        img1.polygon([[95,141], [85,171], [59,152], [69,122]], fill=face[0][8])
        img1.polygon([[74,106], [106,105], [97,134], [71,115]], fill=face[0][9])

        img1.polygon([[112,105], [146,104], [158,136], [130,157], [102,137]], fill=face[1][0])

    def _draw_left(self, img1, face):
        img1.polygon([[56,40], [64,50], [50,71], [43,61]], fill=face[0][0])
        img1.polygon([[67,52], [70,56], [60,83], [52,74]], fill=face[0][1])
        img1.polygon([[72,58], [81,68], [71,98], [62,87]], fill=face[0][2])
        img1.polygon([[60,93], [69,105], [67,114], [52,120]], fill=face[0][3])
        img1.polygon([[64,122], [55,151], [41,156], [50,127]], fill=face[0][4])

        img1.polygon([[46,129], [38,158], [33,159], [34,133]], fill=face[0][5])
        img1.polygon([[31,135], [31,160], [18,165], [19,140]], fill=face[0][6])
        img1.polygon([[31,107], [31,129], [19,134], [19,126]], fill=face[0][7])
        img1.polygon([[32,79], [32,101], [20,120], [20,98]], fill=face[0][8])
        img1.polygon([[39,67], [48,77], [35,96], [35,73]], fill=face[0][9])

        img1.polygon([[49,79], [59,91], [49,121], [34,128], [34,101]], fill=face[1][0])

    def _draw_right(self, img1, face):
        img1.polygon([[176,66], [183,56], [193,84], [186,95]], fill=face[0][0])
        img1.polygon([[184,53], [187,50], [201,71], [194,82]], fill = face[0][1])
        img1.polygon([[188,47], [194,38], [207,59], [201,69]], fill = face[0][2])
        img1.polygon([[211,64], [215,70], [216,93], [204,74]], fill = face[0][3])
        img1.polygon([[217,76], [228,94], [231,116], [219,97]], fill=face[0][4])

        img1.polygon([[220,103], [232,122], [233,130], [222,125]], fill=face[0][5])
        img1.polygon([[223,131], [233,136], [236,161], [225,156]], fill = face[0][6])
        img1.polygon([[210,126], [220,130], [222,155], [219,153]], fill = face[0][7])
        img1.polygon([[194,119], [207,124], [216,153], [204,148]], fill = face[0][8])
        img1.polygon([[195,91], [204,117], [192,112], [189,102]], fill=face[0][9])

        img1.polygon([[196,88], [203,76], [217,98], [220,124], [207,118]], fill=face[1][0])

    def _draw_down_left(self, img1, face):
        img1.polygon([[57,157], [82,174], [67,179], [43,162]], fill=face[0][0])
        img1.polygon([[89,179], [96,184], [96,199], [74,183]], fill=face[0][1])
        img1.polygon([[103,189], [128,206], [127,220], [103,204]], fill=face[0][2])
        img1.polygon([[103,207], [127,224], [127,228], [103,220]], fill=face[0][3])
        img1.polygon([[103,223], [127,231], [127,244], [103,235]], fill=face[0][4])

        img1.polygon([[97,221], [97,233], [89,231], [75,213]], fill=face[0][5])
        img1.polygon([[48,204], [70,212], [84,228], [62,221]], fill=face[0][6])
        img1.polygon([[52,189], [66,207], [44,200], [38,194]], fill=face[0][7])
        img1.polygon([[32,165], [49,185], [35,188], [20,170]], fill=face[0][8])
        img1.polygon([[36,164], [40,163], [64,180], [52,184]], fill=face[0][9])

        img1.polygon([[70,184], [97,203], [97,217], [71,209], [55,189]], fill=face[1][0])

    def _draw_down_right(self, img1, face):
        img1.polygon([[204, 153], [215, 158], [191,177], [178,172]], fill=face[0][0])
        img1.polygon([[218, 159], [222, 161], [205,181], [194,177]], fill=face[0][1])
        img1.polygon([[224, 161], [234, 165], [219,185], [208,181]], fill=face[0][2])
        img1.polygon([[204, 186], [215, 189], [210,196], [190,204]], fill=face[0][3])
        img1.polygon([[186, 209], [206, 200], [191,218], [172,226]], fill=face[0][4])

        img1.polygon([[181, 211], [167,229], [160,231], [161,219]], fill=face[0][5])
        img1.polygon([[133, 231], [155,222], [154,234], [132,243]], fill=face[0][6])
        img1.polygon([[133, 223], [157,206], [156,218], [133,228]], fill=face[0][7])
        img1.polygon([[134, 206], [158,188], [157,202], [133,220]], fill=face[0][8])
        img1.polygon([[172, 177], [186,181], [163,197], [165,183]], fill=face[0][9])

        img1.polygon([[189, 181], [201, 185], [184, 207], [161, 216], [162, 202]], fill=face[1][0])

