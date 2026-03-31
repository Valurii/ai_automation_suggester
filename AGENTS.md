# AGENTS.md

## Purpose

`Valurii/ai_automation_suggester` is a public Home Assistant custom integration for generating AI-assisted automation suggestions from the current smart-home graph.

This repo is maintained as a downstream product repo, not as a generic experiment bucket.

## Guardrails

- Preserve Home Assistant compatibility first.
- Do not auto-apply generated automations without explicit review.
- Keep provider integrations configurable and optional.
- Prefer additive maintainer docs and workflow fixes over invasive code churn.

## Branching

- Feature work starts on `feature/*` or `codex/*`.
- Merge into `develop` first.
- Promote `develop` into `main` only after review.

## Maintainer Notes

- Root docs describe product and repo status.
- `custom_components/ai_automation_suggester/` contains the shipped integration.
- HACS and hassfest workflows must stay green on `develop` and `main`.
