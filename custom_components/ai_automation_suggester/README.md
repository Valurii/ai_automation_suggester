# AI Automation Suggester Component

Core Home Assistant integration for generating AI-assisted automation suggestions from the local entity graph.

This directory contains the custom component that ships through HACS or manual installation. Repository-level maintainer notes, status, and workflow guidance live in the root documentation:

- `README.md`
- `AGENTS.md`
- `docs/STATUS.md`

The component currently focuses on:

- provider-backed suggestion generation
- context-aware prompts built from entities, areas, and optional automation YAML
- persistent notifications plus sensor attributes for dashboard display
- manual review before any automation is applied by the user

For installation and runtime guidance, use the root `README.md`.
