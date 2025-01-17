# Copyright 2022 AIPlan4EU project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from warnings import warn
import unified_planning as up
from enum import Enum, auto
from typing import IO, Optional, Callable


class OptimalityGuarantee(Enum):
    SATISFICING = auto()
    SOLVED_OPTIMALLY = auto()


class OneshotPlannerMixin:
    """Base class that must be extended by an :class:`~unified_planning.engines.Engine` that is also a `OneshotPlanner`."""

    def __init__(self):
        self.optimality_metric_required = False

    @staticmethod
    def is_oneshot_planner() -> bool:
        return True

    @staticmethod
    def satisfies(optimality_guarantee: OptimalityGuarantee) -> bool:
        """
        :param optimality_guarantee: The `optimality_guarantee` that must be satisfied.
        :return: `True` if the `OneshotPlannerMixin` implementation satisfies the given
        `optimality_guarantee`, `False` otherwise.
        """
        return False

    def solve(
        self,
        problem: "up.model.AbstractProblem",
        heuristic: Optional[
            Callable[["up.model.state.ROState"], Optional[float]]
        ] = None,
        timeout: Optional[float] = None,
        output_stream: Optional[IO[str]] = None,
    ) -> "up.engines.results.PlanGenerationResult":
        """
        This method takes a `AbstractProblem` and returns a `PlanGenerationResult`,
        which contains information about the solution to the problem given by the planner.

        :param problem: is the `AbstractProblem` to solve.
        :param heuristic: is a function that given a state returns its heuristic value or `None` if the state is a dead-end, defaults to `None`.
        :param timeout: is the time in seconds that the planner has at max to solve the problem, defaults to `None`.
        :param output_stream: is a stream of strings where the planner writes his
            output (and also errors) while it is solving the problem; defaults to `None`.
        :return: the `PlanGenerationResult` created by the planner; a data structure containing the :class:`~unified_planning.plans.Plan` found
            and some additional information about it.

        The only required parameter is `problem` but the planner should warn the user if `heuristic`,
        `timeout` or `output_stream` are not `None` and the planner ignores them.
        """
        assert isinstance(self, up.engines.engine.Engine)
        problem_kind = problem.kind
        if not self.skip_checks and not self.supports(problem_kind):
            msg = f"{self.name} cannot solve this kind of problem!"
            if self.error_on_failed_checks:
                raise up.exceptions.UPUsageError(msg)
            else:
                warn(msg)
        if not problem_kind.has_quality_metrics() and self.optimality_metric_required:
            msg = f"The problem has no quality metrics but the engine is required to be optimal!"
            raise up.exceptions.UPUsageError(msg)
        return self._solve(problem, heuristic, timeout, output_stream)

    def _solve(
        self,
        problem: "up.model.AbstractProblem",
        heuristic: Optional[
            Callable[["up.model.state.ROState"], Optional[float]]
        ] = None,
        timeout: Optional[float] = None,
        output_stream: Optional[IO[str]] = None,
    ) -> "up.engines.results.PlanGenerationResult":
        """Method called by the OneshotPlannerMixin.solve method."""
        raise NotImplementedError
