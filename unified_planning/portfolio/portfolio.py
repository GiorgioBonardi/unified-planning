"""This module defines the portfolio interface."""
import unified_planning as up

# from unified_planning.engines import ValidationResultStatus
from unified_planning.shortcuts import OneshotPlanner  # , PlanValidator
from unified_planning.exceptions import UPException
from multiprocessing import Process, Pipe
from typing import List

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


class Portfolio:
    """
    Represents the portfolio interface that must be implemented.
    """

    # def __init__(self, name):
    #     self.name = name

    # @property
    # def name(self) -> str:
    #     """Returns the portfolio name."""
    #     return self._name

    # @name.setter
    # def name(self, name) -> str:
    #     self._name = name

    def extract_features(
        self, problem: "up.model.AbstractProblem"
    ) -> List[
        str
    ]:  # le facciamo ritornare un bool/niente/path o (VINCITORE) variabile che contiene global_features.arff(?)/bo
        """
        Takes a problem and returns a list of strings containing its features
        :param problem: The up.model.AbstractProblem instance from which to extract the features.
        :return: True if the extraction was succesfully made
        """

    def create_model(self, features: List[str]) -> str:  # o dataset?
        """
        Return the path to the model or None if some errors occurred
        """

    def get_prediction(
        self,
        features: List[str],  # o dataset?
        model_path,
    ) -> List[str]:
        """
        Takes a list of features and a model and returns a list of ALL planners relative to their probability of solving the `problem`
        (o si potrebbe tornare: the prediction of the model)
        """

    # primitiva 2
    def portfolio_specific_problem(
        self, problem, planners_requested, n_planners_allowed
    ):
        """
        Returns the `list` of `planners` to be used to solve the given `problem`, sorted by probability of success.

        :param domain: `Domain` of the `problem` to be solved
        :param problem: `Problem` to be solved
        :param planners_requested: List of 'planners' who support the 'problem'
        :param n_planners_allowed: Number of `planners` allowed in the portfolio

        :return: `List` of `planners` ordered by probability of success
        """
        assert isinstance(problem, up.model.Problem)
        assert n_planners_allowed > 1, "at least one planner is required"
        assert (
            planners_requested >= n_planners_allowed
        ), "the list of planners must be grater or equal to the number of planners"

        list_planners = []
        # Extracting `features` of the given `problem`
        features = self.extract_features(problem)
        model_path = self.create_model(features)
        model_prediction_list = self.get_prediction(
            features, model_path
        )  # nome variabile mhe

        x = 0
        for line in model_prediction_list:
            line = line.strip()
            if line in planners_requested:
                list_planners.append(line)
                x += 1
            if x == n_planners_allowed:
                break

        return list_planners

    # primitive 2
    # Function using the planners present in a given list to solve a given problem
    def solve_with_portfolio(
        self,
        plannerList: List[str],
        timeLimit: int,
        problem: "up.model.AbstractProblem",
    ) -> "up.engines.results.PlanGenerationResult":
        """
        Returns the first `result` found by a planner inside the `list` given.

        :param plannerList: List of planners to use
        :param timeLimit: Maximum time limit to run the operation
        :param problem: Parsed problem to be solved
        :return: First not null `result` found, otherwise `None`
        """

        assert plannerList, "Planner list is empty!"
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
                        return result
                    else:
                        # The sub-process couldn't finish excecution in time
                        print(
                            f"{p} couldn't solve the problem with the time allocated!"
                        )
                        continue
                # Catch any exceptions
                except BaseException as e:
                    proc.terminate()
                    proc.join()
                    print(
                        f"{p} has encountered an exception while attempting to solve the problem\nException:\n{e}"
                    )
                    continue

                # if plan is not None:
                #     # Validate the plan found
                #     print(f"{p} found this plan: {plan}")
                #     try:
                #         with PlanValidator(problem_kind=problem.kind) as validator:
                #             val = validator.validate(problem, plan)
                #         print(val.status)
                #         if val.status == ValidationResultStatus.VALID:
                #             # Return the first correctly validated `plan`
                #             return result
                #     except:
                #         print(
                #             f"{p} has encountered an exception while attempting to validate the plan"
                #         )
                #         continue
                # else:
                #     print(f"{p} couldn't find a plan")
        raise UPException("Portfolio failed to find a plan")

    def destroy(self):
        pass

    def __enter__(self):
        """Manages entering a Context (i.e., with statement)"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Manages exiting from Context (i.e., with statement)"""
        self.destroy()
