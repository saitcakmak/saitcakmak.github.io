#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from ax.storage.sqa_store.decoder import Decoder
from ax.storage.sqa_store.encoder import Encoder
from ax.utils.testing.core_stubs import (
    get_abandoned_arm,
    get_arm,
    get_batch_trial,
    get_branin_metric,
    get_branin_objective,
    get_branin_outcome_constraint,
    get_choice_parameter,
    get_ordered_choice_parameter,
    get_task_choice_parameter,
    get_experiment_with_batch_and_single_trial,
    get_experiment_with_batch_trial,
    get_experiment_with_data,
    get_experiment_with_multi_objective,
    get_experiment_with_scalarized_objective_and_outcome_constraint,
    get_factorial_metric,
    get_fixed_parameter,
    get_generator_run,
    get_generator_run2,
    get_hartmann_metric,
    get_metric,
    get_objective,
    get_order_constraint,
    get_outcome_constraint,
    get_parameter_constraint,
    get_range_parameter,
    get_scalarized_objective,
    get_scalarized_outcome_constraint,
    get_simple_experiment_with_batch_trial,
    get_sum_constraint1,
    get_sum_constraint2,
    get_experiment_with_miles_map_data,
    get_synthetic_runner,
    get_trial,
)


TEST_CASES = [
    (
        "AbandonedArm",
        get_abandoned_arm,
        Encoder.abandoned_arm_to_sqa,
        Decoder.abandoned_arm_from_sqa,
    ),
    ("Arm", get_arm, Encoder.arm_to_sqa, Decoder.arm_from_sqa),
    ("BatchTrial", get_batch_trial, Encoder.trial_to_sqa, Decoder.trial_from_sqa),
    ("BraninMetric", get_branin_metric, Encoder.metric_to_sqa, Decoder.metric_from_sqa),
    (
        "BraninObjective",
        get_branin_objective,
        Encoder.objective_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "BraninOutcomeConstraint",
        get_branin_outcome_constraint,
        Encoder.outcome_constraint_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "ChoiceParameter",
        get_choice_parameter,
        Encoder.parameter_to_sqa,
        Decoder.parameter_from_sqa,
    ),
    (
        "ChoiceParameter",
        get_ordered_choice_parameter,
        Encoder.parameter_to_sqa,
        Decoder.parameter_from_sqa,
    ),
    (
        "ChoiceParameter",
        get_task_choice_parameter,
        Encoder.parameter_to_sqa,
        Decoder.parameter_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_batch_trial,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_batch_and_single_trial,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_data,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_multi_objective,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_scalarized_objective_and_outcome_constraint,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "Experiment",
        get_experiment_with_miles_map_data,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "FixedParameter",
        get_fixed_parameter,
        Encoder.parameter_to_sqa,
        Decoder.parameter_from_sqa,
    ),
    (
        "FactorialMetric",
        get_factorial_metric,
        Encoder.metric_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "GeneratorRun",
        get_generator_run,
        Encoder.generator_run_to_sqa,
        Decoder.generator_run_from_sqa,
    ),
    (
        "GeneratorRun",
        get_generator_run2,
        Encoder.generator_run_to_sqa,
        Decoder.generator_run_from_sqa,
    ),
    (
        "HartmannMetric",
        get_hartmann_metric,
        Encoder.metric_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "OrderConstraint",
        get_order_constraint,
        Encoder.parameter_constraint_to_sqa,
        Decoder.parameter_constraint_from_sqa,
    ),
    (
        "ParameterConstraint",
        get_parameter_constraint,
        Encoder.parameter_constraint_to_sqa,
        Decoder.parameter_constraint_from_sqa,
    ),
    ("Metric", get_metric, Encoder.metric_to_sqa, Decoder.metric_from_sqa),
    ("Objective", get_objective, Encoder.objective_to_sqa, Decoder.metric_from_sqa),
    (
        "ScalarizedObjective",
        get_scalarized_objective,
        Encoder.objective_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "OutcomeConstraint",
        get_outcome_constraint,
        Encoder.outcome_constraint_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "ScalarizedOutcomeConstraint",
        get_scalarized_outcome_constraint,
        Encoder.outcome_constraint_to_sqa,
        Decoder.metric_from_sqa,
    ),
    (
        "RangeParameter",
        get_range_parameter,
        Encoder.parameter_to_sqa,
        Decoder.parameter_from_sqa,
    ),
    (
        "SimpleExperiment",
        get_simple_experiment_with_batch_trial,
        Encoder.experiment_to_sqa,
        Decoder.experiment_from_sqa,
    ),
    (
        "SyntheticRunner",
        get_synthetic_runner,
        Encoder.runner_to_sqa,
        Decoder.runner_from_sqa,
    ),
    (
        "SumConstraint",
        get_sum_constraint1,
        Encoder.parameter_constraint_to_sqa,
        Decoder.parameter_constraint_from_sqa,
    ),
    (
        "SumConstraint",
        get_sum_constraint2,
        Encoder.parameter_constraint_to_sqa,
        Decoder.parameter_constraint_from_sqa,
    ),
    ("Trial", get_trial, Encoder.trial_to_sqa, Decoder.trial_from_sqa),
]
