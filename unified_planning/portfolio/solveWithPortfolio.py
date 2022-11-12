# 3. ESECUZIONE DI UN PORTFOLIO SU UNO SPECIFICO PROBLEMA
# Input. Un elenco ordinato di pianificatori integrati in UP, un tempo limite, un problema da risolvere
# Output. Un piano o fallimento
# Procedura. Eseguire nell’ordine i pianificatori indicati (suddividendo il CPU time limit equamente tra tutti)




# imports
# ---------------------------------------------
import os  # path
import sys  # argv, exit
import warnings
import unified_planning
# ---------------------------------------------

from unified_planning.shortcuts import *
# Function using the planners present in a given list to solve a given problem
def _solveWithPortfolio(plannerList, timeLimit, problem):
        """
        Returns the first `plan` found by a planner inside the `list` given.

        :param plannerList: List of planners to use
        :param timeLimit: Maximum time limit to run the operation
        :problem: Problem to be solved
        :return: First not null solution found, otherwise `None`
        """

        # Check if arguments are correct

        """Check if the `plannerList` is empty"""
        if not plannerList:
            print("ERROR::::Planner list is empty!")
            sys.exit(-1) 

        """Check if the `timeLimit` has an invalid value"""
        if timeLimit < 0:
            print("ERROR::::Invalid quantity of time assigned!")
            sys.exit(-1) 

        """Calculate time to allocate to each planner"""
        timeAllocated = timeLimit / (len(plannerList))

        print("******** LIST OF PLANNERS USED ********")
        print("**")

        for i in range(0,len(plannerList)):
            print("** #" + str(i+1) + " " + plannerList[i])

        print("**")
        print("** Time Allocated for each planner: ", timeAllocated)
        print("***************************************")    

        
        """Solve the `problem` with each planner inside the `list`"""
        for p in plannerList:
            with OneshotPlanner(name = p) as planner:
                    warnings.filterwarnings("error")
                    try:
                        result = planner.solve(problem, timeout=timeAllocated)

                        if result.plan is not None:
                            """Return the first `plan` found"""
                            print(f"{planner.name} found this plan: {result.plan}")
                            return result
                        else:
                            print(f"{planner.name} couldn't find a plan")
                        
                    except UserWarning:
                        print(UserWarning)

        # for p in plannerList:
        #     with OneshotPlanner(name = p) as planner:

        #         with warnings.catch_warnings(record=True) as caught_warnings:
        #             warnings.filterwarnings("always")
        #             result = planner.solve(problem, timeout=timeAllocated)
                    
        #             for warn in caught_warnings:
        #                 print(warn.message)

        #             if result.plan is not None:
        #                 """Return the first `plan` found"""
        #                 print(f"{planner.name} found this plan: {result.plan}")
        #                 return result
        #             else:
        #                 print(f"{planner.name} couldn't find a plan")
                    
"""Create default `problem` from Documentation to test the function"""
up.shortcuts.get_env().credits_stream = None 
x = Fluent("x")
a = InstantaneousAction("a")
a.add_precondition(Not(x))
a.add_effect(x, True)

problem = Problem("basic")
problem.add_fluent(x)
problem.add_action(a)
problem.set_initial_value(x, False)
problem.add_goal(x)      

result = _solveWithPortfolio(['enhsp','tamer','fast-downward'], 6, problem)
print(result.plan)        































