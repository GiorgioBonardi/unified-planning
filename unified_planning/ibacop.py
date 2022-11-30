import os
import unified_planning as up
from unified_planning import portfolio
from unified_planning.io.pddl_writer import PDDLWriter
from typing import List
import tempfile


class ibacop(portfolio.Portfolio):
    def __init__(self):
        super.__init__("ibacop")

    def extract_features(self, problem: "up.model.AbstractProblem") -> List[str]:
        current_path = os.path.dirname(__file__)
        # guarda riga 180 di ppdl_planner
        w = PDDLWriter(problem, True)
        with tempfile.TemporaryDirectory() as tempdir:
            domain_filename = os.path.join(tempdir, "domain.pddl")
            problem_filename = os.path.join(tempdir, "problem.pddl")
            w.write_domain(domain_filename)
            w.write_problem(problem_filename)

            # need to change the working dir for the following commands to work properly
            os.chdir(tempdir)
            print("\n***start extract features***\n")
            # features
            command = (
                current_path
                + "/features/preprocess/preprocess < "
                + tempdir
                + "/output.sas"
            )
            os.system(command)

            command = (
                current_path
                + "/features/ff-learner/roller3.0 -o "
                + domain_filename
                + " -f "
                + problem_filename
                + " -S 28"
            )
            os.system(command)

            command = (
                current_path
                + "/features/heuristics/training.sh "
                + domain_filename
                + " "
                + problem_filename
            )
            os.system(command)

            command = (
                current_path
                + '/search/downward --landmarks "lm=lm_merged([lm_hm(m=1),lm_rhw(),lm_zg()])" < '
                + tempdir
                + "/output"
            )
            os.system(command)

            command = (
                current_path
                + "/search-mercury/downward ipc seq-agl-mercury <"
                + tempdir
                + "/output"
            )
            os.system(command)
            command = (
                "python2.7 "
                + current_path
                + "/features/translate/translate.py "
                + domain_filename
                + " "
                + problem_filename
            )
            print(command)
            os.system(command)

            # join file
            actual_rootpath = current_path + "/models"
            command = "python2.7 " + actual_rootpath + "/joinFile.py " + tempdir
            os.system(command)

            print("\n***end extract features***\n")

            with os.path.join(tempdir, "global_features.arff") as file_features:
                return file_features.readlines()
