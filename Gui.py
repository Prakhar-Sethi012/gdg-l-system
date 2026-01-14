import tkinter as tk
import turtle


def generate(axiom, rules, iterations):
    current_str = axiom
    for i in range(iterations):
        pat = ""
        for j in current_str:
            pat += rules.get(j, j)
        current_str = pat
    return current_str


def parse_rules(rule_text):
    """
    Accepts rules in format:
      F:F+F--F+F
    OR multiple rules separated by commas:
      F:F+F--F+F,X:FX
    """
    rules = {}
    rule_text = rule_text.strip()
    if not rule_text:
        return rules

    parts = [p.strip() for p in rule_text.split(",") if p.strip()]
    for part in parts:
        if ":" not in part:
            raise ValueError("Rules must be in format Symbol:Replacement (e.g. F:F+F--F+F)")
        sym, repl = part.split(":", 1)
        sym = sym.strip()
        repl = repl.strip()
        if len(sym) != 1:
            raise ValueError("Rule symbol must be a single character (e.g. F)")
        rules[sym] = repl
    return rules


def main():
    root = tk.Tk()
    root.title("L-System Fractal Architect")
    root.geometry("1000x650")

    # ---------------- LEFT: CONTROL PANEL ----------------
    control_frame = tk.Frame(root, padx=10, pady=10)
    control_frame.pack(side=tk.LEFT, fill=tk.Y)

    tk.Label(control_frame, text="Input Dashboard",
             font=("Comic Sans MS", 14)).pack(pady=(0, 10))

    # Axiom
    tk.Label(control_frame, text="Axiom").pack(anchor="w")
    axiom_entry = tk.Entry(control_frame, width=30)
    axiom_entry.insert(0, "F")
    axiom_entry.pack(pady=3)

    # Rules
    tk.Label(control_frame, text="Rules (e.g. F:F+F--F+F)").pack(anchor="w")
    rule_entry = tk.Entry(control_frame, width=30)
    rule_entry.insert(0, "F:F+F--F+F")
    rule_entry.pack(pady=3)

    # Angle
    tk.Label(control_frame, text="Angle (degrees)").pack(anchor="w")
    angle_entry = tk.Entry(control_frame, width=30)
    angle_entry.insert(0, "60")
    angle_entry.pack(pady=3)

    # Iterations
    tk.Label(control_frame, text="Iterations").pack(anchor="w")
    iter_entry = tk.Entry(control_frame, width=30)
    iter_entry.insert(0, "4")
    iter_entry.pack(pady=3)

    # Step length
    tk.Label(control_frame, text="Step Length").pack(anchor="w")
    step_entry = tk.Entry(control_frame, width=30)
    step_entry.insert(0, "5")
    step_entry.pack(pady=3)

    status_label = tk.Label(control_frame, text="", fg="red",
                            wraplength=220, justify="left")
    status_label.pack(pady=(8, 0), anchor="w")

    # ---------------- RIGHT: CANVAS ----------------
    canvas_frame = tk.Frame(root, padx=10, pady=10)
    canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    tk.Label(canvas_frame, text="Turtle Canvas Area",
             font=("Comic Sans MS", 13)).pack(pady=(0, 8))

    canvas = tk.Canvas(canvas_frame, width=700, height=600, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")


    p = turtle.RawTurtle(screen)
    p.hideturtle()
    p.speed(0)
    p.setheading(90)

    def reset_turtle():
        p.clear()
        p.penup()
        p.home()
        p.setheading(90)
        p.pendown()

    def drawing(answer, angle, step):
        turtle.tracer(0, 0)

        stack = []
        for i in answer:
            if i == "F":
                p.forward(step)
            elif i == "+":
                p.right(angle)
            elif i == "-":
                p.left(angle)
            elif i == "[":
                stack.append((p.position(), p.heading()))
            elif i == "]":
                if stack:
                    pos, heading = stack.pop()
                    p.penup()
                    p.goto(pos)
                    p.setheading(heading)
                    p.pendown()

        turtle.update()

    def on_generate():
        status_label.config(text="")
        try:
            axiom = axiom_entry.get().strip()
            rules = parse_rules(rule_entry.get())
            angle = float(angle_entry.get())
            iterations = int(iter_entry.get())
            step = float(step_entry.get())

            if iterations < 0:
                raise ValueError("Iterations must be >= 0")
            if step <= 0:
                raise ValueError("Step length must be > 0")
            if not axiom:
                raise ValueError("Axiom cannot be empty")

            reset_turtle()
            result = generate(axiom, rules, iterations)
            drawing(result, angle, step)

        except Exception as e:
            status_label.config(text=str(e))

    tk.Button(control_frame, text="Generate",
              command=on_generate).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()
