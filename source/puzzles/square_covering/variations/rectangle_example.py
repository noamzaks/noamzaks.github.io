from manimlib.imports import *

class Example(Scene):
    def construct(self):
        # Create 2x3 rectangles
        one   = Rectangle(fill_opacity=0.5, height=2, width=3, color=WHITE, fill_color=WHITE)
        two   = Rectangle(fill_opacity=0.5, height=2, width=3, color=BLUE, fill_color=WHITE)
        three = Rectangle(fill_opacity=0.5, height=2, width=3, color=RED, fill_color=WHITE)

        # Move 2x3 rectangles to position
        # Notice that rectangles are created with their center on the origin so we do the following
        # Align left edge to the x = 0 line
        one.align_to(ORIGIN, LEFT)
        two.align_to(ORIGIN, LEFT)
        three.align_to(ORIGIN, LEFT)
        # Align bottom edges to the y = 0 line
        one.align_to(ORIGIN, DOWN)
        two.align_to(ORIGIN, DOWN)
        three.align_to(ORIGIN, DOWN)

        two.shift(DOWN+2*LEFT)
        three.shift(LEFT)

        # Show the rectangles
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))
        
        # All grid 1x1 squares which an odd number of squares cover
        # Everything is relative to the center of the first square which is the origin
        odd_positions = [
            2*RIGHT,
            2*RIGHT+UP,
            DOWN,
            DOWN+LEFT,
            DOWN+2*LEFT,
            2*LEFT,
            LEFT+UP,
            ORIGIN,
        ]

        # Show a yellow square in each odd position
        for position in odd_positions:
            show_odd = Square(side_length=1, fill_opacity=0.7, color=YELLOW)

            # Move to position
            show_odd.align_to(ORIGIN, LEFT)
            show_odd.align_to(ORIGIN, DOWN)

            show_odd.shift(position)
            self.play(ShowCreation(show_odd))
