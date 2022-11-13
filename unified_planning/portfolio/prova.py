from unified_planning.shortcuts import *
from unified_planning.io.pddl_writer import *
from unified_planning.io.pddl_reader import *
from unified_planning.engines.factory import *

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

engines: Dict[str, Tuple[str, str]] = DEFAULT_ENGINES
tempList = list(engines.keys())
plannerList = []
for p in tempList:
    try:
        with OneshotPlanner(name=p) as planner:
            if hasattr(planner, 'solve'):
                plannerList.append(p)
    except:
        pass

res = []
for p in plannerList:
    with OneshotPlanner(name=p) as planner:
        result = planner.solve(problem)
        toBeAppended = ","+ p + ", " + str(result.status in unified_planning.engines.results.POSITIVE_OUTCOMES)
        res.append(toBeAppended)
# with OneshotPlanner(name='fast-downward') as planner:
#     result = planner.solve(problem, timeout=5)
#     if result.status in unified_planning.engines.results.POSITIVE_OUTCOMES:
#         print(f"{planner.name} found this plan: {result.plan}")
#     else:
#         print("No plan found.")
print(res)