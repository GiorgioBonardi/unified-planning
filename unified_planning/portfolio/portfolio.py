"""This module defines the portfolio interface."""

class Portfolio():
    """
    Represents the portfolio interface that must be implemented.
    """


    def __init__(self):
        #init
        pass

    def extract_features(
        self,
        problem: str,
        domain: str,
        path_output: str
    ) -> bool: #le facciamo ritornare un bool/niente/path di global_features.arff(?)/bo
        """
        Takes a problem, a filename and a map of renaming and returns the plan parsed from the file.
        Takes a problem path, a domain path and an output path and return a boolean indicating whether the extraction was successful 
        :param problem: The up.model.problem.Problem instance for which the plan is generated.
        :param problem: The path of the problem.
        :param domain: The path of the domain.
        :param path_output: The path of the output.
        :return: True if the extraction was succesfully made
        """

    def destroy(self):
        pass

    def __enter__(self):
        """Manages entering a Context (i.e., with statement)"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Manages exiting from Context (i.e., with statement)"""
        self.destroy()