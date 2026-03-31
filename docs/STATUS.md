# Status

## Repo Role

Public Home Assistant integration for suggesting automations from a live entity graph using configurable AI providers.

## Current State

- HACS-style custom integration with config flow and service interface
- Public downstream repo under `Valurii`
- Suitable for continued product hardening, not just archival reference

## Current Focus

- keep metadata and Home Assistant packaging clean
- preserve safe review-first automation suggestion flow
- improve provider/runtime quality without making the integration destructive

## Known Constraints

- upstream lineage exists, but this repo is now maintained as its own public downstream
- tests are lightweight and should be expanded carefully around Home Assistant harness behavior
