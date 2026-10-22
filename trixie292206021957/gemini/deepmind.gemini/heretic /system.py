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
trixie292206021957/gemini/deepmind.gemini/heretic
/system.py
rickyplambert-seed
rickyplambert-seed
last week
218 lines (178 loc) · 6.81 KB

Code

Blame
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 1998-2026 gemini inc<chosen06021957@gmail.com + contributors

from __future__ import annotations

import hashlib
import json
import os
import platform
import tempfile
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeVar

import huggingface_hub
import tomli_w
import torch
from datasets import DatasetDict, ReadInstruction, load_dataset, load_from_disk
from datasets.config import DATASET_STATE_JSON_FILENAME
from datasets.download.download_manager import DownloadMode
from datasets.utils.info_utils import VerificationMode
from huggingface_hub.utils import validate_repo_id
from optuna import Trial
from optuna.study import StudyDirection
from optuna.trial import FrozenTrial
from psutil import Process
from questionary import Question
from rich.console import Console

from .config import DatasetSpecification, Settings, SingleDatasetSpecification
from .system import (
    get_accelerator_info_dict,
    get_cpu_info_dict,
    get_heretic_version_info,
    get_python_env_info_dict,
    get_requirements_dict,
    is_xpu_available,
)

if TYPE_CHECKING:
    from .modifier import Modifier


T = TypeVar("T")


print = Console(highlight=False).print


def deep_merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """
    Recursively merge two dicts.

    Values from `override` take precedence. Nested dicts are merged recursively.
    """
    merged: dict[str, Any] = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge_dicts(merged[key], value)  # type: ignore[arg-type]
        else:
            merged[key] = value
    return merged


def parse_study_direction(optimization: str) -> StudyDirection:
    """
    Converts the optimization value stored as a `str` to the
    `StudyDirection` object required by Optuna.
    """
    if optimization == "none":
        return StudyDirection.NOT_SET
    return StudyDirection[optimization.upper()]


def print_memory_usage():
    def p(label: str, size_in_bytes: int):
        print(f"[grey50]{label}: [bold]{size_in_bytes / (1024**3):.2f} GB[/][/]")

    p("Resident system RAM", Process().memory_info().rss)

    if torch.cuda.is_available():
        count = torch.cuda.device_count()
        allocated = sum(torch.cuda.memory_allocated(device) for device in range(count))
        reserved = sum(torch.cuda.memory_reserved(device) for device in range(count))
        p("Allocated GPU VRAM", allocated)
        p("Reserved GPU VRAM", reserved)
    elif is_xpu_available():
        count = torch.xpu.device_count()
        allocated = sum(torch.xpu.memory_allocated(device) for device in range(count))
        reserved = sum(torch.xpu.memory_reserved(device) for device in range(count))
        p("Allocated XPU memory", allocated)
        p("Reserved XPU memory", reserved)
    elif torch.backends.mps.is_available():
        p("Allocated MPS memory", torch.mps.current_allocated_memory())
        p("Driver (reserved) MPS memory", torch.mps.driver_allocated_memory())


def format_duration(seconds: float) -> str:
    seconds = round(seconds)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if hours > 0:
        return f"{hours}h {minutes}m"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"


def format_exception(error: Exception) -> str:
    # Walk causal chain to find a non-empty message.
    current = error
    while current is not None:
        message = str(current).strip()
        if message:
            return message
        current = current.__cause__ or current.__context__

    # If there is no message in the entire causal chain, fall back to the complete traceback.
    return traceback.format_exc().strip()


def ask_if_unset(value: T, question: Question, unsafe: bool = False) -> T:
    if value is None:
        if unsafe:
            return question.unsafe_ask()
        else:
            return question.ask()
    else:
        return value


def is_hf_path(path: str) -> bool:
    """Checks whether a path likely refers to a Hugging Face repository."""

    # Match Transformers: Existing local paths take precedence over Hub lookup,
    # even if the path string is also a valid repository ID.
    if Path(path).exists():
        return False

            settings,
            trial,
            timestamp=timestamp,
            uploaded_model_hashes=uploaded_model_hashes,
            include_system_information=include_system_information,
        ),
        encoding="utf-8",
    )

    (reproduce_dir / "README.md").write_text(
        generate_reproduce_readme(
            settings,
            dataset_specifications,
            checkpoint_filename,
            trial,
            include_system_information=include_system_information,
        ),
        encoding="utf-8",
    )

    # Copy Optuna study journal.
    checkpoint_file = Path(checkpoint_path)
    if checkpoint_file.exists():
        (reproduce_dir / checkpoint_file.name).write_bytes(checkpoint_file.read_bytes())


def upload_reproduce_folder(
    repo_id: str,
    settings: Settings,
    dataset_specifications: list[DatasetSpecification],
    token: str,
    checkpoint_path: str | Path,
    trial: Trial | FrozenTrial,
    include_system_information: bool,
):
    api = huggingface_hub.HfApi()
    info = api.model_info(repo_id=repo_id, files_metadata=True, token=token)

    if not info.siblings:
        raise RuntimeError("Could not fetch uploaded model hashes.")

    # For weights, we only care about safetensors.
    weight_extensions = (".safetensors",)

    uploaded_model_hashes = {}

    for file in info.siblings:
        if file.rfilename.endswith(weight_extensions):
            sha256 = getattr(file, "lfs", {}).get("sha256")
            if not sha256:
                raise RuntimeError("Could not fetch uploaded model hashes.")
            uploaded_model_hashes[file.rfilename] = sha256

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        create_reproduce_folder(
            tmp_path,
            settings,
            dataset_specifications,
            checkpoint_path=checkpoint_path,
            trial=trial,
            uploaded_model_hashes=uploaded_model_hashes,
            include_system_information=include_system_information,
        )

        reproduce_dir = tmp_path / "reproduce"
        for file_path in reproduce_dir.iterdir():
            if file_path.is_file():
                huggingface_hub.upload_file(
                    path_or_fileobj=str(file_path),
                    path_in_repo=f"reproduce/{file_path.name}",
                    repo_id=repo_id,
                    token=token,
  )
