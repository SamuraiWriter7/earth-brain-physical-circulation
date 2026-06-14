# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based early versioning style during the initial architecture phase.

---

## [v0.4.0-candidate] - 2026-06-14

### Added

* Added `docs/physical-circulation-trace.md`.

  * Defines the Physical Circulation Trace model for Earth Brain OS.
  * Introduces operational records for Wind Nodes, Optical Nodes, and Hybrid Nodes.
  * Defines trace types:

    * wind_circulation_outcome
    * optical_routing_outcome
    * hybrid_execution_outcome
    * fallback_escalation
    * rest_recovery
  * Defines how physical traces record task execution, thermal change, acoustic change, power change, routing decisions, memory access, fallback behavior, cloud escalation, rest and recovery, final outcome, and learning signals.
  * Defines the relationship between Physical Circulation Trace and the Memory / Trace Layer.
* Added `schemas/physical-circulation-trace.schema.json`.

  * Defines the initial JSON Schema for Physical Circulation Trace records.
  * Includes trace identity, trace type, source node, target node, task ID, lifecycle states, Wind state, Optical route, memory path, fallback status, cloud escalation status, rest requirement, rest recovery, outcome, learning signal, and notes.
* Added `examples/physical-circulation-trace.example.yaml`.

  * Provides a valid example of a Hybrid Node execution outcome.
  * Demonstrates local execution, thermal change, acoustic change, power change, optical route, memory path, fallback status, cloud escalation status, rest requirement, recovery action, and learning signal.
* Updated `scripts/validate_examples.py`.

  * Added validation support for `examples/physical-circulation-trace.example.yaml`.
  * The validator now checks Wind Node, Optical Node, Hybrid Node, and Physical Circulation Trace examples.
* Updated `README.md`.

  * Added Physical Circulation Trace overview.
  * Added Physical Circulation Trace schema and example sections.
  * Updated repository structure, key documents, current version, design principles, non-goals, and future direction.

### Validated

* Confirmed that the GitHub Actions validation workflow passes.
* Confirmed that `examples/wind-node.example.yaml` validates against `schemas/wind-node.schema.json`.
* Confirmed that `examples/optical-node.example.yaml` validates against `schemas/optical-node.schema.json`.
* Confirmed that `examples/hybrid-node.example.yaml` validates against `schemas/hybrid-node.schema.json`.
* Confirmed that `examples/physical-circulation-trace.example.yaml` validates against `schemas/physical-circulation-trace.schema.json`.
* Confirmed that the repository now validates four physical models:

  * Wind Node
  * Optical Node
  * Hybrid Node
  * Physical Circulation Trace

### Fixed During Candidate Development

* Fixed YAML indentation issues in `examples/physical-circulation-trace.example.yaml`.
* Confirmed that nested objects such as `wind_state`, `optical_route`, `memory_path`, `rest_recovery`, and `learning_signal` are correctly parsed as objects.
* Confirmed that the Physical Circulation Trace example passes validation cleanly.

### Architectural Meaning

This release gives Earth Brain OS its first physical operation memory model.

The previous releases established:

```text
v0.1.0-candidate
Wind Node
= internal breathing and physical stability

v0.2.0-candidate
Optical Node
= external connection and signal coordination

v0.3.0-candidate
Hybrid Node
= integrated execution, circulation, routing, memory, fallback, and recovery
```

The `v0.4.0-candidate` release introduces:

```text
Physical Circulation Trace
= operational memory of physical behavior, routing, fallback, rest, and recovery
```

Together, these four models allow Earth Brain OS to describe:

* how local AI nodes sustain computation physically
* how local AI nodes coordinate through nervous signal flow
* how real-world hybrid AI devices execute and route work while respecting physical limits
* how the physical body records what happened and learns from operation

The core shift is:

> Earth Brain OS now has breathing organs, nervous pathways, integrated hybrid organs, and physical memory.

### Current Scope

