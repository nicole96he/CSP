# CSP
## Introduction
The objective of this lab is to create a general purpose solver for constraint satisfaction problems (CSPs). In this assignment, the two types of CSPs we will solve are the map coloring problem—in which adjacent states on a map must be colored with different colors—and the circuit board problem—in which components must be laid out on a circuit board such that they do not overlap.
This involves setting up a General CSP class that will hold many of the high-level code for a CSP problem. We also implement MapColoring and CircuitBoard classes that take the inputs corresponding to each and then translates them into the form of the generic CSP. In this case, the generic CSP class keeps track of variables, domains, and constraints, all in integer form. The pre-processing steps are accomplished in the more specialized CSP classes.
To find solutions to the CSPs, we implement a backtracking algorithm that operates in the environment of the integer values dictated by the general CSP class.

## readme
1. test_mapcolor.py
This python file is used to test map_coloring problem. Run this file.
2. test_circuitboard.py
This python file is used to test circuitboard problrm. Run this file
3. backtracking.py
This python file includes backtracking search function, Inference function, MRV heuristic and LCV heuristic.
4. map_color.py
This python file develops a framework that poses the map coloring problem as a CSP.
5. Circuit_board.py
This python file develops a framework that poses the circuit_board layout problem as a CSP.
