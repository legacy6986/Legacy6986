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
trixie292206021957/core
/reclaim_rag.py
rickyplambert-seed
rickyplambert-seed
5 days ago
83 lines (69 loc) · 3.06 KB

Code

Blame
=== TRIXIE LOCAL: HEIR PROTOCOL ENGINEERING BUNDLE ===
Timestamp: 2026-09-24T20:24:19.997Z

--- reclaim_rag.py ---
import re
import torch
import torch.nn as nn
from typing import List

class ContextCompressor(nn.Module):
    def __init__(self, hidden_dim: int = 4096, target_tokens: int = 8):
        super().__init__()
        self.projection = nn.Linear(hidden_dim, hidden_dim)
        self.target_tokens = target_tokens

    def forward(self, chunk_hidden_states: torch.Tensor) -> torch.Tensor:
        compressed = self.projection(chunk_hidden_states)
        return compressed[:, :self.target_tokens, :]

def build_reclaim_prompt(query: str, retrieved_chunks: List[str]) -> str:
    formatted = "\n".join([f"[{i}] {c}" for i, c in enumerate(retrieved_chunks)])
    return f"""You are an objective, highly verifiable AI assistant.
Answer the user query using ONLY the provided reference sources.
For every sentence you write, you must strictly alternate by specifying the reference tag first, followed immediately by the factual claim sentence.

Reference Sources:
{formatted}

User Query: {query}

Format your output strictly as:
[Ref: <Source_ID>] Claim: <Generated Sentence>
"""

def parse_and_verify_claims(generated_output: str, source_texts: List[str]) -> List[dict]:
    pattern = r"\[Ref:\s*(\d+)\]\s*Claim:\s*(.+?)(?=\n*\[Ref:|$)"
    matches = re.findall(pattern, generated_output, re.DOTALL)
    return [
        {
            "source_id": int(sid),
            "claim": claim.strip(),
            "grounded": int(sid) < len(source_texts),
            "source_snippet": source_texts[int(sid)][:100] if int(sid) < len(source_texts) else None
        }
        for sid, claim in matches
    ]

--- ai_triage.py ---
from enum import Enum
from pydantic import BaseModel, Field

class SeverityLevel(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class VulnerabilityInput(BaseModel):
    vuln_id: str
    cvss_score: float = Field(..., ge=0.0, le=10.0)
    component: str
    is_production: bool = False

def assess_vulnerability(vuln: VulnerabilityInput):
    score = vuln.cvss_score
    if vuln.is_production and score >= 7.0:
        score = min(10.0, score + 0.5)

    if score >= 9.0:
        return {"severity": "Critical", "window": "Immediate (0 - 24 Hours)", "action": "Halt deployment, execute container rebuild, and trigger automated patch."}
    elif score >= 7.0:
        return {"severity": "High", "window": "Rapid (1 - 7 Days)", "action": "Deploy patch to staging, verify permissions, and schedule maintenance window."}
    elif score >= 4.0:
        return {"severity": "Medium", "window": "Scheduled (7 - 30 Days)", "action": "Queue configuration adjustment for next routine sprint update."}
    else:
        return {"severity": "Low", "window": "Maintenance (30 - 90 Days)", "action": "Log for backlog review during dependency updates."}

--- .github/CODEOWNERS ---
# Order matters - the last matching pattern takes precedence
* @our-org/core-team
*.js @our-org/frontend-team
*.tsx @our-org/frontend-team
/src/security/ @security-lead-user @our-org/sec-team
