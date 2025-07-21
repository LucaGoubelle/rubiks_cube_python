""" sticker drawer """


class IMGStickerDrawer:
    """
    sticker drawer
    @author: LucaGoubelle
    """

    def draw_front_sticker(self, img1, x,y, elem, size=50):
        """
        draw a front (flat) sticker
        @author: LucaGoubelle
        """
        img1.polygon([(x, y), (x+size, y), (x+size, y+size), (x, y+size)], fill=elem, outline="black")

    def draw_right_sticker(self, img1, x, y, elem, size=50):
        """
        draw a right sticker
        @author: LucaGoubelle
        """
        half = size // 2
        img1.polygon([(x, y), (x+half, y-half), (x+half, y-half+size), (x, y+size)], fill=elem, outline="black")

    def draw_up_sticker(self, img1, x, y, elem, size=50):
        """
        draw a up sticker
        @author: LucaGoubelle
        """
        half = size // 2
        img1.polygon([(x, y), (x+size, y), (x+size-half, y+half), (x-half, y+half)], fill=elem, outline="black")
