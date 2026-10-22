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
trixie292206021957/gemini/deepmind.gemini/core
/remote_controller.py
rickyplambert-seed
rickyplambert-seed
last month
91 lines (73 loc) · 2.63 KB

Code

Blame
#!/usr/bin/env python3
"""
core/remote_controller.py
Core process execution, environment checking, and remote/local orchestration.
"""

import os
import sys
import subprocess
from pathlib import Path

# Resolve repository root relative to this script: rickyplambert/
REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = REPO_ROOT / "config"
DOCS_DIR = REPO_ROOT / "docs"

SEED_FILE = CONFIG_DIR / "rickyplambert-seed"
MANIFEST_FILE = DOCS_DIR / "rickylambert.txt"
README_FILE = DOCS_DIR / "README.md"


def load_seed() -> str:
    """Reads the authority seed anchor from config/rickyplambert-seed."""
    if not SEED_FILE.is_file():
        raise FileNotFoundError(f"Missing seed file at: {SEED_FILE}")
    with open(SEED_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def verify_manifest() -> bool:
    """Verifies that the manifest file exists and lists repository components."""
    if not MANIFEST_FILE.is_file():
        return False
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest_entries = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    # Check that required files exist
    return all((REPO_ROOT / entry).exists() for entry in manifest_entries if not entry.startswith("http"))


def is_remote() -> bool:
    """
    Determines if current process is running in a remote session.
    Checks SSH session indicators or explicit environmental flags.
    """
    return bool(
        os.getenv("SSH_CLIENT")
        or os.getenv("SSH_TTY")
        or os.getenv("IS_REMOTE") == "1"
    )


def remote(action: str = "status", host: str = None) -> dict:
    """
    Handles remote vs. local dispatch.
    
    Usage:
        if remote("verify"):
            ...
    """
    seed = load_seed() if SEED_FILE.exists() else None
    manifest_ok = verify_manifest()
    remote_session = is_remote()

    result = {
        "is_remote": remote_session,
        "seed_loaded": bool(seed),
        "manifest_valid": manifest_ok,
        "action": action,
        "status": "ready"
    }

    if remote_session:
        # Remote execution path
        print(f"[REMOTE] Operating under seed: {seed[:8]}... | Action: {action}")
        result["mode"] = "remote_node"
    else:
        # Local controller path
        print(f"[LOCAL] Operating controller locally. Manifest valid: {manifest_ok}")
        result["mode"] = "local_node"

    return result


if __name__ == "__main__":
    # Example conditional check
    status = remote("check_tree")
    
    if status.get("is_remote"):
        print("[+] Running remote execution sequence...")
    else:
        print("[+] Running local controller sequence...")
