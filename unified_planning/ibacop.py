import os
from unified_planning import portfolio


class ibacop(portfolio.Portfolio):
    def __init__(self):
        super.__init__("ibacop")

    def extract_features(self, problem: str, domain: str, output_path: str) -> bool:
        current_path = os.path.dirname(__file__)
        print("\n***start extract features***\n")
        # features
        command = (
            "python2.7 "
            + current_path
            + "/features/translate/translate.py "
            + domain
            + " "
            + problem
        )
        print(command)
        os.system(command)

        command = (
            current_path
            + "/features/preprocess/preprocess < "
            + output_path
            + "/output.sas"
        )
        os.system(command)

        command = (
            current_path
            + "/features/ff-learner/roller3.0 -o "
            + domain
            + " -f "
            + problem
            + " -S 28"
        )
        os.system(command)

        command = (
            current_path + "/features/heuristics/training.sh " + domain + " " + problem
        )
        os.system(command)

        command = (
            current_path
            + '/search/downward --landmarks "lm=lm_merged([lm_hm(m=1),lm_rhw(),lm_zg()])" < '
            + output_path
            + "/output"
        )
        os.system(command)

        command = (
            current_path
            + "/search-mercury/downward ipc seq-agl-mercury <"
            + output_path
            + "/output"
        )
        os.system(command)

        # join file
        actual_rootpath = current_path + "/models"
        command = "python2.7 " + actual_rootpath + "/joinFile.py " + output_path
        os.system(command)

        print("\n***end extract features***\n")

        if os.path.isfile(output_path + "/global_features.arff"):
            return os.path.getsize(output_path + "/global_features.arff") != 0
        else:
            return False
