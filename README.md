# gdg-l-system
# L-System Fractal Architect

## Overview
This project implements a Lindenmayer System (L-system) to generate fractal patterns using Python.  
The system expands an initial axiom using parallel rewriting rules and visualizes the result using turtle graphics.

This project is part of the GDG Club technical task.

## Goals
- Implement L-system string expansion
- Render generated strings using turtle graphics
- Build an interactive GUI using Tkinter
- Support branching structures using stack-based turtle state saving

## Tech Stack
- Python
- tkinter
- turtle

## Current Status
- Planning and project setup completed
## Implementation Progress

### Phase 1: L-system String Expansion
- Implemented parallel rewriting engine for L-systems
- Ensures all symbol replacements occur simultaneously
- Command-line based input and output

- ### Phase 2: Turtle Visualization
- Integrated L-system generator with turtle graphics
- Implemented standard L-system turtle commands (F, +, -)
- Verified visual output for fractal patterns
- Large iteration counts may impact performance due to exponential growth

- ###Phase 3 was a refactor step, not a new feature.

- ### Phase 4: Branching Support
- Implemented push/pop turtle state using a stack for `[` and `]`
- Restores turtle position and heading using penup/goto/setheading/pendown
- Enables tree-like and plant-like fractal structures



