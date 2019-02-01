# Created by Ningxiang He, 01/30/2019

from map_color import map_color
from backtracking import Backtracking
import timeit

new_csp = map_color()  # create a csp map_color
search = Backtracking(True, True, True)
# define a class Backtracking.
# First parameter represents enable or disable Inference. True means enable. False means disable.
# Second parameter represents enable or disable MRV.
# Third parameter represents enable or disable LCV.

start_time = timeit.default_timer() # start the timer
solution = search.Backtracking_search(new_csp) # call Backtracking search function. Input csp
stop_time = timeit.default_timer() # stop the timer

print ("Run time is:\n", stop_time-start_time) # output run time
print ("The solution is:\n", solution) # print assignment
new_csp.show_result(solution) # print territory and color