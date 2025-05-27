from ventilastation.director import director, stripes
from ventilastation.scene import Scene
from ventilastation.sprites import Sprite


class Block(Sprite):
    def __init__(self, x, y, num_of_strip):
        super(Sprite, self).__init__()
        self.set_x(x * 8)
        self.set_y(16 + y * 8)
        self.set_strip(stripes["ventilatris.png"])
        self.set_frame(num_of_strip)



class Vortetris(Scene):
    stripes_rom = "vortetris"

    def on_enter(self):
        super(Vortetris, self).on_enter()
        self.blocks = []

        for i in range(0, 20, 2):
            for j in range(0, 20, 2):
                block = Block(i, j, 1)
                self.blocks.append(block)

    def step(self):      
        if director.was_pressed(director.BUTTON_D):
            self.finished()

    def finished(self):
        director.pop()
        raise StopIteration()


def main():
    return Vortetris()