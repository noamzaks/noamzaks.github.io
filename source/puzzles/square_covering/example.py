from manimlib.imports import *

class Example(Scene):
    def construct(self):
        # Create 3x3 squares
        one   = Square(fill_opacity=0.5, side_length=3, color=WHITE, fill_color=WHITE)
        two   = Square(fill_opacity=0.5, side_length=3, color=BLUE, fill_color=WHITE)
        three = Square(fill_opacity=0.5, side_length=3, color=RED, fill_color=WHITE)

        # Move 3x3 squares to position
        two.shift(2*DOWN+LEFT)
        three.shift(RIGHT)

        # Show the squares
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))
        
        # All grid 1x1 squares which an odd number of squares cover
        # Everything is relative to the center of the first square which is the origin
        odd_positions = [
            LEFT,
            LEFT+UP,
            2*RIGHT+UP,
            2*RIGHT,
            2*RIGHT+DOWN,
            2*DOWN,
            3*DOWN,
            3*DOWN+LEFT,
            3*DOWN+2*LEFT,
            2*DOWN+2*LEFT,
            DOWN+2*LEFT,
            2*DOWN+LEFT,
            DOWN
        ]

        # Show a yellow square in each odd position
        for position in odd_positions:
            show_odd = Square(side_length=1, fill_opacity=0.7, color=YELLOW)
            show_odd.move_to(position)
            self.play(ShowCreation(show_odd))
