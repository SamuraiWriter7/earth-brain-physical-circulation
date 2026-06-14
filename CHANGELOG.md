# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based early versioning style during the initial architecture phase.

---

## [v0.1.0-candidate] - 2026-06-14

### Added

* Added initial repository foundation for **Earth Brain Physical Circulation**.
* Added `README.md` describing the purpose, concept, repository structure, validation flow, and design principles.
* Added `docs/physical-circulation-overview.md`.

  * Defines the Physical Circulation Layer for Earth Brain OS.
  * Introduces the relationship between Wind Circulation Layer, Optical Nervous Layer, and Physical Compute Substrate.
  * Frames hardware as physical organs inside a civilizational operating system.
* Added `docs/wind-circulation-layer.md`.

  * Defines the Wind Circulation Layer.
  * Introduces the organ model:

    * Compute Lung
    * Cognitive Muscle
    * Silent Pressure Organ
    * Circulation Chamber
    * Power Meridian
    * Stable Peripheral Cell
  * Defines thermal regulation, airflow coordination, acoustic regulation, compute rhythm, power-compute synchronization, local sustainability, and rest/recovery.
  * Defines Wind Node lifecycle states.
* Added `schemas/wind-node.schema.json`.

  * Defines the initial JSON Schema for Wind Node records.
  * Includes thermal, airflow, acoustic, cooling, power, memory, network, lifecycle, and circulation policy properties.
* Added `examples/wind-node.example.yaml`.

  * Provides a valid example of a local AI compute node as a Wind Node.
  * Demonstrates quiet operation, local-first execution, cooldown after burst execution, and escalation when strained.
* Added `scripts/validate_examples.py`.

  * Validates example YAML files against JSON Schemas.
  * Currently validates `examples/wind-node.example.yaml` against `schemas/wind-node.schema.json`.
* Added `.github/workflows/validate-examples.yml`.

  * Runs validation on push, pull request, and manual dispatch.
  * Checks Python syntax.
  * Runs schema validation for example files.

### Validated

* Confirmed that the GitHub Actions validation workflow passes.
* Confirmed that the initial Wind Node example validates against the Wind Node schema.
* Confirmed that the repository now includes a complete minimum loop:

```text
documentation
→ schema
→ example
→ validation script
→ GitHub Actions
```

### Architectural Meaning

This release introduces the first physical infrastructure layer for Earth Brain OS.

The core shift is:

> Earth Brain OS is not only an informational architecture. It also requires physical breath, circulation, cooling, power stability, and local sustainability.

The `v0.1.0-candidate` release establishes the Wind Circulation Layer as the first validated physical organ model of Earth Brain OS.

### Current Scope

This version focuses on:

* Physical Circulation overview
* Wind Circulation Layer
* Wind Node schema
* Wind Node example
* validation workflow

### Future Direction

Possible next versions may add:

* Optical Nervous Layer documentation
* Optical Node schema
* Optical Node example
* Hybrid Wind/Optical Node model
* circulation outcome logs
* thermal-acoustic routing policies
* Earth Brain OS integration records
