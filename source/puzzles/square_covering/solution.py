from manimlib.imports import *

class Solution(Scene):
    def construct(self):
        # We can't draw the entire plane, but let's color a 9x9 grid.
        colors = [
            [ORANGE, RED, BLUE],
            [TEAL, GREEN, YELLOW],
            [GOLD, PURPLE, MAROON]
        ]
        # We want to show all 81 animations at once
        animations = []
        # and keep our grid
        grid = []

        for i in range(9):
            row = []
            for j in range(9):
                FACTOR = 0.75
                square = Square(fill_opacity=0.7, color=colors[i % 3][j % 3], stroke_width=0, side_length=FACTOR)
                square.shift(FACTOR * (i * RIGHT + j * UP - 4*(RIGHT + UP))) # Move everything so it is centered.
                row.append(square)
                animations.append(ShowCreation(square))
            grid.append(row)

        self.play(*animations)

        # Create 3x3 squares
        one   = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=WHITE, fill_color=WHITE)
        two   = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=BLUE, fill_color=WHITE)
        three = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=RED, fill_color=WHITE)

        # Move 3x3 squares to position
        two.shift(FACTOR*(2*DOWN+LEFT))
        three.shift(FACTOR*(RIGHT))

        # Show the squares
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))

        # Hide all squares which aren't colored some color
        animations = []
        for i in range(9):
            for j in range(9):
                if not (i % 3 == 0 and j % 3 == 0):
                    animations.append(FadeOut(grid[i][j]))
        self.play(*animations)

        # Hide all squares but the one which is covered only by the red 3x3 square
        animations = []
        for i in range(9):
            for j in range(9):
                if (i % 3 == 0 and j % 3 == 0) and not (i == 6 and j == 3):
                    animations.append(FadeOut(grid[i][j]))
        self.play(*animations)