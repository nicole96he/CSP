# Created by Ningxiang He, 01/30/2019

from Circuit_board import Circuit_board
from backtracking import Backtracking
import timeit

cur_csp = Circuit_board() # create a csp circuit board
search = Backtracking(False, True, False)
# define a class Backtracking.
# First parameter represents enable or disable Inference. True means enable. False means disable.
# Second parameter represents enable or disable MRV.
# Third parameter represents enable or disable LCV.

start_time = timeit.default_timer() # start the timer
solution = search.Backtracking_search(cur_csp) # call Backtracking search function. Input csp
stop_time = timeit.default_timer() # stop the timer

print ("Run time is:\n", stop_time - start_time) # print run time
print ("The assignment is:\n", solution) # print assignment
cur_csp.show_result(solution) # print the board