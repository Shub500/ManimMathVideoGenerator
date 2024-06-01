from manim import *


class PEMDASExplanation(Scene):
    def construct(self):
        # Write the expression to be evaluated
        expression = MathTex(
            "2", "+", "3", "\\times", "(", "4", "+", "1", ")", color=WHITE
        )
        expression.scale(2)
        expression.to_edge(UP)

        # Highlighting the part in parentheses
        parentheses_group = VGroup(
            expression[4], expression[5], expression[6], expression[7], expression[8]
        )
        parentheses_group.set_color(YELLOW)

        # Explain PEMDAS rule
        pemdas_rule = Text(
            "PEMDAS Rule: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction",
            font_size=24,
        )
        pemdas_rule.to_edge(DOWN)

        # Add all to the scene
        self.play(Write(expression))
        self.wait(1)
        self.play(Write(pemdas_rule))
        self.wait(1)

        # Step 1: Solve inside the parentheses
        self.play(parentheses_group.animate.set_color(BLUE))
        self.wait(1)
        inside_result = MathTex("5", color=BLUE)
        inside_result.move_to(parentheses_group.get_center())
        self.play(Transform(parentheses_group, inside_result))

        # Step 2: Perform multiplication
        times = expression[3]
        self.play(times.animate.set_color(RED))
        self.wait(1)
        multiplication_result = MathTex("15", color=RED)
        multiplication_group = VGroup(expression[2], expression[3], inside_result)
        multiplication_result.move_to(multiplication_group.get_center())
        self.play(Transform(multiplication_group, multiplication_result))

        # Step 3: Perform addition
        plus = expression[1]
        self.play(plus.animate.set_color(GREEN))
        self.wait(1)
        final_result = MathTex("17", color=GREEN)
        final_group = VGroup(expression[0], plus, multiplication_result)
        final_result.move_to(final_group.get_center())
        self.play(Transform(final_group, final_result))

        # Final result displayed
        self.wait(2)
        self.play(FadeOut(final_group), FadeOut(pemdas_rule))

        # Conclusion text
        conclusion_text = Text(
            "Always follow the PEMDAS rules!", font_size=36, color=BLUE
        )
        conclusion_text.to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(2)