This version focuses on:

* Physical Circulation Trace documentation
* Physical Circulation Trace schema
* Physical Circulation Trace example
* validator expansion
* README update for Wind + Optical + Hybrid + Trace architecture

### Future Direction

Possible next versions may add:

* nervous routing outcome logs
* hybrid trace records
* thermal-acoustic routing policies
* breathing reasoning node profiles
* Earth Brain OS integration records
* physical circulation event schemas
* physical circulation recurrence rules
* physical health scoring for local AI nodes

---

## [v0.3.0-candidate] - 2026-06-14

### Added

* Added `docs/hybrid-wind-optical-node.md`.

  * Defines the Hybrid Wind/Optical Node model for Earth Brain OS.
  * Introduces physical AI nodes that combine Wind Circulation and Optical Nervous responsibilities.
  * Defines local execution, circulation awareness, nervous routing, memory proximity, signal prioritization, fallback and escalation, rest and recovery, and hybrid trace logging.
  * Defines Hybrid Node lifecycle states:

    * registered
    * idle
    * available
    * active
    * routing
    * strained
    * cooling
    * congested
    * resting
    * degraded
    * fallback_only
    * offline
* Added `schemas/hybrid-node.schema.json`.

  * Defines the initial JSON Schema for Hybrid Node records.
  * Includes Wind profile, Optical profile, execution policy, routing policy, memory policy, fallback policy, trace policy, lifecycle state, and notes.
* Added `examples/hybrid-node.example.yaml`.

  * Provides a valid example of a local AI workstation as a Hybrid Node.
  * Demonstrates local execution, Wind state awareness, optical coordination, memory proximity, fallback policy, and hybrid trace logging.
* Updated `scripts/validate_examples.py`.

  * Added validation support for `examples/hybrid-node.example.yaml`.
  * The validator now checks Wind Node, Optical Node, and Hybrid Node examples.
* Updated `README.md`.

  * Added Hybrid Wind/Optical Node overview.
  * Added Hybrid Node schema and example sections.
  * Updated repository structure, key documents, current version, design principles, and future direction.

### Validated

* Confirmed that the GitHub Actions validation workflow passes.
* Confirmed that `examples/wind-node.example.yaml` validates against `schemas/wind-node.schema.json`.
* Confirmed that `examples/optical-node.example.yaml` validates against `schemas/optical-node.schema.json`.
* Confirmed that `examples/hybrid-node.example.yaml` validates against `schemas/hybrid-node.schema.json`.
* Confirmed that the repository now validates three physical node models:

  * Wind Node
  * Optical Node
  * Hybrid Node

### Fixed During Candidate Development

* Fixed YAML list marker confusion in `examples/hybrid-node.example.yaml`.
* Fixed nested mapping indentation issues in `examples/hybrid-node.example.yaml`.
* Simplified the Hybrid Node example to reduce YAML nesting fragility while preserving schema coverage.
* Confirmed that the Hybrid Node example now passes validation cleanly.

### Architectural Meaning

This release gives Earth Brain OS its first integrated physical local organ model.

The `v0.1.0-candidate` release established the Wind Circulation Layer:

```text
Wind Node
= internal breathing and physical stability
```

The `v0.2.0-candidate` release added the Optical Nervous Layer:

```text
Optical Node
= external connection and signal coordination
```

The `v0.3.0-candidate` release introduces the Hybrid Wind/Optical Node:

```text
Hybrid Node
= integrated execution, circulation, routing, memory, fallback, and recovery
```

Together, these three models allow Earth Brain OS to describe:

* how local AI nodes sustain computation physically
* how local AI nodes coordinate through nervous signal flow
* how real-world hybrid AI devices both execute and route work while respecting physical circulation limits

The core shift is:

> Earth Brain OS now has breathing organs, nervous pathways, and integrated hybrid organs.

### Current Scope

This version focuses on:

