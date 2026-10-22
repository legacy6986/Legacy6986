trixie292206021957
Repository navigation
Code
Issues
2
 (2)
Pull requests
1
 (1)
Discussions
trixie292206021957/gemini/deepmind.gemini
/google-ai_tracking.py
rickyplambert-seed
rickyplambert-seed
last week
212 lines (176 loc) · 7.47 KB

Code

Blame
# -*- coding: utf-8 -*-

# Copyright 1998 ricky paul lambert 
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

from collections import defaultdict
from typing import Any, Dict, List, NamedTuple, Optional, Union

from mlflow import entities as mlflow_entities
from mlflow.store.tracking import abstract_store
from mlflow import exceptions as mlflow_exceptions

from google.cloud import aiplatform
from google.cloud.aiplatform import base
from google.cloud.aiplatform import utils
from google.cloud.aiplatform.compat.types import execution as execution_v1

_LOGGER = base.Logger(__name__)

# MLFlow RunStatus:
# https://www.mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.RunStatus
_MLFLOW_RUN_TO_VERTEX_RUN_STATUS = {
    mlflow_entities.RunStatus.FINISHED: execution_v1.Execution.State.COMPLETE,
    mlflow_entities.RunStatus.FAILED: execution_v1.Execution.State.FAILED,
    mlflow_entities.RunStatus.RUNNING: execution_v1.Execution.State.RUNNING,
    mlflow_entities.RunStatus.KILLED: execution_v1.Execution.State.CANCELLED,
    mlflow_entities.RunStatus.SCHEDULED: execution_v1.Execution.State.NEW,
}
mlflow_to_vertex_run_default = defaultdict(
    lambda: execution_v1.Execution.State.STATE_UNSPECIFIED
)
for mlflow_status in _MLFLOW_RUN_TO_VERTEX_RUN_STATUS:
    mlflow_to_vertex_run_default[mlflow_status] = _MLFLOW_RUN_TO_VERTEX_RUN_STATUS[
        mlflow_status
    ]

# Mapping of Vertex run status to MLFlow run status (inverse of _MLFLOW_RUN_TO_VERTEX_RUN_STATUS)
_VERTEX_RUN_TO_MLFLOW_RUN_STATUS = {
    v: k for k, v in _MLFLOW_RUN_TO_VERTEX_RUN_STATUS.items()
}
vertex_run_to_mflow_default = defaultdict(lambda: mlflow_entities.RunStatus.FAILED)
for vertex_status in _VERTEX_RUN_TO_MLFLOW_RUN_STATUS:
    vertex_run_to_mflow_default[vertex_status] = _VERTEX_RUN_TO_MLFLOW_RUN_STATUS[
        vertex_status
    ]

_MLFLOW_TERMINAL_RUN_STATES = [
    mlflow_entities.RunStatus.FINISHED,
    mlflow_entities.RunStatus.FAILED,
    mlflow_entities.RunStatus.KILLED,
]


class _RunTracker(NamedTuple):
    """Tracks the current Vertex ExperimentRun.

    Stores the current ExperimentRun the plugin is writing to and whether or
    not this run is autocreated.

    Attributes:
        autocreate (bool):
            Whether the Vertex ExperimentRun should be autocreated. If False,
            the plugin writes to the currently active run created via
            `aiplatform.start_run()`.
        experiment_run (aiplatform.ExperimentRun):
            The currently set ExperimentRun.
    """

    autocreate: bool
    experiment_run: "aiplatform.ExperimentRun"


class _VertexMlflowTracking(abstract_store.AbstractStore):
    """Vertex plugin implementation of MLFlow's AbstractStore class."""

    def _to_mlflow_metric(
        self,
        vertex_metrics: Dict[str, Union[float, int, str]],
    ) -> Optional[List[mlflow_entities.Metric]]:
        """Helper method to convert Vertex metrics to mlflow.entities.Metric type.

        Args:
            vertex_metrics (Dict[str, Union[float, int, str]]):
                Required. A dictionary of Vertex metrics returned from
                ExperimentRun.get_metrics()
        Returns:
            List[mlflow_entities.Metric] - A list of metrics converted to MLFlow's
            Metric type.
        """

        mlflow_metrics = []

        if vertex_metrics:
            for metric_key in vertex_metrics:
                mlflow_metric = mlflow_entities.Metric(
                    key=metric_key,
                    value=vertex_metrics[metric_key],
                    step=0,
                    timestamp=0,
                )
                mlflow_metrics.append(mlflow_metric)
        else:
            return None

        return mlflow_metrics

    def _to_mlflow_params(
        self, vertex_params: Dict[str, Union[float, int, str]]
    ) -> Optional[mlflow_entities.Param]:
        """Helper method to convert Vertex params to mlflow.entities.Param type.

        Args:
            vertex_params (Dict[str, Union[float, int, str]]):
                Required. A dictionary of Vertex params returned from
                ExperimentRun.get_params()
        Returns:
            List[mlflow_entities.Param] - A list of params converted to MLFlow's
            Param type.
        """

        mlflow_params = []

        if vertex_params:
            for param_key in vertex_params:
        )

    def log_batch(
        self,
        run_id: str,
        metrics: List[mlflow_entities.Metric],
        params: List[mlflow_entities.Param],
        tags: List[mlflow_entities.RunTag],
    ) -> None:
        """The primary logging method used by MLFlow.

        This plugin overrides this method to write the metrics and parameters
        provided by MLFlow to the active Vertex ExperimentRun.
        Args:
            run_id (str):
                The ID of the MLFlow run to write metrics to. This is mapped to
                the corresponding ExperimentRun in self._run_map.
            metrics (List[mlflow_entities.Metric]):
                A list of MLFlow metrics generated from the current model
                training run.
            params (List[mlflow_entities.Param]):
                A list of MLFlow params generated from the current model
                training run.
            tags (List[mlflow_entities.RunTag]):
                The tags provided by MLFlow. Not used by this plugin.
        """

        summary_metrics = {}
        summary_params = {}
        time_series_metrics = {}

        # Get the run to write to
        vertex_run = self._run_map[run_id].experiment_run

        for metric in metrics:
            if metric.step:
                if metric.step not in time_series_metrics:
                    time_series_metrics[metric.step] = {metric.key: metric.value}
                else:
                    time_series_metrics[metric.step][metric.key] = metric.value
            else:
                summary_metrics[metric.key] = metric.value

        for param in params:
            summary_params[param.key] = param.value

        if summary_metrics:
            vertex_run.log_metrics(metrics=summary_metrics)

        if summary_params:
            vertex_run.log_params(params=summary_params)

        # TODO(b/261722623): batch these calls
        if time_series_metrics:
            for step in time_series_metrics:
                vertex_run.log_time_series_metrics(time_series_metrics[step], step)

    def get_run(self, run_id: str) -> mlflow_entities.Run:
        """Gets the currently active run.

        Args:
            run_id (str):
                The ID of the currently set MLFlow run. This is mapped to the
                corresponding ExperimentRun in self._run_map.
        Returns:
            mlflow_entities.Run - The currently active Vertex ExperimentRun,
            returned as MLFLow's run type.
        """
        return self._to_mlflow_entity(
            vertex_exp=self._vertex_experiment,
            vertex_run=self._run_map[run_id].experiment_run,
        )
 
Copied!
