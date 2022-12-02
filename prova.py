import os
from unified_planning.io import PDDLReader
from unified_planning.portfolio.portfolio import Portfolio
from unified_planning.ibacop import Ibacop
from unified_planning.shortcuts import *

# permette di testare extract_features, a me(giorgio) funziona

rootpath = os.path.dirname(__file__)

# creation of problem
x = Fluent("x")

a = InstantaneousAction("a")
a.add_precondition(Not(x))
a.add_effect(x, True)

problem = Problem("basic")
problem.add_fluent(x)
problem.add_action(a)
problem.set_initial_value(x, False)
problem.add_goal(x)

reader = PDDLReader()
# problem = rootpath + "/domain/p01.pddl"
# domain = rootpath + "/domain/domain.pddl"
# parsed_problem = reader.parse_problem(domain, problem)

ibacop = Ibacop(["tamer", "lpg"], "")

features = ibacop.extract_features(problem)
print(features)
