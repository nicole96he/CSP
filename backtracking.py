# Created by Ningxiang He, 01/30/2019

import queue

class Backtracking:
    def __init__(self, do_inference = False, do_MRV = False, do_LCV = False):
        self.do_inference = do_inference
        self.do_MRV = do_MRV
        self.do_LCV = do_LCV

    def Backtracking_search(self, csp):
        assignment = {}
        return self.Backtrack(assignment, csp)

    '''
    Purpose: Backtracking 
        Args: assignment, csp
        Returns: assignment or failure
    '''
    def Backtrack(self,assignment, csp):
        if self.goal_test(assignment, csp):   # judge if a solution has finished
            return assignment  # if a solution has finished, return assignment

        var = self.MRV_heuristic(assignment, csp, self.do_MRV)
        # pick a variable to assign value.

        for value in self.LCV_heuristic(var, assignment, csp, self.do_LCV):
            # traverse all possible value for variable
            assignment[var] = value
            if csp.is_legal(value,var,assignment,csp): # if value satisfies constraints
                assignment[var] = value  # put the variable-value into assignment
                inferences = self.Inference(csp, var, assignment, self.do_inference) # call inference
                if inferences != False:
                    result = self.Backtrack(assignment,csp)
                    if result != None:
                        return result
            del assignment[var] # recover
            self.recover_domin(assignment,csp) # recover the domain, which has been revised
        return None

    '''
    Purpose: test if a solution has been accomplished or not
        Args: assignment
        Returns: True or False
    '''
    def goal_test(self, assignment, csp):
        if len(assignment) == len(csp.graph):
            return True
        return False

    '''
    Purpose: MAC-3
        Args: csp, Xi, assignment, do_inference
        Returns: True or False
    '''
    def Inference(self, csp, Xi, assignment, do_inference):
        if do_inference == False: # If we disable inference
            return True
        arcs = queue.Queue() # create a queue
        for Xj in csp.graph[Xi]: # use loop to put pairs into queue
            if Xj in assignment:
                continue
            arcs.put((Xi,Xj))

        while not arcs.empty(): # loop when there is pairs in queue
            cur_arc = arcs.get() # pop first element

            if self.Revise(csp,cur_arc): # judge if domain has been revised or not
                if len(csp.domin[cur_arc[0]]) == 0: # if one of domain is empty
                    return False
                for neighbor in csp.graph[cur_arc[0]]: # traverse all neighbors of Xi
                    if neighbor is not cur_arc[1]: # do not traverse Xj
                        arcs.put((neighbor, cur_arc[0])) # push pair into queue
        return True

    '''
    Purpose: revise domain
        Args: csp, Xi, Xj
        Returns: True or False
    '''
    def Revise(self,csp,cur_arc):
        revised = False
        Xi = cur_arc[0]
        Xj = cur_arc[1]
        for value_x in csp.domin[Xi]: # traverse value in domain
            count = 0
            for value_y in csp.domin[Xj]:
            #if no value y in Dj allows (x,y) to satisfy the constraint between Xi and Xj
                if value_x == value_y:
                    count += 1
            if count == len(csp.domin[Xj]):
                csp.domin[cur_arc[0]].remove(value_x)  # delete value_x from Di
                revised = True
        return revised

    '''
    Purpose: MRV heuristic
        Args: assignment, csp, do_MRV
        Returns: variable
    '''
    def MRV_heuristic(self, assignment, csp, do_MRV):
        if do_MRV == False: # if we disable MRV heuristic
            next_var = len(assignment) # return variable in natural order
            return next_var
        domin_size = 100
        for var in range(0,len(csp.graph)):
            if var not in assignment: # if var is unassigned
                if domin_size > len(csp.domin[var]): # compare domain size
                    domin_size = len(csp.domin[var]) # store smaller domain size
                    next_var = var # choose variable with smaller domain size
        return next_var

    '''
    Purpose：LCV heuristic
        Args: variable, assignment, csp, do_LCV
        Returns: a list of variable
    '''
    def LCV_heuristic(self, var, assignment, csp, do_LCV):
        if do_LCV == False: # if we disable LCV heuristic
            return csp.domin[var]
        order = csp.domin[var]
        cur_ruleout = 0
        rule_out = {}
        for value in csp.domin[var]:  # calculate number of values that will be rule out by this value
            for neighbor in csp.graph[var]:
                if neighbor not in assignment:
                    for nei_val in csp.domin[neighbor]:
                        if value == nei_val:
                            cur_ruleout  += 1
            rule_out[value] = cur_ruleout
            # store number of rule out and value into a dictionary.
            cur_ruleout = 0

        for i in range(0,len(order)-2): # use two loop to sort value according to rule out
            for j in range(i+1,len(order)-1):
                if rule_out[order[i]] > rule_out[order[j]]:
                    c = order[i]
                    order[i] = order[j]
                    order[j] = c
        return order

    '''
    Purpose: recover the domain which has been revised 
        Args: assignment, csp
        Returns: None
    '''
    def recover_domin(self, assignment, csp):
        for var in csp.graph:
            if var not in assignment: # only revise domain of variables which has not been assigned
                csp.domin[var] = csp.copy_domin[var]
        return None

