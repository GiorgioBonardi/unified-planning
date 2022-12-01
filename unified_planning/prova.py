import os
from unified_planning.io import PDDLReader
from unified_planning.portfolio.portfolio import Portfolio

rootpath = os.path.dirname(__file__)
pathDomain = os.path.join(rootpath, "portfolio/domain")
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

portfolio = Portfolio()
try:
    result = portfolio.solve_with_portfolio(
        ["tamer", "fast-downward"], 30, parsed_problem
    )
    plan = result.plan
    print(f"PLAN FOUND:\n{plan}")
except:
    print("No planner could find a solution to the problem!")
