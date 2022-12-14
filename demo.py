import os
from unified_planning.io import PDDLReader
from unified_planning.portfolio.portfolio import Portfolio
from unified_planning.ibacop import Ibacop
from unified_planning.shortcuts import *

# Set current working directory
rootpath = os.path.dirname(__file__)


# used for the creation of an up.AbstractProblem, not utilized here
# reader = PDDLReader()
# parsed_problem = reader.parse_problem(domain, problem)

# Input initializing for extract_feature function
# problem = rootpath + "/domain/p01.pddl"
# domain = rootpath + "/domain/domain.pddl"

# Creation of a default PDDL problem
x = Fluent("x")

a = InstantaneousAction("a")
a.add_precondition(Not(x))
a.add_effect(x, True)

problem = Problem("basic")
problem.add_fluent(x)
problem.add_action(a)
problem.set_initial_value(x, False)
problem.add_goal(x)

# Creation of ibacop specific portfolio
model_path = "RotationForest.model"
dataset_path = "global_features_simply.arff"
ibacop = Ibacop(
    os.path.join(rootpath, model_path),
    os.path.join(rootpath, dataset_path)
)

# Extraction of the features of a specific problem
features = ibacop.extract_features(
    problem=problem
)
print(
    f"The specific problem extracted presents the following features:\n\n{features}\n"
)

# Alternative extraction procedure
# features = ibacop.extract_features(parsed_problem)

print(
    "\nUse the features just extracted to predict whether the planners of the model solve the problem or not"
)
prediction_list = ibacop.get_prediction(features)
print(f"{prediction_list}")

available_planners = ["tamer", "enhsp", "fast-downward", "lpg"]
print(f"\nPlanners that we would potentially like to use: {available_planners}")

n = 2
print(f"\nNumber of maximum planners we want inside our portfolio: {n}")

print(
    "\nUse the problem and the pre-existing model to retrieve N planners from the ones available to us. Those N planners are to be used to solve the problem"
)
newPortfolio = ibacop.portfolio_specific_problem(available_planners, n, problem=problem)
print(f"\nThe portfolio contains the following planners: {newPortfolio}")

total_time_limit = 20
print(
    f"\nUse the new portfolio generated to solve the given specific problem with a time related constraint equal to: {total_time_limit}"
)

try:
    result = ibacop.solve_with_portfolio(newPortfolio, total_time_limit, problem)
    print(f"The result found for the problem is as follows:\n{result}")
except BaseException as e:
    print(e.with_traceback)
