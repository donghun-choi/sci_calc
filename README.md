# SciCalc - Scientific Calculator (Console + GUI)

## 📌 Description

SciCalc is a two-stage scientific calculator project built with Python.

- Arithmetic operations
- Trigonometric functions (and their inverses)
- Logarithmic functions
- Exponents, roots, factorial
- Shift-mode toggling for extended operations
- A solver for quadratic and cubic equations

---

## Milestones

### 📍 Milestone 1: Console-Based Calculator

- Implemented all core math operations in console
- Used `eval()` safely with custom math context
- Functional modules created in `calculator/`
- Uploaded and tested on GitHub

### 📍 Milestone 2: GUI Scientific Calculator

- Built with **Tkinter** under `gui/`
- Fully interactive button-based interface
- **Shift button** toggles extended operations:
  - `cos → cos⁻¹`, `x² → x³`, `π → e`, `log10 → logx`, `√ → ³√`, `! → xy`
- `eqn` button provides popup interface to solve quadratic/cubic equations

---

## How to Run

### Console Version

```bash
python main.py
```

### GUI Version

```bash
python gui_main.py
```
