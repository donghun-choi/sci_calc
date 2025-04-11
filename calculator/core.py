# calculator/core.py
import math
from calculator.trig import sin, cos, tan, asin, acos, atan
from calculator.log_exp import log10, logx, square, power
from calculator.utils import factorial

def evaluate_expression(expr):
    safe_dict = {
        "pi": math.pi,
        "e": math.e,
        "sin": sin, "cos": cos, "tan": tan,
        "asin": asin, "acos": acos, "atan": atan,
        "log10": log10, "logx": logx,
        "x2": square, "xy": power,
        "fact": factorial
    }
    try:
        return eval(expr, {"__builtins__": {}}, safe_dict)
    except Exception as e:
        return f"Error: {e}"
