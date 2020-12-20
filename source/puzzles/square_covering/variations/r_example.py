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

        # Here's an easter egg - did you know that e=π=3?
        two.shift(np.pi/2*DOWN+np.e*LEFT)
        three.shift(math.sqrt(np.e)*LEFT)

        # Show the rectangles
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))

        # I found no better way than brute force to do this (at least we have align_to)
        # but manim is fun nontheless :D
        r1 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=2, width=math.sqrt(np.e))
        r1.align_to(three, RIGHT)
        r1.shift(math.sqrt(np.e) * RIGHT)
        r1.align_to(one, DOWN)

        self.play(ShowCreation(r1))

        r2 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=np.pi/2, width=math.sqrt(np.e))
        r2.align_to(three, LEFT)
        r2.align_to(two, DOWN)
        r2.shift(2*UP)

        self.play(ShowCreation(r2))

        r3 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=np.pi/2, width=3)
        r3.align_to(two, LEFT)
        r3.align_to(two, DOWN)

        self.play(ShowCreation(r3))

        r4 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=(2 - np.pi/2), width=(np.e - math.sqrt(np.e)))
        r4.align_to(two, LEFT)
        r4.align_to(two, UP)

        self.play(ShowCreation(r4))

        r5 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=(2 - np.pi/2), width=(3 - np.e))
        r5.align_to(ORIGIN, LEFT)
        r5.align_to(ORIGIN, DOWN)

        self.play(ShowCreation(r5))
