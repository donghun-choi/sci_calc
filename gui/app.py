import tkinter as tk
from tkinter import simpledialog
from calculator.core import evaluate_expression
from calculator.solver import solve_quadratic, solve_cubic
import math

class SciCalcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SciCalc")
        self.shift = False

        self.display = tk.Entry(root, width=35, font=("Arial", 18), bd=5, justify='right')
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        self.shift_buttons = {}
        self.create_buttons()

    def add_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def evaluate(self):
        expr = self.display.get()
        result = evaluate_expression(expr)
        self.clear_display()
        self.add_to_display(str(result))

    def toggle_shift(self):
        self.shift = not self.shift
        self.update_shift_buttons()

    def update_shift_buttons(self):
        if self.shift:
            self.set_shift("cos", "acos(", "cos")
            self.set_shift("sin", "asin(", "sin")
            self.set_shift("tan", "atan(", "tan")
            self.set_shift("π", "e", "pi")
            self.set_shift("log", "logx(", "log10")
            self.set_shift("x2", "x3(", "x2")
            self.set_shift("√", "cbrt(", "sqrt")
            self.set_shift("!", "xy(", "fact")
        else:
            self.set_shift("cos", "cos(", "cos")
            self.set_shift("sin", "sin(", "sin")
            self.set_shift("tan", "tan(", "tan")
            self.set_shift("π", "π", "pi")
            self.set_shift("log", "log10(", "log10")
            self.set_shift("x2", "x2(", "x2")
            self.set_shift("√", "√(", "sqrt")
            self.set_shift("!", "fact(", "fact")

    def set_shift(self, key, new_text, value):
        btn = self.shift_buttons.get(key)
        if btn:
            btn.config(text=new_text, command=lambda: self.add_to_display(value + "(" if value.isalpha() else value))

    def solve_equation(self):
        choice = simpledialog.askstring("Equation Solver", "Type: quad or cubic")
        if choice == "quad":
            a = float(simpledialog.askstring("Quadratic", "a:"))
            b = float(simpledialog.askstring("Quadratic", "b:"))
            c = float(simpledialog.askstring("Quadratic", "c:"))
            result = solve_quadratic(a, b, c)
        elif choice == "cubic":
            a = float(simpledialog.askstring("Cubic", "a:"))
            b = float(simpledialog.askstring("Cubic", "b:"))
            c = float(simpledialog.askstring("Cubic", "c:"))
            d = float(simpledialog.askstring("Cubic", "d:"))
            result = solve_cubic(a, b, c, d)
        else:
            result = "Invalid input"
        self.clear_display()
        self.add_to_display(str(result))

    def create_buttons(self):
        btn_data = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),('(',1,4),(')',1,5),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),('π',2,4),('e',2,5),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),('x2',3,4),('log',3,5),
            ('0',4,0),('.',4,1),('!',4,2),('+',4,3),('sin',4,4),('cos',4,5),
            ('tan',5,0),('asin',5,1),('acos',5,2),('atan',5,3),('√',5,4),('=',5,5),
            ('Clear',6,0),('Shift',6,1),('eqn',6,2),
        ]

        for (text, row, col) in btn_data:
            if text == "=":
                cmd = self.evaluate
            elif text == "Clear":
                cmd = self.clear_display
            elif text == "Shift":
                cmd = self.toggle_shift
            elif text == "eqn":
                cmd = self.solve_equation
            else:
                val = text
                if text in ["π"]:
                    val = "pi"
                elif text == "x2":
                    val = "x2("
                elif text == "log":
                    val = "log10("
                elif text == "√":
                    val = "sqrt("
                elif text == "!":
                    val = "fact("
                elif text in ["sin", "cos", "tan", "asin", "acos", "atan"]:
                    val = text + "("
                cmd = lambda v=val: self.add_to_display(v)

            btn = tk.Button(self.root, text=text, width=6, height=2, font=("Arial", 14), command=cmd)
            btn.grid(row=row, column=col, padx=3, pady=3)

            if text in ["cos", "sin", "tan", "π", "log", "x2", "√", "!"]:
                self.shift_buttons[text] = btn
