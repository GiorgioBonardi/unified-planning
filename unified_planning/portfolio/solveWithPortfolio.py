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
from unified_planning.shortcuts import OneshotPlanner
from unified_planning.io import PDDLReader
from multiprocessing import Process, Queue 
# ---------------------------------------------

from unified_planning.shortcuts import *
# Function using the planners present in a given list to solve a given problem
def _solveWithPortfolio(plannerList, timeLimit, problem):
        """
        Returns the first `plan` found by a planner inside the `list` given.

        :param plannerList: List of planners to use
        :param timeLimit: Maximum time limit to run the operation
        :param problem: Parsed problem to be solved
        :return: First not null solution found, otherwise `None`
        """

        # Check if arguments are correct

        # Check if the `plannerList` is empty
        if not plannerList:
            print("ERROR::::Planner list is empty!")
            sys.exit(-1) 

        # Check if the `timeLimit` has an invalid value
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

        # Solve the `problem` with each planner inside the `list`
        q = Queue()
        for p in plannerList:
            with OneshotPlanner(name = p) as planner:
                    #warnings.filterwarnings("error")
                    try:
                        result = None
                        p = Process(target = lambda: q.put(planner.solve(problem)))
                        p.start()
                        result = q.get(block = True, timeout = timeAllocated)
   
                        if result.plan is not None:
                            # Return the first `plan` found
                            print(f"{planner.name} found this plan: {result.plan}")
                            return result
                        else:
                            print(f"{planner.name} couldn't find a plan")

                    except:
                        print(f"{planner.name} TIMED OUT")
                        p.terminate()
                        p.join()


rootpath = os.path.dirname(__file__)
pathDomain = os.path.join(rootpath, "domain")
##estrazione features per domain/problem
for dir in os.listdir(pathDomain):  
    pathSpecificDomain = os.path.join(pathDomain, dir)
    for i in range(1,2):
    #i = 1
    #for file in os.listdir(pathSpecificDomain):
        original_domain = os.path.join(pathSpecificDomain, "p"+str(i).zfill(2)+"-domain.pddl")
        original_problem = os.path.join(pathSpecificDomain, "p"+str(i).zfill(2)+".pddl")
        currentpath = os.path.join(pathSpecificDomain, "result"+str(i).zfill(2))

        if(os.path.isfile(original_problem)):
            if(not os.path.isdir(currentpath)):
                os.mkdir(currentpath)
            os.chdir(currentpath)

print("PROBLEM: " + original_problem)
print("DOMAIN" + original_domain)
reader = PDDLReader()
parsed_problem = reader.parse_problem(original_domain, original_problem)

result = _solveWithPortfolio(['tamer','enhsp','fast-downward'], 30, parsed_problem)

if(result is not None):
    print("\n\n\nPLAN FOUND:")
    print(result.plan) 
else:
    print("No planner could find a solution to the problem!")
       