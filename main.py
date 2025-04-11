from calculator.core import evaluate_expression
from calculator.solver import solve_quadratic, solve_cubic

def main():
    print("Welcome to SciCalc! Type 'exit' to quit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        elif user_input == "quad":
            a, b, c = map(float, input("Enter a, b, c: ").split())
            print("Roots:", solve_quadratic(a, b, c))
        elif user_input == "cubic":
            a, b, c, d = map(float, input("Enter a, b, c, d: ").split())
            print("Roots:", solve_cubic(a, b, c, d))
        else:
            result = evaluate_expression(user_input)
            print("= ", result)

if __name__ == "__main__":
    main()
