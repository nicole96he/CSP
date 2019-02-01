# Created by Ningxiang He, 01/30/2019

class Circuit_board:
    def __init__(self):
        self.component = []
        self.component.append(["aaa", "aaa"])
        self.component.append(["bbbbb", "bbbbb"])
        self.component.append(["cc", "cc", "cc"])
        self.component.append(["eeeeeee"])
        self.graph = {0: [1, 2, 3],
                      1: [0, 2, 3],
                      2: [0, 1, 3],
                      3: [0, 1, 2]}
        list = []
        domin = []
        for var in range(0,4):
            size_x = len(self.component[var][0])
            size_y = len(self.component[var])
            for x in range(0, 10 - size_x + 1):
                for y in range(0, 3 - size_y + 1):
                    list.append((x,y))
            domin.append(list)
            list = []
        self.domin = domin

        original_grid = []
        for i in range(0,3):
            row = []
            for j in range(0,10):
                row.append("*")
            original_grid.append(row)

        self.original_grid = original_grid
        self.copy_domin = self.domin

    '''
        Purpose: test if current value of variable satisfies constraints or not
            Args: value, var, assignment, csp
            Returns: True or False
        '''
    def is_legal(self, value, var, assignment, csp):
        cur_size_x = len(csp.component[var][0])
        cur_size_y = len(csp.component[var])
        for key in assignment:
            if key==var:
                continue
            x = assignment[key][0] # x coordinate of a component
            y = assignment[key][1]
            size_x = len(csp.component[key][0])
            size_y = len(csp.component[key])
            if (cur_size_x + value[0]-1) < x or value[0] > (x + size_x-1) or (cur_size_y + value[1]-1) < y or value[1] > (y + size_y-1):
            # judge if two components overlap or not
                    continue
            return False
        return True

    '''
    Purpose: print nice board 
        Args: assignment
        Returns: None
    '''
    def show_result(self, assignment):
        for var in self.graph: # traverse all components
            x = assignment[var][0]
            y = assignment[var][1]
            size_x = len(self.component[var][0])
            size_y = len(self.component[var])
            for a in range(y,y + size_y):
                for b in range(x,x + size_x):
                    self.original_grid[2-a][b] = self.component[var][0][0]
                    # notice: in the board, lower left corner is (0,0),
                    # while in the printed list , higher corner is (0,0).
                    # So, y coordinate changes.

        print ("The solution is:")
        for i in range(0,3): # use two loops to print two-dimensional list
            for j in range(0,10):
                print (self.original_grid[i][j], end = '')
            print ("")