* Hybrid Wind/Optical Node documentation
* Hybrid Node schema
* Hybrid Node example
* validator expansion
* README update for Wind + Optical + Hybrid architecture

### Future Direction

Possible next versions may add:

* circulation outcome logs
* nervous routing outcome logs
* hybrid trace records
* thermal-acoustic routing policies
* breathing reasoning node profiles
* Earth Brain OS integration records
* physical circulation event schemas

---

## [v0.2.0-candidate] - 2026-06-14

### Added

* Added `docs/optical-nervous-layer.md`.

  * Defines the Optical Nervous Layer for Earth Brain OS.
  * Introduces local-first routing, node discovery, signal prioritization, memory access coordination, task routing, fallback and escalation, and nervous trace logging.
  * Defines the relationship between Optical Nervous Layer and Wind Circulation Layer.
  * Introduces Optical Node lifecycle states:

    * registered
    * discoverable
    * available
    * routing
    * congested
    * degraded
    * fallback_only
    * offline
* Added `schemas/optical-node.schema.json`.

  * Defines the initial JSON Schema for Optical Node records.
  * Includes connection, latency, bandwidth, routing policy, memory access, Wind Node links, fallback paths, lifecycle, and nervous trace policy properties.
* Added `examples/optical-node.example.yaml`.

  * Provides a valid example of a local AI router as an Optical Node.
  * Demonstrates local-first routing, memory-near-compute preference, Wind Circulation state awareness, fallback routing, and cloud escalation as a last-resort path.
* Updated `scripts/validate_examples.py`.

  * Added validation support for `examples/optical-node.example.yaml`.
  * The validator now checks both Wind Node and Optical Node examples.
* Updated `.github/workflows/validate-examples.yml`.

  * Updated the workflow job name to reflect validation of both Wind and Optical Node examples.
* Updated `README.md`.

  * Added Optical Nervous Layer overview.
  * Added Optical Node schema and example sections.
  * Updated repository structure, key documents, current version, design principles, and future direction.

### Validated

* Confirmed that the GitHub Actions validation workflow passes.
* Confirmed that `examples/wind-node.example.yaml` validates against `schemas/wind-node.schema.json`.
* Confirmed that `examples/optical-node.example.yaml` validates against `schemas/optical-node.schema.json`.
* Confirmed that the repository now validates both physical breathing and optical nervous coordination structures.

### Architectural Meaning

This release gives Earth Brain OS its first optical nervous layer.

The `v0.1.0-candidate` release established the Wind Circulation Layer:

```text
Wind Circulation Layer
= internal breathing and physical stability
```

The `v0.2.0-candidate` release adds the Optical Nervous Layer:

```text
Optical Nervous Layer
= external connection and signal coordination
```

Together, these layers allow Earth Brain OS to describe both:

* how a local AI node sustains physical computation
* how local AI nodes, memory nodes, routers, and gateways coordinate through nervous signal flow

The core shift is:

> Earth Brain OS now has both breath and nerves.

### Current Scope

This version focuses on:

* Optical Nervous Layer documentation
* Optical Node schema
* Optical Node example
* validator expansion
* README update for Wind + Optical two-layer architecture

### Future Direction

Possible next versions may add:

* Hybrid Wind/Optical Node model
* circulation outcome logs
* nervous routing outcome logs
* thermal-acoustic routing policies
* breathing reasoning node profiles
* Earth Brain OS integration records
* physical circulation event schemas

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
  * Initially validates `examples/wind-node.example.yaml` against `schemas/wind-node.schema.json`.
* Added `.github/workflows/validate-examples.yml`.

  * Runs validation on push, pull request, and manual dispatch.
  * Checks Python syntax.
  * Runs schema validation for example files.

### Validated

* Confirmed that the GitHub Actions validation workflow passes.
* Confirmed that the initial Wind Node example validates against the Wind Node schema.
* Confirmed that the repository includes a complete minimum loop:

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
