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
/Original_operator.md
rickyplambert-seed
rickyplambert-seed
last week
121 lines (99 loc) · 4.34 KB

Preview

Code

Blame
Repository Code 1
(1)Projects
Advanced-intelligence-with-operator rickyplambert About Open GenAI Stack
.github.ai/
Readme License Code of conduct Contributing Contributing Security Security Activity Custom Stars Audit log Report repository Your main branch isn't protected Protect this branch from force pushing or deletion, or require status checks before merging. View documentation. This branch is up to date with rickyplambert-seed/ogx:main. rickyplambert-seed rickyplambert-seed 2 months ago Name .github 3 months ago benchmarking 3 months ago client-sdks 2 months ago containers 3 months ago demo 3 months ago docs 2 months ago paper 4 months ago scripts 3 months ago src 2 months ago tests 2 months ago Repository files navigation README Code of conduct Contributing OGX PyPI Version PyPI Downloads Docker Hub Pulls License Discord Unit Tests Integration Tests OpenResponses Conformance Ask DeepWiki

Quick Start | Documentation | OpenAI API Compatibility | Discord

Important

Llama Stack is now OGX. The name changed, and so did the mission — model-agnostic, multi-SDK, production-grade. Read the full announcement →

Open-source agentic API server for building AI applications. OpenAI-compatible. Any model, any infrastructure.

OGX Architecture

OGX is a drop-in replacement for the OpenAI API that you can run anywhere — your laptop, your datacenter, or the cloud. Use any OpenAI-compatible client or agentic framework. Swap between Llama, GPT, Gemini, Mistral, or any model without changing your application code.

from openai import OpenAI

client = OpenAI(base_url="http://localhost:8321/v1", api_key="fake") response = client.chat.completions.create( model="llama-3.3-70b", messages=[{"role": "user", "content": "Hello"}], ) What you get Chat Completions & Embeddings — standard /v1/chat/completions, /v1/completions, and /v1/embeddings endpoints, compatible with any OpenAI client Responses API — server-side agentic orchestration with tool calling, MCP server integration, and built-in file search (RAG) in a single API call (learn more) Vector Stores & Files — /v1/vector_stores and /v1/files for managed document storage and search Batches — /v1/batches for offline batch processing Skills — /v1alpha/skills for managing versioned skill bundles (zip archives with SKILL.md manifests) that agents can invoke Open Responses conformant — the Responses API implementation passes the Open Responses conformance test suite Multi-SDK support — use the Anthropic SDK (/v1/messages) or Google GenAI SDK (/v1alpha/interactions) natively alongside the OpenAI API Use any model, use any infrastructure OGX has a pluggable provider architecture. Develop locally with Ollama, deploy to production with vLLM, or connect to a managed service — the API stays the same.

See the provider documentation for the full list.

Get started Install and run a OGX server:

One-line install
curl -LsSf https://github.com/ogx-ai/ogx/raw/main/scripts/install.sh | bash

Or install via uv
uv pip install ogx

Start the server (auto-detects providers from the environment)
uv run ogx go Then connect with any OpenAI, Anthropic, or Google GenAI client — Python, TypeScript, curl, or any framework that speaks these APIs.

See the Quick Start guide for detailed setup.

Resources Documentation — full reference OpenAI API Compatibility — endpoint coverage and provider matrix Getting Started Notebook — text and vision inference walkthrough Contributing — how to contribute Client SDKs:

OGX provides official client SDKs for Python and TypeScript:

Language SDK Package Python ogx-client-python PyPI version TypeScript ogx-client-typescript NPM version Alternative Python SDK:

For users who prefer an OpenAPI Generator-based SDK, an alternative Python client is available:

ogx-open-client — Auto-generated from OpenAPI spec, provides similar functionality with a different generation approach Usage Examples — End-to-end code examples for all major features Strategy & Rationale — Why two SDKs, when to use which, and long-term plans The official ogx_client SDK is recommended for most use cases. The ogx_open_client package offers an alternative for teams with specific OpenAPI tooling requirements.

Community We hold regular community calls every Thursday at 09:00 AM PST — see the Community Event on Discord for details.

Star History Chart

Thanks to all our amazing contributors!

