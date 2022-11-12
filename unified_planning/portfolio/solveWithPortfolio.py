# 3. ESECUZIONE DI UN PORTFOLIO SU UNO SPECIFICO PROBLEMA
# Input. Un elenco ordinato di pianificatori integrati in UP, un tempo limite, un problema da risolvere
# Output. Un piano o fallimento
# Procedura. Eseguire nell’ordine i pianificatori indicati (suddividendo il CPU time limit equamente tra tutti)




# imports
# ---------------------------------------------
import os  # path
import sys  # argv, exit

# ---------------------------------------------
import unified_planning
from unified_planning.io.pddl_reader import *
from unified_planning.io.pddl_writer import *
from unified_planning.shortcuts import *


 # function 3
def _solveWithPortfolio(plannerList, timeLimit, problem):
    
        # Check if all arguments are correct
        if not plannerList:
            print("ERROR::::Planner list is empty!")
            sys.exit(-1) 

        if timeLimit < 0:
            print("ERROR::::Invalid quantity of time assigned!")
            sys.exit(-1) 

        # Calculate time to allocate to each planner
        timeAllocated = timeLimit / (len(plannerList))

        print("******** LIST OF PLANNERS USED ********")
        print("**")

        for i in range(0,len(plannerList)):
            print("** #" + str(i+1) + " " + plannerList[i])

        print("**")
        print("** Time Allocated for each planner: ", timeAllocated)
        print("***************************************")    

        for p in plannerList:
            with OneshotPlanner(name = p) as planner:
                result = planner.solve(problem, timeout=timeAllocated)
                print(f"{planner.name} found this plan: {result.plan}")
        
        return result

# if __name__ == '__main__':
x = Fluent("x")

a = InstantaneousAction("a")
a.add_precondition(Not(x))
a.add_effect(x, True)

problem = Problem("basic")
problem.add_fluent(x)
problem.add_action(a)
problem.set_initial_value(x, False)
problem.add_goal(x)

plan = _solveWithPortfolio(['enhsp'], 5, problem)

print(plan)































