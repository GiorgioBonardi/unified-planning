# 3. ESECUZIONE DI UN PORTFOLIO SU UNO SPECIFICO PROBLEMA
# Input. Un elenco ordinato di pianificatori integrati in UP, un tempo limite, un problema da risolvere
# Output. Un piano o fallimento
# Procedura. Eseguire nell’ordine i pianificatori indicati (suddividendo il CPU time limit equamente tra tutti)


# imports
# ---------------------------------------------
import os
import sys
from unified_planning.engines import ValidationResultStatus, results
from unified_planning.shortcuts import OneshotPlanner, PlanValidator
from unified_planning.io import PDDLReader
from multiprocessing import Process, Pipe

# ---------------------------------------------

# Custom Process class that supports solving of a `problem` with the given `planner` and sends the result through a Pipe estabilished connection
class SolverProcess(Process):
    def __init__(self, conn, planner, problem, **kwargs):
        Process.__init__(self, **kwargs)
        self._conn = conn
        self._planner = planner
        self._problem = problem

    # override the run function
    def run(self):
        try:
            result = self._planner.solve(self._problem)
            self._conn.send(result)
        except BaseException as e:
            # If the `solve` function of the planner raises an Exception, it is sent through the pipe to be handled elsewhere
            self._conn.send(e)


# Function using the planners present in a given list to solve a given problem
def _solveWithPortfolio(plannerList, timeLimit, problem):
    """
    Returns the first `plan` found by a planner inside the `list` given.

    :param plannerList: List of planners to use
    :param timeLimit: Maximum time limit to run the operation
    :param problem: Parsed problem to be solved
    :return: First not null `plan` found, otherwise `None`
    """
    # Check if arguments are correct

    # Check if the `plannerList` is empty
    assert plannerList, "Planner list is empty!"

    # Check if the `timeLimit` has an invalid value
    assert timeLimit > 0, "Invalid quantity of time assigned!"

    # Calculate time to allocate to each planner
    timeAllocated = timeLimit / (len(plannerList))

    print("\n******** LIST OF PLANNERS USED ***********")
    print("**")

    for i in range(0, len(plannerList)):
        print("** #" + str(i + 1) + " " + plannerList[i])

    print("**")
    print("** Time Allocated for each planner: ", timeAllocated)
    print("******************************************\n")

    # Solve the `problem` with each planner inside the `list`
    connMain, connSolver = Pipe()
    for p in plannerList:
        with OneshotPlanner(name=p) as planner:
            try:
                # Creating and starting solving sub-process
                proc = SolverProcess(connSolver, planner, problem)
                proc.start()

                # Wait for the sub-process to put its result into the Pipe, Time limit = `timeAllocated`
                if connMain.poll(timeAllocated):
                    # If the result is ready before Timeout, retrieve it from the pipe
                    result = connMain.recv()
                    # Check if the result is an exception, if True then raise it
                    if isinstance(result, BaseException):
                        raise result
                    proc.terminate()
                    proc.join()
                else:
                    # The sub-process couldn't finish excecution in time
                    print(f"{p} couldn't solve the problem with the time allocated!")
                    continue
            # Catch any exceptions
            except BaseException as e:
                proc.terminate()
                proc.join()
                print(
                    f"{p} has encountered an exception while attempting to solve the problem\nException:\n{e}"
                )
                continue

            plan = result.plan

            if plan is not None:
                # Validate the plan found
                print(f"{p} found this plan: {plan}")
                try:
                    with PlanValidator(problem_kind=problem.kind) as validator:
                        val = validator.validate(problem, plan)
                    print(val.status)
                    if val.status == ValidationResultStatus.VALID:
                        # Return the first correctly validated `plan`
                        return plan
                except:
                    print(
                        f"{p} has encountered an exception while attempting to validate the plan"
                    )
                    continue
            else:
                print(f"{p} couldn't find a plan")
    return None


rootpath = os.path.dirname(__file__)
pathDomain = os.path.join(rootpath, "domain")
##estrazione features per domain/problem
for dir in os.listdir(pathDomain):
    pathSpecificDomain = os.path.join(pathDomain, dir)
    for i in range(1, 2):
        # i = 1
        # for file in os.listdir(pathSpecificDomain):
        original_domain = os.path.join(
            pathSpecificDomain, "p" + str(i).zfill(2) + "-domain.pddl"
        )
        if not os.path.isfile(original_domain):
            original_domain = os.path.join(pathSpecificDomain, "domain.pddl")
        original_problem = os.path.join(
            pathSpecificDomain, "p" + str(i).zfill(2) + ".pddl"
        )
        currentpath = os.path.join(pathSpecificDomain, "result" + str(i).zfill(2))

        if os.path.isfile(original_problem):
            if not os.path.isdir(currentpath):
                os.mkdir(currentpath)
            os.chdir(currentpath)

print("PROBLEM: " + original_problem)
print("DOMAIN" + original_domain)
reader = PDDLReader()
parsed_problem = reader.parse_problem(original_domain, original_problem)

plan = _solveWithPortfolio(["tamer", "fast-downward"], 30, parsed_problem)

if plan is not None:
    print(f"PLAN FOUND:\n{plan}")
else:
    print("No planner could find a solution to the problem!")
