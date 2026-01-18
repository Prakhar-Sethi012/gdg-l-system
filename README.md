#Gdg_Task-1
# L-System Fractal Architect

## Overview
This project implements a **Lindenmayer System (L-system)** to generate fractal patterns using Python.
An initial axiom is expanded using **parallel rewriting rules**, and the final string is visualized
using **turtle graphics**.

The final implementation provides an **interactive Tkinter GUI** with an embedded turtle canvas.

This project was developed as part of the **GDG Club technical task**.

---

## Goals
- Implement L-system string expansion using parallel rewriting
- Render generated strings using turtle graphics
- Build an interactive GUI using Tkinter
- Support branching structures using stack-based turtle state management

---

## Tech Stack
- Python
- tkinter
- turtle

---

## Implementation Progress

### Phase 1: L-system String Expansion
- Implemented parallel rewriting engine for L-systems
- Ensures all symbol replacements occur simultaneously
- Command-line based input and output

---

### Phase 2: Turtle Visualization
- Integrated L-system generator with turtle graphics
- Implemented standard L-system turtle commands:
  - `F` → move forward
  - `+` → turn right
  - `-` → turn left
- Verified visual output for fractal patterns
- Large iteration counts may impact performance due to exponential growth

---

### Phase 3: Refactoring
- Phase 3 was a refactor step focused on improving code structure
- No new user-facing features were added in this phase

---

### Phase 4: Branching Support
- Implemented push/pop turtle state using a stack for `[` and `]`
- Restores turtle position and heading using:
  - `penup()`
  - `goto()`
  - `setheading()`
  - `pendown()`
- Enables tree-like and plant-like fractal structures

---

### Phase 5: Tkinter GUI Integration
- Added a Tkinter-based GUI with an input dashboard
- Embedded turtle inside the Tkinter window using `RawTurtle`
- User-configurable inputs:
  - Axiom
  - Rules
  - Angle
  - Iterations
  - Step length
- Optimized rendering using `turtle.tracer(0, 0)` and `turtle.update()`

---

## Project Structure

- `lsystem_basic.py`  
  Core L-system string expansion logic using parallel rewriting.

- `lsystem_turtle_merge.py`  
  Command-line based turtle visualization integrating:
  - L-system expansion
  - Standard turtle commands (`F`, `+`, `-`)
  - Used for early visual validation.

- `Branching_Support.py`  
  Extended turtle renderer with stack-based branching support using:
  - `[` to push turtle state
  - `]` to restore turtle state  
  Enables tree-like and plant-like fractal structures.

- `FINAL_(Gui).py`  
  Final Tkinter GUI implementation:
  - Input dashboard for axiom, rules, angle, iterations, step length
  - Embedded turtle canvas using `RawTurtle`
  - Optimized rendering using `turtle.tracer(0, 0)`

- `Screenshots`
  ![Koch Fractal](https://github.com/Prakhar-Sethi012/gdg-l-system/blob/20a86ee34aafc182799278f304d9cf5f8125adaf/Koch_Style_Fractal.png)
  ![Tree Fractal](https://github.com/Prakhar-Sethi012/gdg-l-system/blob/20a86ee34aafc182799278f304d9cf5f8125adaf/Tree_Fractal.png)
  
  

- `README.md`  
  Project documentation and usage instructions.
---

## How to Run

### GUI Version (Recommended)
```bash
python FINAL_(Gui).py
