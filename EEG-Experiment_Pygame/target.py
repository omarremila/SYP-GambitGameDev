import pygame as pg

pg.init()

class Target:
    # Class attributes.
    timer = 0
    size = 64

    # Constructor function.
    def __init__(self, screen):
        # Instance attributes.
        self.screen = screen

    # Draw target statically.
    def draw(self, x_pos, y_pos, colour):
        pg.draw.rect(self.screen, colour, (x_pos, y_pos, self.size, self.size), 2)

    def draw_x(self, x_pos, y_pos, colour):
        # Calculate the end points of the first line (top-left to bottom-right)
        start_pos1 = (x_pos, y_pos)
        end_pos1 = (x_pos + self.size, y_pos + self.size)

        # Calculate the end points of the second line (bottom-left to top-right)
        start_pos2 = (x_pos, y_pos + self.size)
        end_pos2 = (x_pos + self.size, y_pos)

        # Draw the first line
        pg.draw.line(self.screen, colour, start_pos1, end_pos1, width=2)

        # Draw the second line
        pg.draw.line(self.screen, colour, start_pos2, end_pos2, width=2)

    # Flicker target.
    def flicker(self, rate, x_pos, y_pos, colour):
        if self.timer >= rate:
            self.draw(x_pos, y_pos, colour)
            self.timer = 0
        else:
            self.timer +=1

                # Flicker target.
    def flicker_x(self, rate, x_pos, y_pos, colour):
        if self.timer >= rate:
            self.draw_x(x_pos, y_pos, colour)
            self.timer = 0
        else:
            self.timer +=1