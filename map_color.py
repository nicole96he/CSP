# Created by Ningxiang He, 01/30/2019

class map_color:
    def __init__(self):
        self.domin = {}
        for var in range(0,7):
            self.domin[var] = [1,2,3]
            # 1 represents red, 2 represents green, 3 represents blue
        self.graph = {0: [1, 2],
                      1: [0, 2, 3],
                      2: [0, 1, 3, 4, 5],
                      3: [1, 2, 4],
                      4: [2, 3, 5],
                      5: [2, 4],
                      6: []}
        self.territory = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
        self.color = {1:"red",
                      2:"green",
                      3:"blue"}
        # self.color stores relationship between color and value
        self.copy_domin = self.domin # this is a back up domain used to recover domain

    '''
    Purpose: test if current value of variable satisfies constraints or not
        Args: value, var, assignment, csp
        Returns: True or False
    '''
    def is_legal(self, value, var, assignment, csp):
        for neighbor in csp.graph[var]:
            if neighbor in range(0, len(assignment)-1):
                if assignment[neighbor] == value: # if neighbor's color is same as oneself
                    return False
        return True

    def show_result(self,assignment):
        print("The colors of map are:")
        for var in assignment:
            print (self.territory[var], ":", end = '')
            print (self.color[assignment[var]])