##estrazione features per domain/problem
##far provare a risolvere il problema per gli N planner
##unire features + nomePlanner + true/false 
    ##si potrebbe modificare joinFile.py passandogli la lista dei planner e lista di true/false

import os               # path and process management
import sys              # argv, exit


#TODO: da aggiungere i limiti presenti in solve_agl?
def extract_features(original_domain, original_problem, rootpathOutput):
    print("\n***start extract features***\n")
    #features
    command = "python2.7 " + currentpath + "/features/translate/translate.py " + original_domain + " " + original_problem
    print(command)
    os.system(command)

    command =  currentpath + "/features/preprocess/preprocess < " + rootpathOutput + "/output.sas"
    os.system(command)
    
    command = currentpath + "/features/ff-learner/roller3.0 -o " + original_domain + " -f " + original_problem + " -S 28"
    os.system(command)

    command = currentpath + "/features/heuristics/training.sh "  + original_domain + " " + original_problem
    os.system(command)

    command = currentpath +"/search/downward --landmarks \"lm=lm_merged([lm_hm(m=1),lm_rhw(),lm_zg()])\" < " + rootpathOutput + "/output"
    os.system(command)

    command = currentpath + "/search-mercury/downward ipc seq-agl-mercury <" + rootpathOutput + "/output"
    os.system(command)

    #join file
    actual_rootpath = currentpath + "/models"
    command = "python2.7 "+ actual_rootpath + "/joinFile.py " + rootpathOutput
    os.system(command)

    print("\n***end extract features***\n")

#domain
#problem
#requestedPlanners = list of planners who support the problem
#n = max number of planner in the portfolio
#Output. Un elenco di N pianificatori ordinato
# Procedura. Estrarre le feature per P. 
# Invocare Weka con le feature estratte per ricavare la probabilità di successo dei vari pianificatori integrati in UP nel risolvere P. 
# Ordinare L sulla base della probabilità di successo. Restituire i primi N elementi di L

#TODO: Possible CHECK for existance of `domain` and `problem`
#TODO: Possible CHECK for `requestedPlanners` size to be >= n with n > 1 
def portfolio_specific_problem(domain, problem, requestedPlanners, n):
    """
        Returns the `list` of `planners` to be used to solve the given `problem`, sorted by probability of success.

        :param domain: `Domain` of the `problem` to be solved
        :param problem: `Problem` to be solved
        :param requestedPlanners: List of planners to use
        :param n: Number of `planners` to be used to solve the given `problem`
        
        :return: `List` of `planners` ordered by probability of success
        """
    
    """ Extracting `features` of the given `problem` """
    #TODO: Should be independent from this file
    extract_features(domain, problem, currentpath)

    #rimozione attributi 
    """ Call to `weka.jar` to remove unused `features` """
    command = "java -cp "+ currentpath +"/models/weka.jar -Xms256m -Xmx1024m weka.filters.unsupervised.attribute.Remove -R 1-3,18,20,65,78-79,119-120 -i "+ pathname + "/global_features.arff -o "+ pathname +"/global_features_simply.arff"
    os.system(command)
    #far predirre a weka
    #ottiene la lista dei pianificatori ordinata per probabilità di successo
    """ The `model` creates the `list` of ALL planners relative to their probability of solving the `problem` """
    command = "python2.7 "+ currentpath +"/models/parseWekaOutputFile.py "+   currentpath +"/outputModel " + currentpath +"/listPlanner"
    os.system(command)

    #analisi di listPlanner e tenere solo quelli presenti in requestedPlanners (forse inutile passare requestedPlanners?)
    #TODO: Possible to use listPlanner as a variable and not as a file?
    """ Create the `list` of `planners` from the file """
    with open(currentpath +"/listPlanner") as file:
        listPlanner = [next(file) for x in range(n)] #TODO: If we only take n from all planners, maybe we exclude some of the requested ones

    tempList = listPlanner
    #TODO: Model gives us a list of ALL the planners with their respective % of success
    # so if a planner has 0% it is still present, but maybe it isn't requested by input so it must be removed
    """ Removal of `planners` inside `listPlanner` that are not requested """
    for planner in listPlanner:
        if planner not in requestedPlanners:
            tempList.remove(planner)

    #TODO: Consider only the first `n` planners inside tempList

    return tempList #da togliere i vari \n

    

if __name__ == '__main__':
    pathname = os.getcwd()
    currentpath = os.path.abspath(pathname)
    truePlannerList = portfolio_specific_problem(currentpath + "/domain.pddl", currentpath + "/problem.pddl", [], 2)
    print(truePlannerList)
    # pathname = os.getcwd()
    # currentpath = os.path.abspath(pathname)
    # rootpath = os.path.abspath(os.path.join(currentpath,"..")) + "/training"
    # pathDomain = pathname + "/domain"
    # ##estrazione features per domain/problem
    # for dir in os.listdir(pathDomain):
    #     pathSpecificDomain = pathDomain + "/" + dir
    #     for i in range(1,2):
    #     #i = 1
    #     #for file in os.listdir(pathSpecificDomain):
    #         original_domain = pathSpecificDomain + "/p01-domain.pddl"
    #         original_problem = pathSpecificDomain + "/p"+str(i).zfill(2)+".pddl"
    #         currentpath = pathSpecificDomain + "/result"+str(i).zfill(2)

    #         if(os.path.isfile(original_problem)):
    #             if(not os.path.isdir(currentpath)):
    #                 os.mkdir(currentpath)
    #             os.chdir(currentpath)
    #             extract_features(original_domain, original_problem, currentpath)
    #             #i+=1

    # #creazione file "joined_global_features" unico
    # command = "python2.7 "+ pathname + "/join_globals.py " + pathname
    # print(command)
    # os.system(command)

    # #rimozione attributi 
    # command = "java -cp "+ rootpath +"/models/weka.jar -Xms256m -Xmx1024m weka.filters.unsupervised.attribute.Remove -R 1-3,18,20,65,78-79,119-120 -i "+ pathname + "/joined_global_features.arff -o "+ pathname +"/joined_global_features_simply.arff"
    # os.system(command)

    # #check result      
    # command = "java -Xmx1024M -cp " + pathname + "/models/weka.jar weka.classifiers.meta.RotationForest -t " + pathname +"/joined_global_features_simply.arff > " + pathname + "/output"
    # print(command)
    # os.system(command)

    # #saving model
    # command = "java -Xmx1024M -cp " + pathname + "/models/weka.jar weka.classifiers.meta.RotationForest  -t " + pathname + "/joined_global_features_simply.arff -d " + pathname + "/RotationForest.model"
    # print(command)
    # os.system(command)

    # # #comando che prende in ingresso il model (gia' allenato) e il train set utilizzati per avere una predizione in output nel file outputModel
    # # command = "java -Xms256m -Xmx1024m -cp "+ pathname +"/models/weka.jar weka.classifiers.meta.RotationForest -l "+pathname+"/RotationForest.model -T "+pathname+"/global_features_simply.arff -p 113 > "+pathname+"/outputModel"
    # # os.system(command)

    # # command = "python2.7 "+ pathname +"/models/parseWekaOutputFile.py "+pathname+"/outputModel "+pathname+"/listPlanner"
    # # os.system(command)


    # ##far provare a risolvere il problema per gli N planner

    # # planners = ["tamer", "enhsp", "pyperplan", "lgp"]

    # # for i in xrange(0, len(planners)):
    # #     planner = rootpath + "/" + planners[i] + "/plan"
    # #     run (planner, original_domain, original_problem, result, timeout)